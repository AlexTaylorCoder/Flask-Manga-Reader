#Scraper
from bs4 import BeautifulSoup
from collections import deque
import requests
class Scraper(BeautifulSoup):
    def __init__(self,url) -> None:
        super().__init__()
        body = requests.get(url).text
        self.soup = BeautifulSoup(body,"html.parser")
    # def select(self):
    #     super(Scraper,self).select()
    



class MangakalotScraper:
    def __init__(self) -> None:
        self.latest_page = 1
        self.hot_page = 1
        self.new_page = 1
        self.search_page = 1

        self.hot_url = f"https://mangakakalot.com/manga_list?type=topview&category=all&state=all&page={self.hot_page}"
        self.latest_url = f"https://mangakakalot.com/manga_list?type=latest&category=all&state=all&page={self.latest_page}"
        self.new_url = f"https://mangakakalot.com/manga_list?type=newest&category=all&state=all&page={self.new_page}"
        self.search_url = f"https://mangakakalot.com/search/story/"

        #Structured this way to abstract when using class, less params needed to be passed in
    def hot(self):
        scrapedHTML = Scraper(self.hot_url).soup
        self.selectbody(scrapedHTML)
    def latest(self):
        scrapedHTML = Scraper(self.latest_url).soup
        self.selectbody(scrapedHTML)
    def new(self):
        scrapedHTML = Scraper(self.latest_url).soup
        self.selectbody(scrapedHTML)
    def search(self,query):
        scrapedHTML = Scraper(f"{self.search_url}{query}?page={self.search_page}").soup
        self.selectbody(scrapedHTML)
    def selectbody(self,html):
        return html.select("body > div.container > div.main-wrapper > div.leftCol.listCol > div")
    def nextHotPage(self):
         self.hot_page += 1
    def nextNewPage(self):
        self.new_page += 1 
    def nextLatestPage(self):
        self.latest_page +=1


class MangaParkScraper:
    #API maintains search by remembering last manga id ?langs=en
    #For latest has button with id url so need to get link
    #For search next pages follows typical pagination pattern
    base_url = "https://mangapark.io/"
    def __init__(self) -> None:
        self.search_page = 1
        self.latest_pages_cache = deque()
        # self.latest_pages = 
        #To navigate between links doubly linked list structure seems best, so deque
        self.home_url = self.base_url + "v3x?langs=en"
        self.latest_url = self.base_url + "latest?langs=en&prevPos="
        self.search_url = self.base_url + f"search?page={self.search_page}&word="
    
    def home(self):
        scrapedHTML = Scraper(self.home_url).soup
        self.selectbody(scrapedHTML)
    #For latest should save links to page to navigate between
    def latest(self,next=None):
        scrapedHTML = Scraper(self.latest_url+next).soup
        self.selectbody(scrapedHTML)
        nextPage = self.nextpageurl(scrapedHTML)
        self.latest_pages_cache.append(nextPage)
    #Space represented by +
    def search(self,query):
        scrapedHTML = Scraper(f"{self.search_url}{query}").soup
        #Format the html into json
        content = self.selectbody(scrapedHTML)
        mangas = []
        # "type":manga["type"],
        # "title":title,
        # "en-title": enTitle,
        # "description": description,
        # "demo":manga["attributes"]["publicationDemographic"],
        # "status":manga["attributes"]["status"],
        # "rating":manga["attributes"]["contentRating"],
        # "tags":tags,
        # "api_id": id,
        # "cover_url": cover_url or None
        for manga in content:
            #Querying inwards to reduce amount of css selectors needed
            latest_chapter = manga.select_one("div .d-flex.align-items-center.flex-shrink-1 a") 
            titleElement = manga.select_one("div .ps-2.d-flex.flex-column.flex-grow-1 a")
            title = titleElement["title"] if titleElement else None


            # breakpoint()
            descriptionElement = manga.select_one("div div div .limit-html")
            description = descriptionElement.text if descriptionElement else None
            enTitleElement = manga.select_one("div .mt-1.small.text-muted.text-ellipsis-2.alias > span:nth-child(2)")
            enTitle = enTitleElement.text if enTitleElement else None
            #search-list > div:nth-child(3) > div > div.mt-1.small.text-muted.text-ellipsis-2.alias > span:nth-child(2) > span:nth-child(2)
            categories = manga.select_one("div .mt-1.small.text-muted.text-ellipsis-2.genres")
#search-list > div:nth-child(3) > div > a
            details = manga.select_one("a")
            # breakpoint()
            print(latest_chapter)
            # breakpoint()
            tags = []
            for category in categories.select("span"):
                if category != "Japanese":
                    tags.append(category.text)


            demo = "adult" if categories.select_one("b") else "safe"
            type = categories.select_one("u").text if categories.select_one("u") else None

            # Need to verify that it exists for specific manga
            mangas.append({
            "title": title,
            "en-title": enTitle,
            "description": description,
            "type": type,
            "api_id": details["href"].split("/")[1],
            "tags":tags,
            "cover_url":details.img["src"],
            "details_link":details["href"],
            "demo":demo,
            "latest_url": latest_chapter["href"] if latest_chapter else "No Link Available",
            "latest_text": latest_chapter.text if latest_chapter else "No Text Available"})
        # breakpoint()
        return mangas
    def selectbody(self,html):
        return html.select("div.col.mt-3.pb-3.d-flex.item.line-b")
    def details(self,link):
        scrapedHTML = Scraper(self.base_url+link).soup
        


    def nextpageurl(self,html):
        return html.select_one("#mainer > div .btn.btn-warning").href
    def nextlatestpage(self):
        next = self.latest_pages_cache[-1]
        self.latest(self.latest_url,next)
    def nextsearchpage(self):
        self.search_page += 1
    
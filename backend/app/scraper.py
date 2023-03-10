#Scraper
from bs4 import BeautifulSoup
from collections import deque
import requests
class Scraper:
    def __init__(self,url) -> None:
        body = requests.get(url).body
        self.soup = BeautifulSoup(body)



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
        scrapedHTML = Scraper(self.hot_url)
        self.selectbody(scrapedHTML)
    def latest(self):
        scrapedHTML = Scraper(self.latest_url)
        self.selectbody(scrapedHTML)
    def new(self):
        scrapedHTML = Scraper(self.latest_url)
        self.selectbody(scrapedHTML)
    def search(self,query):
        scrapedHTML = Scraper(f"{self.search_url}{query}?page={self.search_page}")
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
    def __init__(self) -> None:
        self.search_page = 1
        self.latest_pages_cache = deque()
        # self.latest_pages = 
        #To navigate between links doubly linked list structure seems best, so deque
        self.home_url = "https://mangapark.io/v3x?langs=en"
        self.latest_url = "https://mangapark.io/latest?langs=en&prevPos="
        self.search_url = f"https://mangapark.io/search?page={self.search_page}&word="
    def home(self):
        scrapedHTML = Scraper(self.home_url)
        self.selectbody(scrapedHTML)
    #For latest should save links to page to navigate between
    def latest(self,next=None):
        scrapedHTML = Scraper(self.latest_url+next)
        self.selectbody(scrapedHTML)
        nextPage = self.nextpageurl(scrapedHTML)
        self.latest_pages_cache.append(nextPage)
    #Space represented by +
    def search(self,query):
        scrapedHTML = Scraper(f"{self.search_url}{query}")
        self.selectbody(scrapedHTML)
    def selectbody(self,html):
        return html.select("div.col.mt-3.pb-3.d-flex.item.line-b")
    def nextpageurl(self,html):
        return html.select_one("#mainer > div .btn.btn-warning").href
    def nextlatestpage(self):
        next = self.latest_pages_cache[-1]
        self.latest(self.latest_url,next)
    def nextsearchpage(self):
        self.search_page += 1
    
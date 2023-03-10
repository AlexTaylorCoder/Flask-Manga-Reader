#Scraper
from bs4 import BeautifulSoup
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
        self.selectbody()
    def latest(self):
        scrapedHTML = Scraper(self.latest_url)
        self.selectbody()
    def new(self):
        scrapedHTML = Scraper(self.latest_url)
        self.selectbody()
    def search(self,query):
        scrapedHTML = Scraper(f"{self.search_url}{query}?page={self.search_page}")
        self.selectbody()
    def selectbody(self,html):
        return html.select("body > div.container > div.main-wrapper > div.leftCol.listCol > div")


    def nextHotPage(self):
         self.hot_page += 1
    def nextNewPage(self):
        self.new_page += 1 
    def nextLatestPage(self):
        self.latest_page +=1


#Scraper
from bs4 import BeautifulSoup
import requests
class Scraper:
    def __init__(self,url) -> None:
        body = requests.get(url).body
        self.soup = BeautifulSoup(body)
    

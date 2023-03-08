import requests
import os
class Mangadex:
    base_url = "https://api.mangadex.org"
    base_manga_url = "https://api.mangadex.org/manga"
    stats_url = "https://api.mangadex.org/statistics/manga/"
    
    def __init__(self):
        pass 
    def search(self,params):
        response = requests.get(self.base_manga_url,
                                params=params)
        
        response.raise_for_status()
        
        manga_data = response.json()
        
        stats_response = requests.get(self.stats_url+manga_data.id)

        stats_response.raise_for_status()

        stats_data = stats_response.json()

        return {manga_data,stats_data}
    
    def chapters(self,manga_id):
        #Find chapters
        response = requests.get(f"{self.base_manga_url}/{manga_id}/feed",params={"translatedLanguage[]":["en"]})
        chapter_info = response.json()

        return [chapter["id"] for chapter in chapter_info["data"]]

    def chapter(self,chapter_id):
            #Find closest server that chapter is served on
        response_server = requests.get(f"{self.base_url}/at-home/server/{chapter_id}")
        chapter_server_data = response_server.json()

        return [chapter_server_data["baseUrl"],chapter_server_data["chapter"]["hash"],chapter_server_data["chapter"]["data"],chapter_server_data["chapter"]["dataSaver"]]
    
    def page(self,host,chapterHash,page,highRes=False):

        #This should just be an image url
        # May need to proxy image aka download onto server and serve from there
        quality = "data" if highRes else "data-saver"
        img_url = f"{host}/{quality}/{chapterHash}/{page}"
        response_image = requests.get(img_url)

        return response_image.content, img_url

    def download(self,img):
        # With saved images add /user to path
        # with open(f"{folder_path}/{page}", mode="wb") as f:
        #     f.write(img)
        pass

    #A page is an image
    def chapter_pages(self,manga_id,highRes=False):
        chapter_data = self.chapter(chapter_id=2)
        quality = 2 if highRes else 3
        for page in chapter_data[quality]:
            self.page(host=chapter_data[0],chapterHash=chapter_data[1],page=page)

        






# def fetch_handling_get(url,params={}):
#     try:
#         r = requests.get(url,params=params)
#         r.raise_for_status()
#     except requests.exceptions.HTTPError as err:
#         raise SystemExit(err)

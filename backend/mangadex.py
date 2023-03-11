import requests
import os
class Mangadex:
    base_url = "https://api.mangadex.org"
    base_manga_url = f"{base_url}/manga"
    stats_url = f"{base_url}/statistics/manga/"
    tags_url = f"{base_url}/manga/tag"
    cover_url = f"{base_url}/cover/"
    cover_image_url = "https://uploads.mangadex.org/covers/"
    
    def __init__(self):
        pass 
    def search(self,query,includedTags=None,excludedTags=None,cover=True):

        #To add filter by tag need request to tags
        params = { "title":query}
        if includedTags or excludedTags:
            tags = requests.get(self.tags_url).json()

            included_tag_ids = [
            tag["id"]
            for tag in tags["data"]
            if tag["attributes"]["name"]["en"]
            in includedTags
            ]

            excluded_tag_ids = [
            tag["id"]
            for tag in tags["data"]
            if tag["attributes"]["name"]["en"]
            in excludedTags
            ]

            params["includedTags[]"] = included_tag_ids
            params["includedTags[]"] = excluded_tag_ids

        response = requests.get(self.base_manga_url,params=params)

        
        response.raise_for_status()
        
        #Returns top 10 most relevant
        #Type (manga/webtoon/etc) tags title --> og and en description year, content rating, demo ["senin,shounen,etc"]
        # Also need to get cover, not provided by regular search endpoint
        manga_data = response.json()
            

        mangas = []
        for manga in manga_data["data"]:
            tags = []
            
            related_data = manga['relationships']
            id = manga["id"]
            if cover:
                #Need to handle no cover
                #Last item in list always cover, should handle lack of cover page or lack of file
                if len(related_data) > 0 and related_data[-1]['type'] == 'cover_art':
                    img_json = requests.get(f"{self.cover_url}{related_data[-1]['id']}").json()
                    fileName = img_json["data"]["attributes"]["fileName"]
                    cover_url = f"{self.cover_image_url}{id}/{fileName}"
            else:
                cover_url = "Not Found"


            for tag in manga["attributes"]["tags"]:
                tags.append(tag["attributes"]["name"]["en"])

            try:
                enTitle = manga["attributes"]["altTitles"][0]["en"]
            except KeyError:
                enTitle = None 

            description = self.language_handler(manga["attributes"]["description"])
            title = self.language_handler(manga["attributes"]["title"])
            
            #May need additional handlers to deal with empty values
            mangas.append({
                "type":manga["type"],
                "title":title,
                "en-title": enTitle,
                "description": description,
                "demo":manga["attributes"]["publicationDemographic"],
                # "status":manga["attributes"]["status"], Can get when fetching individual manga
                "rating":manga["attributes"]["contentRating"],
                "tags":tags,
                "api_id": id,
                "cover_url": cover_url or None
            })
            
        
        # stats_response = requests.get(self.stats_url+manga_data.id)

        # stats_response.raise_for_status()

        # stats_data = stats_response.json()

        return mangas
    def language_handler(self,content):
        try:
            eng_content = content["en"]
        except KeyError:
            if len(content) > 0:
                return content.values()[0]
            else:
                return None 
        else:
            return eng_content
    
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

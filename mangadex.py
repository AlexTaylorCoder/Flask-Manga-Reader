import requests
class Mangadex:
    base_url = "https://api.mangadex.org/manga"
    def __init__(self):
        pass 
    def search(self,params):
        response = requests.get(Mangadex.base_url,
                                params=params)

        response.raise_for_status()

        return response.json() 

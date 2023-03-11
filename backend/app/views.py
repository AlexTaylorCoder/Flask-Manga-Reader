from app import app
from mangadex import Mangadex
from app.scraper import MangakalotScraper, MangaParkScraper
from flask import request

sourceMapping = {
    "mangakakalot": MangakalotScraper(),
    "mangapark": MangaParkScraper(),
    "mangadex": Mangadex()
}

@app.route("/")
def home():
    pass
#Updates
#Updates all chapters that user has and where status is not complete
#Get all user mangas resource links and if not completed search 
@app.route("/update")
def update():
    pass
#History

#Browse searchword = request.args.get('key', '')
@app.route("/search")
def search():
    searchQuery = request.args.get("query")
    sources = request.args.get("sources")
    #Sources should list like one,two,three for multi query 
    results = {}
    for source in sources.split(","):
        targetedSource = sourceMapping[source]
        sourceInfo = targetedSource.search(searchQuery)
        results[source] = sourceInfo

    return results
    # args = request.args
    # data = mangaSearch.search(args)
    # print(data)
    

@app.route("/manga/<id>/details")
def details():
    pass 

@app.route("/manga/<id>/feed")
def feed():
    pass


@app.route("/saved_chapters")
def saved_chapters():
    pass

#Load Stats
@app.route("/profile")
def profile():
    pass

@app.route("/manga",methods=["POST","GET"])
def save_manga():
    pass 

@app.route("/save_chapter")
def save_chapter():
    pass 


@app.route("/auth")
def auth():
    pass

@app.route("/login",methods=["POST"])
def login():
    pass

@app.route("/signup",methods=["POST"])
def signup():
    pass
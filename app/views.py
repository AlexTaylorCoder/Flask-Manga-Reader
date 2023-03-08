from app import app
from mangadex import Mangadex

@app.route("/")
def home():
    pass
#Updates


#History


#Browse searchword = request.args.get('key', '')
@app.route("/search")
def search():
    mangaSearch = Mangadex()
    # args = request.args
    # data = mangaSearch.search(args)
    # print(data)


#Load Stats
def profile():
    pass
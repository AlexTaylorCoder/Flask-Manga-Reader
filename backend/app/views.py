from app import app
from mangadex import Mangadex

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
    mangaSearch = Mangadex()
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
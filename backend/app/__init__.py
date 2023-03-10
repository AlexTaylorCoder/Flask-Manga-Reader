from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

from app import views
from app import models
from app.scraper import MangakalotScraper, MangaParkScraper
from mangadex import Mangadex





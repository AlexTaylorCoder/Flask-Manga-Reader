from flask_sqlalchemy import SQLAlchemy
from app import db 

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(30))
    avatar = db.Column(db.String(200))

    def __repr__(self):
        return '<User %r>' % self.username


# class UserStatistics(db.Model):
#     readtime = db.Column(db.Integer)


author_manga = db.Table('author_manga',
                        db.Column('author_id',db.ForeignKey('author.id')),
                        db.Column('manga_id',db.ForeignKey('manga.id'))
                        )
#SQLITE CANNOT STORE ARRAY FOR CATEGORIES

manga_category = db.Table('manga_category',
                        db.Column('category_id',db.ForeignKey('category.id')),
                        db.Column('maga_id',db.ForeignKey('manga.id')),
                          )

#This will be reference to api not manga itself so there will be multiple references to the same manga
class Manga(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    author = db.Column(db.String(50))
    last_chaper = db.Column(db.Integer)
    last_page = db.Column(db.Integer)
    cover = db.Column(db.String(200))
    description = db.Column(db.String(300))
    views = db.Column(db.Integer)
    saves = db.Column(db.Integer)
    mangastatics = db.relationship("MangaStatistic",uselist=False,back_populates="manga")
    rating = db.Column(db.Integer)


class MangaStatistic(db.Model):
    readtime = db.Column(db.Integer)
    id = db.Column(db.Integer, primary_key=True)

    #  = relationship("Parent", back_populates="child") 


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(50))
    mangas = db.relationship('Manga',secondary=author_manga,backref="authors") #This allows manga.authors as well as authors.manga

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20),unique=True)
    mangas = db.relationship('Manga',secondary=manga_category,backref="categories") # Needed b/c manga can have multiple categories and vice-verca



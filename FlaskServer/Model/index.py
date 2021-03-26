from peewee import *

db = SqliteDatabase('news_articles.db')

class BaseModel(Model):
    class Meta:
        database = db

class Articles(BaseModel):
    title = CharField(unique=True)
    article = CharField()
    link = CharField()
    date = CharField()
    class Meta:
        db_table = 'Articles'

db.connect()


import pymongo

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db=client['practoaudit']

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()

    print "DB created"
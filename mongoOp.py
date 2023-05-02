import pymongo

def connect(collectionName):
    client = pymongo.MongoClient("mongodb+srv://NIXBLACK:nixblack11@cluster0.tk5azpj.mongodb.net/test")
    Database = client["bank"]
    if collectionName=='users':
        users = ['users']
    elif collectionName=='publicAnnouncements':
        publicAnnouncements = ['publicAnnouncements']
    
def caller(tag):
import pymongo

def connect(collectionName):
    client = pymongo.MongoClient("mongodb+srv://NIXBLACK:nixblack11@cluster0.tk5azpj.mongodb.net/test")
    Database = client["bank"]
    if collectionName=='users':
        users = ['users']
        return users
    elif collectionName=='publicAnnouncements':
        publicAnnouncements = ['publicAnnouncements']
        return publicAnnouncements
    
def caller(tag):
    if(tag=="login"):
        users = connect("users")
        
    elif(tag=="balance_enquiry"):
        users = connect("users")
    elif(tag=="latest_updates"):
        public = connect("publicAnnouncements")
    elif(tag=="interest_rates"):
        public = connect("publicAnnouncements")
        
import pymongo
import os
from dotenv import load_dotenv

# Load variables from .env into the environment
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

#add more for documents
#calender academic calender

def connect(collectionName):
    client = pymongo.MongoClient(DATABASE_URL)
    Database = client["BankBot"]
    collection = Database[collectionName]
    return collection

def userExists(id):
    resp: bool = False
    users = connect("Users")

    exists = users.find_one({"id": id})
    if exists:
        resp = True
    else:
        resp = False
    return resp
    
def ifNewCred(id, credentials):
    users = connect("Users")
    [username, password] = credentials.split(" ")
    alreadyLogin = users.find_one({"id": id})
    if users["username"]!=username or users["password"]!=password:
        users.update_one({"id": id}, {"$set": {"id": -1}})
        return True
    return False    

def login(id, credentials):
    resp: bool = False
    users = connect("Users")

    [username, password] = credentials.split(" ")

    exists = users.find_one({"username": username, "password": password})
    if exists:
        if exists["id"] == -1:
            users.update_one({"username": username, "password": password}, {"$set": {"id": id}})
            resp = True
        else:
            resp = False
    else:
        resp = False
    return resp

def logout(id):
    resp: bool = False
    users = connect("Users")

    result = users.update_one({"id": id}, {"$set": {"id": id}})

    if result.matched_count > 0:
        resp = True
    else:
        resp = False
    return resp

def balance(id):
    users = connect("Users")
    user = users.find_one({"id": id})
    return user["balance"]

def balanceGraph(id):
    users = connect("Users")
    user = users.find_one({"id": id})
    return user["balanceValues"]

def updates():
    public = connect("Public")
    publicData = public.find_one({})
    return publicData["latestUpdates"]

def interest():
    public = connect("Public")
    publicData = public.find_one({})
    return publicData["interestRates"]
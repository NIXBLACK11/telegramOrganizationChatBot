import pymongo
import os
from dotenv import load_dotenv

# Load variables from .env into the environment
load_dotenv()

DATABASE_URL = os.getenv("mongodb+srv://NIXBLACK:nixblack11@cluster0.tk5azpj.mongodb.net/")

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
    
def login(id, credentials):
    resp: bool = False
    users = connect("Users")
    
    try:
        [username, password] = credentials.split(" ")
    except ValueError:
        resp = False

    exists = users.find_one({"username": username, "password": password})
    if exists:
        if exists["id"] == -1:
            users.update_one({"username": username, "password": password}, {"id": id})
            resp = True
        else if exists["id"] == id:
            resp = True
        else:
            resp = False
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
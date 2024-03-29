import pymongo
import os
from dotenv import load_dotenv

# Load variables from .env into the environment
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
def connect(collectionName):
    client = pymongo.MongoClient(DATABASE_URL)
    Database = client["bank"]
    if collectionName=='users':
        users = Database['users']
        return users
    elif collectionName=='publicAnnouncements':
        publicAnnouncements = Database['publicAnnouncements']
        return publicAnnouncements
    
def login(users, tag):
    pass
    x = tag.split(" ")
    one = users.find_one({"name" : x[0], "password" : x[1]}, {"_id":1})
    # print(one)
    if one:
        return one["_id"]
    return "-1"
    
def balance(users, id):
    one = users.find_one({"_id":id})
    return one["accountBalance"]

def balanceGraph(users, id):
    one = users.find_one({"_id":id})
    return one["balanceValues"]

def updates(public):
    one = public.find_one({"callerId":321}, {'latestUpdates':1})
    return one["latestUpdates"]

def interest(public):
    one = public.find_one({"callerId":321}, {'interestRates':1})
    return one["interestRates"]
    
def caller(tag, id):
    if(id =="do"):
        users = connect("users")
        return login(users, tag)
    elif(tag=="balance_enquiry"):
        users = connect("users")
        return balance(users, id)
    elif(tag=="latest_updates"):
        public = connect("publicAnnouncements")
        return updates(public)
    elif(tag=="interest_rates"):
        public = connect("publicAnnouncements")
        return interest(public)
    elif(tag=="balance_graph"):
        users = connect("users")
        values = balanceGraph(users, id)
        return "graph "+values

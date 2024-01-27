import pymongo
import os
from dotenv import load_dotenv

# Load variables from .env into the environment
load_dotenv()

DATABASE_URL = os.getenv("mongodb+srv://NIXBLACK:nixblack11@cluster0.tk5azpj.mongodb.net/")

def connect():
    client = pymongo.MongoClient(DATABASE_URL)
    Database = client["BankBot"]
    users = Database['Users']
    return users

def userExists(id):
    users = connect()
    exists = users.find_one({"id:": id})
    if exists:
        return true
    else 
        return false
    

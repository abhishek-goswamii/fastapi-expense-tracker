import certifi
import pymongo
from dotenv import dotenv_values

config = dotenv_values(".env")
url = config["MONGO_URI"]


client = pymongo.MongoClient(url)
expensetracker_db = client["expensetracker"]
users_collection = expensetracker_db["users"]


try:
    expensetracker_db.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


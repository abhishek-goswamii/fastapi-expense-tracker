import pymongo
from dotenv import dotenv_values

config = dotenv_values(".env")
url = config["MONGO_URI"]

# client
client = pymongo.MongoClient(url)

# database name
expensetracker_db = client["expensetracker"]

# collections references
users_collection = expensetracker_db["users"]
expenses_collection = expensetracker_db["expenses"]
balances_collection = expensetracker_db["balances"]

# testing connection
try:
    expensetracker_db.command('ping')
    print("successfully connected to MongoDB!")
except Exception as e:
    print(e)
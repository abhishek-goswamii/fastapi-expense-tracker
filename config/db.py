from pymongo import MongoClient
from dotenv import dotenv_values

config = dotenv_values(".env")

print("printing url"+config["MONGO_URI"])

def connect_to_mongodb():
    mongodb_client = MongoClient(config["MONGO_URI"])
    database = mongodb_client[config["DB_NAME"]]
    print("Connected to the MongoDB database!")
    return mongodb_client, database

def close_mongodb_connection(mongodb_client):
    mongodb_client.close()
    print("Closed MongoDB connection.")

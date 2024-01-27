from pymongo import MongoClient
from dotenv import dotenv_values

config = dotenv_values(".env")

mongodb_client = MongoClient(config["MONGO_URI"])

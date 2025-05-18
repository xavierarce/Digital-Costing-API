from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://xavierarce54321:T6oTYGp2A5F7UPPm@digitalcosting.ftcfrbp.mongodb.net/?retryWrites=true&w=majority&appName=DIGITALCOSTING"

client = MongoClient(uri, server_api=ServerApi('1'))
db = client.digitalcosting  # or your DB name

try:
    # The ping command is cheap and does not require auth.
        client.admin.command('ping')
        print("✅ Successfully connected to MongoDB!")
except Exception as e:
        print("❌ Server not available:", e)
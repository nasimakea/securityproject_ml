import os
from dotenv import load_dotenv
import pymongo

load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")
print("Mongo URL:", MONGO_DB_URL)

client = pymongo.MongoClient(MONGO_DB_URL)

print("\nDatabases:")
print(client.list_database_names())

db = client["network_security"]  # change ONLY if your constant is different

print("\nCollections:")
print(db.list_collection_names())

collection = db["phishing_data"]  # change ONLY if your constant is different

print("\nDocument count:", collection.count_documents({}))
print("Sample document:", collection.find_one())

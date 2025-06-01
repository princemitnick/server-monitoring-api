import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv


#load_dotenv()

#MONGO_URI = os.getenv("MONGO_UR")
#MONGO_DB = os.getenv("MONGO_DB", "monitoring")
#MONGO_COLLECTION = os.getenv("MONGO_COLLECTION", "metrics")

#client = AsyncIOMotorClient(MONGO_URI)
#db = client[MONGO_DB]
#metrics_collection = db[MONGO_COLLECTION]

MONGO_URL = "mongodb://localhost:27017"
client = AsyncIOMotorClient(MONGO_URL)
db = client["monitoring"]
metrics_collection = db["metrics"]
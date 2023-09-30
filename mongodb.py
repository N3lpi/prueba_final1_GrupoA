from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env.

user = os.getenv('MONGO_USER')
password = os.getenv('MONGO_PASSWORD')

uri = f"mongodb+srv://{user}:{password}@cluster0.fo30jxs.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

client.get_database('final2').get_collection('repositorio').insert_one(document={"indicativo": "5530E", "n_tor_n": "30", "q_max_n": "29"})
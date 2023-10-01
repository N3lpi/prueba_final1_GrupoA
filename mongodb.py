from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import certifi
import os


load_dotenv()  # take environment variables from .env.

user = os.getenv('MONGO_USER')
password = os.getenv('MONGO_PASSWORD')

uri = f"mongodb+srv://{user}:{password}@cluster0.fo30jxs.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server


# Send a ping to confirm a successful connection
ca = certifi.where()

def dbConnection():
    try:
        client = MongoClient(uri, tlsCAFile=ca)
        db = client["final2"]
    except ConnectionError:
        print('Error con la bdd')
    return db


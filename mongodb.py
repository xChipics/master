from pymongo import MongoClient
from dotenv import load_dotenv
from pymongo.server_api import ServerApi

import os
load_dotenv()

user = os.getenv('MONGO_USER')
pas = os.getenv('MONGO_pass')


uri = "mongodb+srv://"+user+":"+pas+"@cluster0.2dw56pq.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
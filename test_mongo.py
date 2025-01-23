'''
This is just to check or do the connection to the mongodb database

'''


from pymongo.mongo_client import MongoClient
from collections.abc import MutableMapping  # Correct for Python 3.3+

uri = "mongodb+srv://buzzideas7:buzz12345@cluster0.qle05.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
from fastapi import FastAPI
import pymongo
from models import RequestData
import os

mongo_host = os.environ.get("MONGO_HOST", "mongodb-service")
mongo_port = int(os.environ.get("MONGO_PORT", 27017))
mongo_username = os.environ.get("MONGO_USERNAME","your_username")
mongo_password = os.environ.get("MONGO_PASSWORD","your_password")

app = FastAPI()

@app.post("/send_data/")
async def send_data(requestData: RequestData):
    client = pymongo.MongoClient(
        host=mongo_host,
        port=mongo_port,
        username=mongo_username,
        password=mongo_password,
        authSource="admin",  # The authentication database
    )
    mydb = client["TestDB_2"]
    mycol = mydb["Users"]

    document = {
        "name": f"{requestData.name}",
        "age": f"{requestData.age}",
        "location": f"{requestData.location}"
    }
    mycol.insert_one(document)

    return {"message": f"Hello {requestData.name}"}

@app.get("/hello_message/")
async def get_data():
    return {"message": "Hello World"}

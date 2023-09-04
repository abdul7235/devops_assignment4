from fastapi import FastAPI
import pymongo
from models import RequestData

app = FastAPI()

@app.post("/send_data/")
async def send_data(requestData:RequestData):
    client = pymongo.MongoClient("mongodb://db:27017")
    mydb = client["TestDB_2"]
    mycol = mydb["Users"]
    
    document = {"name": f"{requestData.name}", "age": f"{requestData.age}", "location": f"{requestData.location}"}
    mycol.insert_one(document)
    
    return {"message": f"Hello {requestData.name}"}

@app.get("/hello_message/")
async def get_data():
    return {"message": "Hello World"}
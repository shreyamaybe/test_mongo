import pymongo

client = pymongo.MongoClient("mongodb+srv://shreyabag_:AtPU3vNYQ3BWEPk@cluster0.0dxj5.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d={
    "name": "shreya",
    "email" : "bagshreya25@gmail.com",
    "surname": "bag"
}
db1=client['mongotest']
coll=db1['test']
coll.insert_one(d)
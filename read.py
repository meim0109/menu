import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

aond  = input("請輸入您實施減肥菜單的天數：")
cond  = input("請輸入您減肥菜單需要的時段：")

db = firestore.client()
collection_ref = db.collection("減肥菜單")
docs = collection_ref.get()
result = ""
for doc in docs:
    dict = doc.to_dict()
    if aond in dict["date"]  
        result += "您實施減肥菜單的天數："+ dict["date"] +"您今天選擇的時段是:"+ dict["time"] + "主食:"+ dict["Staple Food"] 
        result += "副餐:" + dict["Nonstaple Food"]+ "飲品:" + dict["beverage"] + "水果or點心:"+ dict["fruit"]+ "<br>"

    if cond in dict["time"]  	
        result += "您實施減肥菜單的天數："+ dict["date"] +"您今天選擇的時段是:"+ dict["time"] + "主食:"+ dict["Staple Food"] 
        result += "副餐:" + dict["Nonstaple Food"]+ "飲品:" + dict["beverage"] + "水果or點心:"+ dict["fruit"]+ "<br>"
print(result)

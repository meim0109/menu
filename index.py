import requests
from bs4 import BeautifulSoup


#from flask import Flask, render_template, request, abort, jsonify
#from datetime import datetime, timezone, timedelta

#import firebase_admin
#from firebase_admin import credentials, firestore
#cred = credentials.Certificate("serviceAccountKey.json")
#firebase_admin.initialize_app(cred)
#db = firestore.client()
#app = Flask(__name__)

from flask import Flask, render_template, request,make_response, jsonify
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
app = Flask(__name__)

@app.route("/")
def index():
    homepage = "<h1>黃靜梅Python讀取Firestore</h1>"
    homepage += "<a href=/account>網頁表單輸入實例</a><br><br>"
    homepage += "<a href=/search>瘦身菜單</a><br><br>"
    return homepage

@app.route("/account", methods=["GET", "POST"])
def account():
    if request.method == "POST":
        user = request.form["user"]
        pwd = request.form["pwd"]
        result = "您輸入的帳號是：" + user + "; 密碼為：" + pwd 
        return result
    else:
        return render_template("account.html")

@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        aond = request.form["date"]
        result = "請輸入您實施減肥菜單的天數：" + aond

    if request.method == "POST":
        cond = request.form["time"]
        result = "請輸入您減肥菜單需要的時段：" + cond

        db = firestore.client()
        collection_ref = db.collection("減肥菜單")
        docs = collection_ref.get()
        result = ""
        for doc in docs:
            dict = doc.to_dict()
            if aond in dict["date"] and cond in dict["time"]:
                result += "您實施減肥菜單的天數："+ dict["date"] +"您今天選擇的時段是:"+ dict["time"] + "主食:"+ dict["Staple Food"] 
                result += "副餐:" + dict["Nonstaple Food"]+ "飲品:" + dict["beverage"] + "水果or點心:"+ dict["fruit"]+ "<br>"
            
        if result == "":
            result = "抱歉，查無相關條件的瘦身菜單"

        return result
           
    else:
        return render_template("search.html")

@app.route("/webhook", methods=["POST"])
def webhook():
    # build a request object
    req = request.get_json(force=True)
    # fetch queryResult from json
    action =  req.get("queryResult").get("action")
    #msg =  req.get("queryResult").get("queryText")
    #info = "動作：" + action + "； 查詢內容：" + msg

    if (action == "menuChoice"):
        menu =  req.get("queryResult").get("parameters").get("menu")
        #info = "您今天選擇的時段是:" + menu
        if (menu == "早餐"):
            menu = "早餐)"
        elif (menu == "午餐"):
            menu = "午餐"
        elif (menu == "晚餐"):
            menu = "晚餐"
        info = "您要查詢減肥菜單的：" + menu + "，相關時段：\n"

        collection_ref = db.collection("減肥菜單")
        docs = collection_ref.get()
        result = ""
        for doc in docs:
            dict = doc.to_dict()
            if aond in dict["date"] and cond in dict["time"]:
                result += "您實施減肥菜單的天數："+ dict["date"] +"您今天選擇的時段是:"+ dict["time"] + "主食:"+ dict["Staple Food"] 
                result += "副餐:" + dict["Nonstaple Food"]+ "飲品:" + dict["beverage"] + "水果or點心:"+ dict["fruit"]+ "<br>"

        info += result

    elif (action == "menuDetail"):  
        cond =  req.get("queryResult").get("parameters").get("FilmQ")
        keyword =  req.get("queryResult").get("parameters").get("any")
        info = "您要查詢減肥菜單的" + cond + "，"+"關鍵字是：" + keyword + "\n\n"

        if (cond == "時段"):
            collection_ref = db.collection("減肥菜單")
            docs = collection_ref.get()
            found = False
            for doc in docs:
                dict = doc.to_dict()
                if keyword in dict["time"]:
                    found = True 
                    info += "時段：" + dict["time"] + "\n"
                    info += "天數：" + dict["date"] + "\n"
                    info += "主食：" + dict["Staple Food"] + "\n"
                    info += "配餐：" + dict["Nonstaple Food"] + "\n"
                    info += "飲品：" + dict["beverage"] + "\n" 
                    info += "水果：" + dict["fruit"] + "\n\n"

                if not found:
                    info += "很抱歉，目前無符合這個關鍵字的相關資訊喔"
            return make_response(jsonify({"fulfillmentText": info}))

        elif (cond == "天數"):
            collection_ref = db.collection("減肥菜單")
            docs = collection_ref.get()
            found = False
            for doc in docs:
                dict = doc.to_dict()
                if keyword in dict["date"]:
                    found = True 
                    info += "時段：" + dict["time"] + "\n"
                    info += "天數：" + dict["date"] + "\n"
                    info += "主食：" + dict["Staple Food"] + "\n"
                    info += "配餐：" + dict["Nonstaple Food"] + "\n"
                    info += "飲品：" + dict["beverage"] + "\n" 
                    info += "水果：" + dict["fruit"] + "\n\n"

                if not found:
                    info += "很抱歉，目前無符合這個關鍵字的相關資訊喔"


    return make_response(jsonify({"fulfillmentText": info}))

if __name__ == "__main__":
    app.run()
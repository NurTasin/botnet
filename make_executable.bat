@echo off
pyinstaller -F --distpath ./bin -n windowsdefender bot.pyw
rm -rf ./build *.spec
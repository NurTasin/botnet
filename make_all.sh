pyinstaller -F --distpath ./release/production/ -i ./asset/network.ico -n windowsdefender bot.pyw
cp bot.pyw bot.py
pyinstaller -F --distpath ./release/debug -i ./asset/network.ico -n windowsdefender bot.py
rm -rf ./build *.spec bot.py
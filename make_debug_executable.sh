cp bot.pyw bot.py
pyinstaller -F --distpath ./release/debug/ -i ./asset/network.ico bot.py -n networkmanager
rm -rf ./build *.spec bot.py
pyinstaller -F --distpath ./release/production/ -i ./asset/network.ico bot.pyw -n networkmanager
rm -rf ./build *.spec
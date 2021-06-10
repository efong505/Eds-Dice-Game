cls
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py 
pip install pygame
pip install pillow
pip install pyinstaller
pyinstaller --windowed --icon=dice.ico FongFinalRevised.py
copy splash.png .\dist\FongFinalRevised\
copy game-over2.jpg .\dist\FongFinalRevised\
copy youwon.jpg .\dist\FongFinalRevised\
copy dice.ico .\dist\FongFinalRevised\
copy ooh.mp3 .\dist\FongFinalRevised\
copy applause.wav .\dist\FongFinalRevised\
copy snakeeyesroll.wav .\dist\FongFinalRevised\


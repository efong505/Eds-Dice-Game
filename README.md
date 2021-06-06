# Ed's Dice Game
 A game that plays against the computer rolling 5 times. Winner is the one that scores the highest points. 

## Prerequisits
This program has been written with python 3.9.5. The gui is based on the TKinter module. 
If you don't have pygame, you will need to install it. 
PIL is also required 
I've included a batch file pyinstaller.bat It also creates an executable file for a Windows user. **See the Create Executable section below.**

## To Create Executable Program on Windows
 I'm using pyinstaller to create an executable file for my python program. I've included a batch file, pyinstaller.bat that installs everything that you would need to have the program work on a Windows computer.
 You can either open the batch file in the command line or double click the file directly. 
 
 1. Open the folder that contains all of the project files in a command line window. 
 2. Open the batch file by typing `pyinsall.bat` and hitting enter.
 3. The batch file will install all of the modules needed for the program. At the end of the needed installed files and modules, pyinstaller will create folders with files in them. The folder that will contain the exe file will be in `dist`. 
 4. Open the `dist` folder. 
 5. In the `dist` folder, open the `FongFinalRevised` folder. 
 6. In the the `FongFinalRevised` folder, look for the execution file. `FongFinalRevised.exe`. This will launch the program if all went well. 
 
 You can also use these commands to install everthing in the batch file.
 ````batch
 curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py 
pip install pygame
pip install pillow
pip install pyinstaller
pyinstaller --windowed --icon=dice.ico FongFinalRevised.py
 ````
### Enjoy!!!

######################################################################################
## FongFinal                                                                         ##
## Programmer: Edward Fong                                                           ##
## Email: efong@cnm.edu                                                              ##
## Purpose: Final - A GUI based game where the user plays against the computer.      ##
##   Each roll is followed by the computers roll. The one that rolls the highest     ##
##   score wins the round. 5 rounds are played and the one that scores the highest   ##
##   points after round 5 wins the game.                                             ##
#######################################################################################

from PIL import ImageTk,Image
import tkinter as tk
import random
import pygame

class DiceGame():
    def __init__(self):
        'Initilizer(constructor) Sets up the window, canvas, window sizes and centers the startup in the center of the screen. '

        # list, dictionary, and variables instantiation
        self.dice = []
        self.d = {}
        self.userTally = 0
        self.computerTally = 0
        self.bttn_clicks = 0
        self.i = ''

        # Create tk object
        self.t = tk.Tk()
        # Set Title
        self.t.title('FongFinal - Roll The Dice Game')
        # Window Width and height 
        self.window_width = 725
        self.window_height = 725
        # Get Screen dimensions
        self.screen_width = self.t.winfo_screenwidth()
        self.screen_height = self.t.winfo_screenheight()
        # Find Center Point of screen
        self.center_x = int(self.screen_width / 2 - self.window_width / 2)
        self.center_y = int(self.screen_height / 2 - self.window_height / 2)
        # geometry
        self.t.geometry(f'{self.window_width}x{self.window_height}+{self.center_x}+{self.center_y}')
        # Set icon
        self.t.iconbitmap(r'dice.ico')
        # Set and Pack
        self.c = tk.Canvas(self.t, width=725, height=725)
        self.c.pack()

        # Setup buttons and labels - Call buttons_labels function
        self.buttons_labels()

    # Roll Dice Action
    def roll_dice(self):
        'The roll_dice method is the action handler for the roll button. '
        # Dice objects
        self.dice_objects()
        # Check and display who wins round
        self.roundCheck()
        # Play and Win/Lose Labels
        self.labels()
        # Check who wins game, display if user wins or
        # loses with graphics and play winning or losing sound
        self.gameWinLose()

    # Checks to see who wins round and displays win or loss
    def roundCheck(self):
        'Check to see who wins the round displays if player won or lost the round'
        if(self.userDiceString > self.computerDiceString):
            self.displayWinLoseLabel.configure(text="YOU WIN!!!", fg='green')
            self.userTally += 1
        else:
            self.displayWinLoseLabel.configure(text="YOU LOST!", fg='red')
            self.computerTally += 1

    # Checks to see who wins game, display if user wins or loses
    # with graphics and play winning or losing sound
    def gameWinLose(self):
        'Checks who wins game, displays if user wins or loses and displays graphics and sounds accordlingly'
        if (self.bttn_clicks == 5 and self.computerTally > self.userTally):
            self.rollButton.configure(state='disabled')

            # Hide labels and dice
            self.displayWinLoseLabel.configure(text="") # hide win/lose label
            self.computerLabel.configure(text="") # hide computer label
            self.computerDiceObjects.configure(text="") # hide computer dice
            # Lost label
            self.img = ImageTk.PhotoImage(Image.open('C:\\Users\\Ed\\Documents\\School\\CNM\\Summer 2021\\Python\\Programs\\Final\\dicerollgame-master\\exe\\game-over2.jpg').resize((755,200)))
            self.winLoseLabel = tk.Label(self.t, image=self.img)
            self.i = self.c.create_window(350, 520, window=self.winLoseLabel)
            # Lose Sound
            pygame.mixer.init()
            pygame.mixer.music.load('C:\\Users\\Ed\\Documents\\School\\CNM\\Summer 2021\\Python\\Programs\\Final\\dicerollgame-master\\exe\\ooh.mp3')
            pygame.mixer.music.play()


        elif (self.bttn_clicks == 5 and self.userTally > self.computerTally):
            self.rollButton.configure(state='disabled')

            # Hide labels and dice
            self.displayWinLoseLabel.configure(text="") # hide win/lose label
            self.computerLabel.configure(text="") # hide computer label
            self.computerDiceObjects.configure(text="") # hide computer dice
            # Win Label
            self.img = ImageTk.PhotoImage(Image.open("C:\\Users\\Ed\\Documents\\School\\CNM\\Summer 2021\\Python\\Programs\\Final\\dicerollgame-master\\exe\\youwon.jpg").resize((755,200)))
            self.winLoseLabel = tk.Label(self.t, image=self.img)
            self.i = self.c.create_window(350, 520, window=self.winLoseLabel)

            #Win Sound
            pygame.mixer.init()
            pygame.mixer.music.load('C:\\Users\\Ed\\Documents\\School\\CNM\\Summer 2021\\Python\\Programs\\Final\\dicerollgame-master\\exe\\applause.wav')
            pygame.mixer.music.play()

    # Dice Objects
    def dice_objects(self):

        # Dice list
        self.dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
        # Dice dictionary
        self.d = {'\u2680':1, '\u2681':2, '\u2682':3, '\u2683':4, '\u2684':5, '\u2685':6}

        #user's roll
        self.userDice1 = random.choice(self.dice)
        self.userDice2 = random.choice(self.dice)

        #computer's roll
        self.computerDice1 = random.choice(self.dice)
        self.computerDice2 = random.choice(self.dice)

        # User Dice Pieces
        self.diceObjects.configure(text=f'{self.userDice1} {self.userDice2}')
        self.c.create_window(380, 250, window=self.diceObjects)

        # Computer Dice Pieces
        self.computerDiceObjects.configure(text=f'{self.computerDice1} {self.computerDice2}')
        self.c.create_window(380, 380, window=self.computerDiceObjects)

        # User Label
        self.userLabel.configure(text="Your Dice")

        # Computer Label
        self.computerLabel.configure(text="Computer's Dice")
        # User Combined Dice Score
        self.userDiceString = self.d[self.userDice1]+self.d[self.userDice2]
        # Computer Combined Dice Score
        self.computerDiceString = self.d[self.computerDice1]+self.d[self.computerDice2]

    # Labels
    def labels(self):
        'Labels for win and game plays along with button clicks counter(increment)'
        self.numberRolledLabel.configure(text="You rolled  "+str(self.userDiceString))
        self.computerNumberRolledLabel.configure(text="Computer rolled  "+str(self.computerDiceString))
        self.bttn_clicks += 1
        self.timesRolledLabel['text'] = "Number of Rolls: " + str(self.bttn_clicks)

    # Restart Action
    def restart(self):
        'The restart method is the action handler to the Start/restart button'
        self.bttn_clicks= 0
        self.userTally = 0
        self.computerTally = 0
        self.timesRolledLabel.configure(text="")
        self.numberRolledLabel.configure(text="No rolls yet", width=15)
        self.computerNumberRolledLabel.configure(text="No rolls yet",width=15)
        self.displayWinLoseLabel.configure(text="")
        pygame.mixer.init()
        pygame.mixer.music.stop()
        if self.i:
            self.c.delete(self.i)
        self.rollButton.configure(state='normal')

    def buttons_labels(self):
        'The buttons_lables method creates all of the buttons and lables in one place'
        # Start with Dice not on screen
        self.diceObjects = tk.Label(self.t, text='asdf', font=('Times', 120),fg='green')
        # Start with Computer Dice not on screen
        self.computerDiceObjects = tk.Label(self.t, text='asdf', font=('Times', 75),fg='black')
        # Start Button
        self.startButton = tk.Button(self.t, text='Start/Replay', font=('times', 20,"bold"),background="blue",foreground='white',height=1, width=10, command=self.restart)
        self.c.create_window(275, 78, window=self.startButton)
        # Roll Button
        self.rollButton = tk.Button(self.t, text='Roll the dice', font=('times', 20,"bold"),state="disabled",background="brown",foreground='yellow',height=1, width=10, command=self.roll_dice)
        self.c.create_window(470, 78, window=self.rollButton)
        # Times Rolled Label
        self.timesRolledLabel = tk.Label(self.t, text='', font=('Times',20,'bold'),fg='brown')
        self.c.create_window(180, 650, window=self.timesRolledLabel)
        # Game Win or Lose Label
        self. displayWinLoseLabel = tk.Label(self.t, text='', font=('Times',50, 'bold'), fg='yellow')
        self.c.create_window(375, 520, window=self.displayWinLoseLabel)
        # User Number Rolled
        self.numberRolledLabel = tk.Label(self.t, text='NO ROLLS YET', font=('Times',20,'bold'),bg='purple',fg='yellow', width=13)
        self.c.create_window(580, 650, window=self.numberRolledLabel)
        # Computer Number Rolled
        self.computerNumberRolledLabel = tk.Label(self.t, text='NO ROLLS YET', font=('Times',20,'bold'),bg='yellow', fg='purple', width=13)
        self.c.create_window(580, 690, window=self.computerNumberRolledLabel)
        # Start Splash Image
        self.splash = ImageTk.PhotoImage(Image.open("C:\\Users\\Ed\\Documents\\School\\CNM\\Summer 2021\\Python\\Programs\\Final\\dicerollgame-master\\exe\\splash.png").resize((725, 600)))
        self.splashLabel = tk.Label(self.t, image=self.splash)
        self.i = self.c.create_window(362, 425, window=self.splashLabel)
        # User Label
        self.userLabel = tk.Label(self.t, text='', font=('Times', 25, 'bold'), fg="green")
        self.c.create_window(390,175, window=self.userLabel)
        # Computer Label
        self.computerLabel = tk.Label(self.t, text='', font=('Times', 15, 'bold'), fg="black")
        self.c.create_window(383,330, window=self.computerLabel)
        # Rules Label
        self.rulesLabel = tk.Label(self.t, text='Game rule: The player wins if he/she scores the most points within 5 rolls against the computer.', font=('Times',13,'bold'),fg='yellow',bg="black")
        self.c.create_window(363, 20, window=self.rulesLabel)

# Create App object
app = DiceGame()
# Main Loop
app.t.mainloop()


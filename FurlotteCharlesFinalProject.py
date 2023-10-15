#import tkinter for gui
import tkinter as tk
#import ctypes for changing top of window color
import ctypes as ct
#import random module for dice
import random

#creates a dark title bar(not my code https://stackoverflow.com/questions/17251016/python-tkinter-how-to-change-the-windows-border-color)
def dark_title_bar(window):#I did not right the code in this function
    """
    MORE INFO:
    https://learn.microsoft.com/en-us/windows/win32/api/dwmapi/ne-dwmapi-dwmwindowattribute
    """
    window.update()
    set_window_attribute = ct.windll.dwmapi.DwmSetWindowAttribute
    get_parent = ct.windll.user32.GetParent
    hwnd = get_parent(window.winfo_id())    
    value = 2
    value = ct.c_int(value)
    set_window_attribute(hwnd, 20, ct.byref(value), 4)

#define main class
class main:
    #write initialization code
    def __init__(self):
        #create main window
        self.window = tk.Tk()
        #creates the second window
        self.window2 = tk.Tk()
        #calls the function to make top bar of application dark
        dark_title_bar(self.window)
        #changes the top bar of {self.window2} to be dark
        dark_title_bar(self.window2)
        #changes the look of the application to a dark theme
        self.changeLooks(self.window)
        #changes the look of {self.window2} to a dark theme
        self.changeLooks(self.window2)
        #creates buttons and entry field
        self.createInputs()
        #places buttons and entry field
        self.placeInputs()
        #create the images and place them in the bottom left and the bottom right
        self.createAndPlaceImages()

    def createAndPlaceImages(self):
        #open the images
        self.tempImage1 = tk.PhotoImage(file = 'DiceImageOne.png')
        self.tempImage2 = tk.PhotoImage(file = 'DiceImageTwo.png')
        #create image label objects
        self.image1 = tk.Label(self.window, image = self.tempImage1, borderwidth = 0, text = 'Picture of Dice')
        self.image2 = tk.Label(self.window, image = self.tempImage2, borderwidth = 0, text = 'Picture of Dice')
        #place the images in the grids
        self.image1.grid(row = 6, column = 1)
        self.image2.grid(row = 6, column = 4)

    #rolls the dice
    def rollDice(self, size):
        return  random.randint(1, size)
    #rolls the dice at advantage
    def rollDiceAdv(self, size):
        #stores both rolls of the dice
        self.tempDiceNum1 = random.randint(1, size)
        self.tempDiceNum2 = random.randint(1, size)
        #finds the biggest rolls of the dice and returns it
        if self.tempDiceNum1 >= self.tempDiceNum2:
            return self.tempDiceNum1
        else:
            return self.tempDiceNum2
    #rolls the dice at disadvantage
    def rollDiceDisAdv(self, size):
        #stores both rolls of the dice
        self.tempDiceNum1 = random.randint(1, size)
        self.tempDiceNum2 = random.randint(1, size)
        #finds the smallest rolls of the dice and returns it
        if self.tempDiceNum1 <= self.tempDiceNum2:
            return self.tempDiceNum1
        else:
            return self.tempDiceNum2

    #processes input string and does the calculations of dice rolling and then .pack() the info to a second window
    def calculations(self, input):
        #gets the length of the {input}
        self.inputLength = len(input)
        #initialize a temp num for looping use later
        self.tempNum = 0
        #initialize where the info from the string will be stored
        self.timesToRoll = ''
        self.whatToRoll = ''
        self.whatToAdd = ''
        self.numberToAdd = ''
        self.finalNumber = 0
        #initialize both {self.Adv} and {self.DisAdv} to false
        self.Adv = False
        self.DisAdv = False
        #gets the number of times to roll
        if input[self.tempNum] == 'A':
            self.tempNum += 4
            self.Adv = True
        elif input[self.tempNum] == 'D':
            self.tempNum += 7
            self.DisAdv = True
        while input[self.tempNum] != 'D':
            self.timesToRoll += input[self.tempNum]
            self.tempNum += 1
        #skips the 'D" from being inputted from the data
        self.tempNum += 1
        #get what sort of dice needs to be rolled
        while self.tempNum < self.inputLength and input[self.tempNum] != '+' and input[self.tempNum] != '-':
            self.whatToRoll += input[self.tempNum]
            self.tempNum += 1
        #gets weather stuff should be added, subtracted or nothing from the results
        if self.tempNum < self.inputLength:
            self.whatToAdd = input[self.tempNum]
            self.tempNum += 1
        #gets what to add or subtract if there there is anything to add or subtract
        while self.tempNum < self.inputLength:
            self.numberToAdd += input[self.tempNum]
            self.tempNum += 1
        #resets {self.temNum}
        self.tempNum = 0
        #does the dice rolling and calculations
        #if {Adv.}
        if self.Adv == True:
            while self.tempNum < int(self.timesToRoll):
                #keep track of how many times things have been rolled
                self.tempNum += 1
                #rolls the dice and adds it to the total
                self.finalNumber += self.rollDiceAdv(int(self.whatToRoll))
        #elif {DisAdv.}
        elif self.DisAdv == True:
            while self.tempNum < int(self.timesToRoll):
                #keeps track of how many times things have been rolled
                self.tempNum += 1
                #rolls the dice and adds it to the total
                self.finalNumber += self.rollDiceDisAdv(int(self.whatToRoll))
        #else
        else:
            while self.tempNum < int(self.timesToRoll):
                #keep track of how many times things have been rolled
                self.tempNum += 1
                #rolls the dice and adds it to the total
                self.finalNumber += self.rollDice(int(self.whatToRoll))
        #displays the dice rolls
        if self.whatToAdd == '+':
            #adds {self.numberToAdd}
            self.finalNumber += int(self.numberToAdd)
            #displays final result
            self.final = tk.Label(self.window2, text = (self.timesToRoll, 'D', self.whatToRoll,  '+', self.numberToAdd, '=', self.finalNumber))
            self.final.pack()
        elif self.whatToAdd == '-':
            #subtracts {self.numberToAdd}
            self.finalNumber -= int(self.numberToAdd)
            #displays final result
            self.final = tk.Label(self.window2, text = (self.timesToRoll, 'D', self.whatToRoll,  '-', self.numberToAdd, '=', self.finalNumber))
            self.final.pack()
        else:
            self.final = tk.Label(self.window2, text = (self.timesToRoll, 'D', self.whatToRoll, '=', self.finalNumber))
            self.final.pack()

    #enters the info from the {self.entry} field for processing to {}
    def enter(self):
        self.getEntry = str(self.entry.get())
        self.entry.delete(0, 100)
        self.calculations(self.getEntry)

    #inputs the buttons onto the {self.entry} field
    def buttonInput(self, buttonInput):
        #gets the length of how many chars the {self.entry} field has
        self.tempLength = len(str(self.entry.get()))
        #uses the length from above to put the {buttonInput} into the end of the {self.entry} field
        self.entry.insert(self.tempLength, buttonInput)
        
    #creates all of the buttons and entry for {self.window}
    def createInputs(self):
        #creates entry field
        self.entry = tk.Entry(self.window, width = 60)
        #creates the buttons
        self.button0 = tk.Button(self.window,  text = '0', command = lambda: self.buttonInput(0), width = 15, height = 7, bg = '#555555', fg = '#dddddd')
        self.button1 = tk.Button(self.window,  text = '1', command = lambda: self.buttonInput(1), width = 15, height = 7, bg = '#555555', fg = '#dddddd')
        self.button2 = tk.Button(self.window,  text = '2', command = lambda: self.buttonInput(2), width = 15, height = 7, bg = '#555555', fg = '#dddddd')
        self.button3 = tk.Button(self.window,  text = '3', command = lambda: self.buttonInput(3), width = 15, height = 7, bg = '#555555', fg = '#dddddd')
        self.button4 = tk.Button(self.window,  text = '4', command = lambda: self.buttonInput(4), width = 15, height = 7, bg = '#555555', fg = '#dddddd')
        self.button5 = tk.Button(self.window,  text = '5', command = lambda: self.buttonInput(5), width = 15, height = 7, bg = '#555555', fg = '#dddddd')
        self.button6 = tk.Button(self.window,  text = '6', command = lambda: self.buttonInput(6), width = 15, height = 7, bg = '#555555', fg = '#dddddd')
        self.button7 = tk.Button(self.window,  text = '7', command = lambda: self.buttonInput(7), width = 15, height = 7, bg = '#555555', fg = '#dddddd')
        self.button8 = tk.Button(self.window,  text = '8', command = lambda: self.buttonInput(8), width = 15, height = 7, bg = '#555555', fg = '#dddddd')
        self.button9 = tk.Button(self.window,  text = '9', command = lambda: self.buttonInput(9), width = 15, height = 7, bg = '#555555', fg = '#dddddd')
        self.buttonDice = tk.Button(self.window,  text = 'D', command = lambda: self.buttonInput('D'), width = 15, height = 7, bg = '#555555', fg = '#dddddd')
        self.buttonEnter = tk.Button(self.window,  text = 'Enter', command = self.enter, width = 15, height = 7, bg = '#555555', fg = '#dddddd')
        self.buttonMinus = tk.Button(self.window,  text = '-', command = lambda: self.buttonInput('-'), width = 15, height = 7, bg = '#555555', fg = '#dddddd')
        self.buttonAdd = tk.Button(self.window,  text = '+', command = lambda: self.buttonInput('+'), width = 15, height = 7, bg = '#555555', fg = '#dddddd')
        self.buttonDisAdv = tk.Button(self.window,  text = 'DisAdv.', command = lambda: self.buttonInput('DisAdv.'), width = 15, height = 7, bg = '#555555', fg = '#dddddd')
        self.buttonAdv = tk.Button(self.window,  text = 'Adv.', command = lambda: self.buttonInput('Adv.'), width = 15, height = 7, bg = '#555555', fg = '#dddddd')
        self.exit = tk.Button(self.window, text = 'exit', command = exit, width = 32, height = 7, bg = '#555555', fg = '#dddddd')

    #places all buttons and entry stuff from {createInputs()}
    def placeInputs(self):
        #places the entry field
        self.entry.grid(row = 1, column = 1, columnspan = 4)
        #places the buttons 
        self.button7.grid(row = 2, column = 1)
        self.button8.grid(row = 2, column = 2)
        self.button9.grid(row = 2, column = 3)
        self.buttonMinus.grid(row = 2, column = 4)

        self.button4.grid(row = 3, column = 1)
        self.button5.grid(row = 3, column = 2)
        self.button6.grid(row = 3, column = 3)
        self.buttonAdd.grid(row = 3, column = 4)

        self.button1.grid(row = 4, column = 1)
        self.button2.grid(row = 4, column = 2)
        self.button3.grid(row = 4, column = 3)
        self.buttonDisAdv.grid(row = 4, column = 4)

        self.button0.grid(row = 5, column = 1)
        self.buttonDice.grid(row = 5, column = 2)
        self.buttonEnter.grid(row = 5, column = 3)
        self.buttonAdv.grid(row = 5, column = 4)

        self.exit.grid(row = 6, column = 2, columnspan = 2)
    #changes the look of the app, mainly changes the color.
    def changeLooks(self, windowName):
        #set title of {self.window}
        windowName.title('Dice Calculator')
        #sets the background to grey
        windowName.configure(bg = '#444444')

    #code for running {self.window}
    def runWindow(self):
        
        self.window.mainloop()


#runs the code
window = main()

window.runWindow()
window.displayImages()

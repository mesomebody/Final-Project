#As of 10/02/2023, this code is opsolete

#imports tkinter as tk
import tkinter as tk
import ctypes as ct
import random
#makes the window
root = tk.Tk()
#sets the title for the {root} window
root.title('Calculator')

#creates and displays entry window
entry = tk.Entry(root, width = 60)
#sets the entry field to be put in the grid
entry.grid(row = 1, column = 1, columnspan=4)

#makes the second window
rootTwo = tk.Tk()

#sets the colors of the background
root.configure(bg = '#444444')
rootTwo.configure(bg = '#444444')

#changes the color of the main bar
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
dark_title_bar(root)
dark_title_bar(rootTwo)


#handles rolling the dice
def randomDice(dieSize):
    return random.randint(1, dieSize)


#code to roll the dice
def rollDice(info):
    #info is a string
    loopLength = len(info)
    tempNum = 0
    #times to roll
    timesToRoll = ''
    whatToRoll = ''
    whatToAdd = ''
    numberToAdd = ''
    finalNumber = 0
    while info[tempNum] != 'D':
        timesToRoll += info[tempNum]
        tempNum += 1
    tempNum += 1
    while tempNum < loopLength and info[tempNum] != '+' and info[tempNum] != '-':
        whatToRoll += info[tempNum]
        tempNum += 1
    if tempNum < loopLength:
        whatToAdd = info[tempNum]
        tempNum += 1
    while tempNum < loopLength:
        numberToAdd += info[tempNum]
        tempNum += 1
    tempNum = 0
    whatToRollTemp = int(whatToRoll)
    while tempNum < int(timesToRoll):
        tempNum += 1
        finalNumber += randomDice(whatToRollTemp)
        print(finalNumber)
    if whatToAdd == '+':
        finalNumber += int(numberToAdd)
        final = tk.Label(rootTwo, text = (timesToRoll, 'D', whatToRoll, '+', numberToAdd, '=', finalNumber))
        final.pack()
    elif whatToAdd == '-':
        finalNumber -= int(numberToAdd)
        final = tk.Label(rootTwo, text = (timesToRoll, 'D', whatToRoll, '-', numberToAdd, '=', finalNumber))
        final.pack()
    else:
        finalText = timesToRoll, 'D', whatToRoll, '=', finalNumber
        final = tk.Label(rootTwo, text = (finalText))
        final.pack()
    return finalNumber


#code for running button inputs
def numInput(command):
    tempEntry = entry.get()
    tempLength = len(tempEntry)
    entry.insert(tempLength, command)

def enter():
    getEntry = str(entry.get())
    entry.delete(0, 100)
    pushText = tk.Label(rootTwo, text = getEntry)
    pushText.pack()
    #process text
    tempReturn = rollDice(getEntry)


#creates the buttons for input
buttonZero = tk.Button(root, text = 0, command = lambda: numInput(0), width = 15, height = 7, bg = '#555555', fg = '#dddddd').grid(row = 6, column = 1)
buttonDie = tk.Button(root, text = 'D', command = lambda: numInput('D'), width = 15, height = 7, bg = '#555555', fg = '#dddddd').grid(row = 6, column = 2)
buttonEnter = tk.Button(root, text = 'Enter', command = enter, width = 15, height = 7, bg = '#555555', fg = '#dddddd').grid(row = 6, column = 3)
buttonAdv = tk.Button(root, text = 'Adv.', command = lambda: numInput('Adv'), width = 15, height = 7, bg = '#555555', fg = '#dddddd').grid(row = 6, column = 4)

buttonOne = tk.Button(root, text = 1, command = lambda: numInput(1), width = 15, height = 7, bg = '#555555', fg = '#dddddd').grid(row = 5, column = 1)
buttonTwo = tk.Button(root, text = 2, command = lambda: numInput(2), width = 15, height = 7, bg = '#555555', fg = '#dddddd').grid(row = 5, column = 2)
buttonThree = tk.Button(root, text = 3, command = lambda: numInput(3), width = 15, height = 7, bg = '#555555', fg = '#dddddd').grid(row = 5, column = 3)
buttonDisAdv = tk.Button(root, text = 'DisAdv.', command = lambda: numInput('DisAdv'), width = 15, height = 7, bg = '#555555', fg = '#dddddd').grid(row = 5, column = 4)

buttonFour = tk.Button(root, text = 4, command = lambda: numInput(4) , width = 15, height = 7, bg = '#555555', fg = '#dddddd').grid(row = 4, column = 1)
buttonFive = tk.Button(root, text = 5, command = lambda: numInput(5), width = 15, height = 7, bg = '#555555', fg = '#dddddd').grid(row = 4, column = 2)
buttonSix = tk.Button(root, text = 6, command = lambda: numInput(6), width = 15, height = 7, bg = '#555555', fg = '#dddddd').grid(row = 4, column = 3)
buttonPlus = tk.Button(root, text = '+', command = lambda: numInput('+'), width = 15, height = 7, bg = '#555555', fg = '#dddddd').grid(row = 4, column = 4)

buttonSeven = tk.Button(root, text = 7, command = lambda: numInput(7), width = 15, height = 7, bg = '#555555', fg = '#dddddd').grid(row = 3, column = 1)
buttonEight = tk.Button(root, text = 8, command = lambda: numInput(8), width = 15, height = 7, bg = '#555555', fg = '#dddddd').grid(row = 3, column = 2)
buttonNine = tk.Button(root, text = 9, command = lambda: numInput(9), width = 15, height = 7, bg = '#555555', fg = '#dddddd').grid(row = 3, column = 3)
ButtonMinus = tk.Button(root, text = '-', command = lambda: numInput('-'), width = 15, height = 7, bg = '#555555', fg = '#dddddd').grid(row = 3, column = 4)



#runs the main loop for the application
root.mainloop()
#runs the second window for the application
rootTwo.mainloop()

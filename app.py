import tkinter as tk
from tkinter import DISABLED
from PIL import Image, ImageTk
from random import randint
import ctypes

root = tk.Tk()
appTitle = 'Higher & Lower'

randomized = [0, 0, 0, 0]
isGameOver = False
labelCARD0 = tk.Label()
labelCARD1 = tk.Label()
labelCARD2 = tk.Label()
labelCARD3 = tk.Label()
frameTutorial = tk.Frame()
frameOuter = tk.Frame()
frameNewGame = tk.Frame()


def getBackColor():
    random = randint(0, 5)
    colors = ['blue', 'gray', 'green', 'purple', 'red', 'yellow']
    return colors[random]


def getColor():
    random = randint(0, 3)
    colors = ['C', 'D', 'H', 'S']
    return colors[random]


def getRandom():
    random = randint(2, 13)
    return random


def changeCard(which: int):
    randomized[which] = getRandom()
    # zabezpiecz przed wylosowaniem tej samej, co poprzednia
    if which != 0:
        while randomized[which] == randomized[which-1]:
            randomized[which] = getRandom()

    if randomized[which] == 10:
        temp = 'J'
    elif randomized[which] == 11:
        temp = 'Q'
    elif randomized[which] == 12:
        temp = 'K'
    elif randomized[which] == 13:
        temp = 'A'
    else:
        temp = randomized[which]
    tempCARD = ImageTk.PhotoImage(Image.open(
        'cards/{0}{1}.png'.format(temp, getColor())).resize((300, 500), Image.ANTIALIAS))
    if which == 0:
        labelCARD0.configure(image=tempCARD)
        labelCARD0.image = tempCARD
    elif which == 1:
        labelCARD1.configure(image=tempCARD)
        labelCARD1.image = tempCARD
    elif which == 2:
        labelCARD2.configure(image=tempCARD)
        labelCARD2.image = tempCARD
    elif which == 3:
        labelCARD3.configure(image=tempCARD)
        labelCARD3.image = tempCARD


def sendAlert(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)


def checkGameOver(toCheck, isHigher: bool):
    if isHigher:
        if randomized[toCheck] < randomized[toCheck-1]:
            return True
        else:
            return False
    else:
        if randomized[toCheck] > randomized[toCheck-1]:
            return True
        else:
            return False


def getNext(toReveal: int, isHigher: bool):
    global isGameOver
    if not isGameOver:
        if toReveal == 0:
            # pierwsza karta, niezależna od isHigher
            changeCard(toReveal)
        elif toReveal in (1, 2, 3):
            # sprawdz czy wylosowana
            if randomized[toReveal] == 0:
                # sprawdz czy poprzednia wylosowana
                if randomized[toReveal-1] != 0:
                    changeCard(toReveal)
                    # sprawdz czy wieksza niz poprzednia [x->x-1]
                    if checkGameOver(toReveal, isHigher):
                        isGameOver = True
                        sendAlert(appTitle, 'Przegrana', 0)
                    elif toReveal == 3:
                        sendAlert(appTitle, 'Wygrana', 0)
                else:
                    sendAlert(
                        appTitle, 'Nie możesz jeszcze sprawdzić tej karty', 0)
            else:
                sendAlert(appTitle, 'Ta karta została już wylosowana', 0)


def startGame():
    frameTutorial.destroy()
    frameOuter.place(relwidth=1, relheight=1)


root.title(appTitle)
root.iconbitmap('favicon.ico')
root.resizable(False, False)

canvas = tk.Canvas(root, height=720, width=1280)
canvas.pack()

# poradnik

frameTutorial = tk.Frame(root, bg="#121212")
frameTutorial.place(relwidth=1, relheight=1)
frameTutorial_inner = tk.Frame(frameTutorial, bg="#121212")
frameTutorial_inner.place(relwidth=0.7, relheight=0.2, relx=0.15, rely=0.4)
titleLabel = tk.Label(frameTutorial_inner, text="Higher & Lower",
                      bg="#121212", font=(None, 24), foreground="#654fd9")
titleLabel.pack()
descriptionLabel = tk.Label(frameTutorial_inner, text="Zdecyduj czy następna karta będzie wyższa, czy niższa",
                            bg="#121212", font=(None, 15), foreground="#aae")
descriptionLabel.pack(pady=5)
titleButton = tk.Button(frameTutorial_inner, text="Rozpocznij grę", padx=10,
                        pady=5, bg="white", borderwidth=0, font=(None, 12), command=lambda: startGame())
titleButton.pack()
copyrightLabel = tk.Label(frameTutorial_inner, text="Napisane w Pythonie przez: Marcel Gańczarczyk (mganczarczyk.pl)",
                          bg="#121212", font=(None, 7), foreground="#aae")
copyrightLabel.pack(pady=3)


# gra

frameOuter = tk.Frame(root, bg="#121212")

paddingFrame = tk.Frame(frameOuter, bg="#121212")
paddingFrame.place(relwidth=0.99, relheight=0.90, relx=0.005, rely=0.05)

# karta 1
frameInner1 = tk.Frame(paddingFrame, bg="#121212")
frameInner1.place(relwidth=0.25, relheight=1, relx=0)

frameInner1_button_Higher = tk.Button(
    frameInner1, text="Higher", padx=10, pady=5, bg="white", command=lambda: getNext(1, True), borderwidth=0)
frameInner1_button_Higher.pack(side="top")

frameInner1_button_Lower = tk.Button(
    frameInner1, text="Lower", padx=10, pady=5, bg="white", command=lambda: getNext(1, False), borderwidth=0)
frameInner1_button_Lower.pack(side="bottom")

img0 = ImageTk.PhotoImage(Image.open(
    'cards/{0}_back.png'.format(getBackColor())).resize((300, 500), Image.ANTIALIAS))
labelCARD0 = tk.Label(frameInner1, image=img0)
labelCARD0.pack(fill="none", expand=True)
getNext(0, False)

# karta 2
frameInner2 = tk.Frame(paddingFrame, bg="#121212")
frameInner2.place(relwidth=0.25, relheight=1, relx=0.25)

frameInner1_button_Higher = tk.Button(
    frameInner2, text="Higher", padx=10, pady=5, bg="white", command=lambda: getNext(2, True), borderwidth=0)
frameInner1_button_Higher.pack(side="top")

img1 = ImageTk.PhotoImage(Image.open(
    'cards/{0}_back.png'.format(getBackColor())).resize((300, 500), Image.ANTIALIAS))
labelCARD1 = tk.Label(frameInner2, image=img1)
labelCARD1.pack(fill="none", expand=True)

frameInner2_button_Lower = tk.Button(
    frameInner2, text="Lower", padx=10, pady=5, bg="white", command=lambda: getNext(2, False), borderwidth=0)
frameInner2_button_Lower.pack(side="top")

# karta 3
frameInner3 = tk.Frame(paddingFrame, bg="#121212")
frameInner3.place(relwidth=0.25, relheight=1, relx=0.5)

frameInner3_button_Higher = tk.Button(
    frameInner3, text="Higher", padx=10, pady=5, bg="white", command=lambda: getNext(3, True), borderwidth=0)
frameInner3_button_Higher.pack(side="top")

img2 = ImageTk.PhotoImage(Image.open(
    'cards/{0}_back.png'.format(getBackColor())).resize((300, 500), Image.ANTIALIAS))
labelCARD2 = tk.Label(frameInner3, image=img2)
labelCARD2.pack(fill="none", expand=True)

frameInner3_button_Lower = tk.Button(
    frameInner3, text="Lower", padx=10, pady=5, bg="white", command=lambda: getNext(3, False), borderwidth=0)
frameInner3_button_Lower.pack(side="top")

# karta 4
frameInner4 = tk.Frame(paddingFrame, bg="#121212")
frameInner4.place(relwidth=0.25, relheight=1, relx=0.75)

frameInner4_button_Higher = tk.Button(
    frameInner4, text="Higher", padx=10, pady=5, bg="white", borderwidth=0, state=DISABLED)
frameInner4_button_Higher.pack(side="top")

img3 = ImageTk.PhotoImage(Image.open(
    'cards/{0}_back.png'.format(getBackColor())).resize((300, 500), Image.ANTIALIAS))
labelCARD3 = tk.Label(frameInner4, image=img3)
labelCARD3.pack(fill="none", expand=True)

frameInner4_button_Lower = tk.Button(
    frameInner4, text="Lower", padx=10, pady=5, bg="white", borderwidth=0, state=DISABLED)
frameInner4_button_Lower.pack(side="top")

root.mainloop()

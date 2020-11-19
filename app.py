import tkinter as tk
from tkinter import filedialog, Text
from PIL import Image, ImageTk
import os
from random import randint

def klik():
    img2 = ImageTk.PhotoImage(Image.open('C:\\Users\\Marcel\\Desktop\\img{0}.jpg'.format(randint(1,2))))
    label.configure(image=img2)
    label.image = img2

root = tk.Tk()
root.title('Higher & Lower')
root.iconbitmap(r'C:\\Users\\Marcel\\Desktop\\favicon.ico')
root.resizable(False, False)

canvas = tk.Canvas(root, height=720, width=1280)
canvas.pack()


frameOuter = tk.Frame(root, bg="#263D42")
frameOuter.place(relwidth=1, relheight=1)

paddingFrame = tk.Frame(frameOuter, bg="#263D42")
paddingFrame.place(relwidth=0.99, relheight=0.90, relx=0.005, rely=0.05)

frameInner1 = tk.Frame(paddingFrame)
frameInner1.place(relwidth=0.25, relheight=1, relx=0)

frameInner1_button = tk.Button(frameInner1, text="Higher", padx=10, pady=5, bg="white", command=klik, borderwidth=0)
frameInner1_button.pack(side="top")

frameInner1_img = tk.Frame(frameInner1)
frameInner1_img.place(relwidth=0.95, relheight=0.9, relx=0.025, rely=0.05)

frameInner2_button = tk.Button(frameInner1, text="Lower", padx=10, pady=5, bg="white", command=klik, borderwidth=0)
frameInner2_button.pack(side="bottom")

img = ImageTk.PhotoImage(Image.open('C:\\Users\\Marcel\\Desktop\\img1.jpg'))
label = tk.Label(frameInner1_img, image=img)
label.pack()

# frameInner2 = tk.Frame(paddingFrame, bg="white")
# frameInner2.place(relwidth=0.25, relheight=1, relx=0.25)

# frameInner2 = tk.Frame(paddingFrame, bg="white")
# frameInner2.place(relwidth=0.25, relheight=1, relx=0.50)

# frameInner2 = tk.Frame(paddingFrame, bg="white")
# frameInner2.place(relwidth=0.25, relheight=1, relx=0.75)

root.mainloop()
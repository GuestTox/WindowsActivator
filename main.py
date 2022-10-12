from random import choice
from time import sleep
from tkinter import *
from tkinter import messagebox
import webbrowser

sitelist = (
    "https://www.youtube.com/channel/UC2agMj1ftrGL43Sd6j1CbNA",
    "https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley",
    "https://piv.pivpiv.dk/",
    "https://www.youtube.com/watch?v=EiZhe9Smgh4&ab_channel=NotFunny",
    "https://www.reddit.com/r/cumhentai/top/?t=all"
)

root = Tk()

root.geometry("300x100")
root.title("Windows Activator")

def troll():
    messagebox.showwarning("HACKED", "YOUR PC HAS BEEN HACKED.")
    messagebox.showwarning("HACKED", "YOU CANT ESCAPE.")
    messagebox.showwarning("HACKED", "YOU CANT CLOSE THIS NOW.")
    messagebox.showwarning("HACKED", "SAY GOODBYE TO YOUR PC.")
    for x in range(3):
        messagebox.showwarning("HACKED", "STOP CLOSING, IT WONT WORK.")
    for x in range(3):
        messagebox.showwarning("HACKED", "STOP NOW.")
    messagebox.showwarning("DONT CLOSE.", "IF YOU CLOSE THIS, YOUR COMPUTER WILL BE DAMAGED")
    root.attributes("-fullscreen", True)
    for widget in root.winfo_children():
        widget.destroy()
    root.config(bg="black")
    label = Label(root, text="Your PC Has been Hacked.", bg="black", fg="white", font=("Roboto Bold", 30))
    label.config(anchor=CENTER)
    label.pack(pady=250)
    labela = Label(root, text="If you restart your PC, it will be damaged forever.", bg="black", fg="white", font=("Roboto Bold", 30))
    labela.pack()

button = Button(root, text="Activate Windows.", anchor=CENTER, command=troll, pady=10, padx=10).pack(pady=25)

root.mainloop()

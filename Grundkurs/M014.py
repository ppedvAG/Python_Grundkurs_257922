# from tkinter import Tk, Label, Button, mainloop
from tkinter import *

###################################################

window = Tk()  # Schritt 1: Window erstellen

window.config(bg="lightblue")
window.geometry("1000x500+2500+300")
window.wm_title("Mein erstes Fenster")

###################################################

l = Label(text="Hallo Welt")
l.place(width=150, height=30, x=20, y=20)

b = Button(text="Zähler++")
b.place(width=150, height=30, x=20, y=60)

counter = 0
def increment():
	global counter
	counter += 1
	l.config(text=counter)

b.config(command=lambda: increment())  # Methodenzeiger

###################################################

if __name__ == "__main__":
	mainloop()
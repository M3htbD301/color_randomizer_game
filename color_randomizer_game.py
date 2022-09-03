from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
import random

root=Tk()
root.title("Encapsulation")
root.geometry("800x600")

label_name=Label(root, text="",font=("Lucida Sans Unicode", 20), bg="white")
label_name.place(relx=0.5, rely=0.5, anchor=CENTER)
class Game:
    def __init__(self):
        self.__score=0
    
    def updateGame(self):
        self.color=["red","orange","yellow","green","blue","purple"]
        self.random_number_for_color=random.randint(0,5)
        self.text=["red","orange","yellow","green","blue","purple"]
        self.random_number_for_text=random.randint(0,5)
        label_name["text"]=self.text[self.random_number_for_text]
        label_name["text"]=self.color[self.random_number_for_color]
        


btn = Button(root,text="Start",command=obj.updateGame, bg="dark olive green", fg="white", releif=Flat, padx=10, pady=1, font=("Arial",15))
btn.place(relx=0.95,rely=0.5, anchor=E)

"""what is obj supposed to be? i know its the object but what should i make it?"""
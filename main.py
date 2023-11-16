import re
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import nltk
from nltk.corpus import words

nltk.download("words")

class SpellingChecker:

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("600x500")

        self.text = Scrolledtext(Self.root, font = ("arial",14))
        self.text.bind("<Keyrelease>", self.check)
        self.text.pack()

        self.root.mainloop()

    def check(self,event):
        print ("Hello World")
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
        self.text.bind("<KeyRelease>", self.check)
        self.text.pack()

        self.old_spaces = 0

        self.root.mainloop()

    def check(self,event):
        content = self.text.get("1.0", tk.END)
        space_count = content.count(" ")
        if space_count != self.old_spaces:
            self.old_spaces = space_count
            for word in_content.spilt(" "):
                if re.sub(r"[^\w]", "", word.lower())

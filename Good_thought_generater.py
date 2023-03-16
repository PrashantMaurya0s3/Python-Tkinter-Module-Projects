from tkinter import *
import requests
import random

class ThoughtGenerator:
    def __init__(self, master):
        self.master = master
        self.master.title("Thought Generator")
        self.master.geometry("1000x300")
        self.master.config(bg='black')

        self.thought_label = Label(self.master, wraplength=800, font=("Courier New", 16, 'bold'), fg='red', bg='black')
        self.thought_label.configure(text="")
        self.thought_label.pack(ipadx=20, ipady=20, padx=20, pady=20)

        self.generate_thought_button = Button(self.master, text='GENERATE', command=self.generate, width=30,
                                            font=("Courier New", 16, 'bold'), bg="#FF0000", activebackground="#FF0000",
                                            fg="black", activeforeground="white")
        self.generate_thought_button.pack()

        self.master.mainloop()

    def generate(self):
        self.thought_label.configure(text="")
        thought_json = requests.get("http://api.quotable.io/random").json()
        thought = "{}\n\nBy: {}".format(thought_json['content'], thought_json['author'])
        print(thought)
        self.thought_label.configure(text=thought, fg='red', bg='black', font=("Courier New", 16, 'bold'))

if __name__ == "__main__":
    root = Tk()
    app = ThoughtGenerator(root)

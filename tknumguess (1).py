from tkinter import *
import tkinter as tk
import tkinter.messagebox
import random
class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.e = ""
        self.num = random.randrange(1,100)
        # widget can take all window
        self.pack(fill=BOTH, expand=1)

        # create button, link it to clickExitButton()
        exitButton = Button(self, text="Guess" ,command=self.clickExitButton)

        # place button at (0,0)
        exitButton.place(x=0, y=60)
        self.s = tk.Scale(self, label='none', from_=0, to=100, orient=tk.HORIZONTAL, length=500, showvalue=0,tickinterval=10, resolution=1, command=self.print_selection)
        self.s.pack()
    def print_selection(self,v):
        print(v)
        self.e = v
        self.s.config(label = v)
    def clickExitButton(self):
        print(self.e)
        if self.e == "":
            tkinter.messagebox.showerror('Error','You didn\'t even choose anything!')
        else:
            if int(self.e) == self.num:
                tkinter.messagebox.showinfo('game','you got it!')
                exit("you won!")
            else:
                if int(self.e) > self.num:
                    tkinter.messagebox.showwarning('note','lower')
                else:
                    tkinter.messagebox.showwarning('note','higher')




root = Tk()
app = Window(root)
root.wm_title("Number Guesser made with Tkinter")
root.geometry("500x85")
root.mainloop()

"""
TKNumGuess
Use with python
Dont Forget to install TK into your python installation using:
pip install tk
"""
import tkinter as tk, tkinter.messagebox, random
global awns
awns,nume,window, = random.randint(0,100),-1,tk.Tk()

def guess():
    if nume == -1:
      tkinter.messagebox.showerror('Alert!','Please choose a number!')
    else:
      if nume == awns:
        tkinter.messagebox.showinfo('Game','You win!')
        window.destroy()
      else:
        if nume > awns:
          tkinter.messagebox.showinfo('Game','The Number is lower. Try again!')
        else:
            tkinter.messagebox.showinfo('Game','The Number is higher. Try again!')
def print_selection(num):
  global nume
  nume = int(num)
hello,s,button = tk.Label(text="Guess the Number Between 0 and 100"),tk.Scale(window, from_=0, to=100, orient=tk.HORIZONTAL, length=200, showvalue=1,tickinterval=20, resolution=1, command=print_selection),tk.Button(text="Guess!",command=guess)
window.title("TKNumGuess")
window.geometry("240x100")
hello.pack()
s.pack()
button.pack()
tk.mainloop()

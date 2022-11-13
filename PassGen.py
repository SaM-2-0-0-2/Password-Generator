from tkinter import * 
import tkinter as tk
from tkinter import messagebox
import random

global password
def passgen():
    pass1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    pass2=[]
    for i in pass1:
        x=i.upper()
        pass2.append(x)
    pass1 = pass1 + pass2 + ['!','@','#','$','%','&','*']
    password=''
    for i in range (0,12):
        password = password + random.choices(pass1)[0]
    messagebox.showinfo('Password Generator',f'Generated Password: {password}')
       
    
root = Tk()
root.title("Password Generator")

c1 = Canvas(root, width = 500, height = 200, bg = "white")
c1.pack()

l1 = Label(root, text = 'Password Generator')
l1.config(font = ("bold", 20),bg = "black",fg = 'white')
c1.create_window(250, 30, window = l1)

br1 = Label(root, text='------------------------------------------------------------')
br1.config(font=("bold", 18),bg = "white",fg = 'grey')
c1.create_window(250, 80, window = br1)

Submit = Button(text = 'Generate',command = lambda:[passgen()], bg = 'pink', fg = 'black', font = ('helvetica', 15, 'bold'))
c1.create_window(250, 130, window = Submit)

root.mainloop()
from tkinter import *
from tkinter.font import BOLD
from tkinter.ttk import *
import time
from datetime import datetime

def refresh():
    t=time.strftime("%I:%M:%S")
    j = datetime.now().strftime(".%f")
    clock.config(text=t)
    time_label.config(text = time.strftime("%p"))
    s_label.config(text = j[:3])

    date_label.config(text= time.strftime("%d . %m . %Y"))    
    clock.after(10,refresh)
    
canvas = Tk()
canvas.geometry("400x115")
canvas.resizable(False, False)
canvas.title("Digital Clock")
canvas.config(background = "black")



clock = Label(canvas, font=('ds-digital', 80), background='black', foreground="red", anchor = "s")
clock.grid(row=0, column = 0, padx=5, pady = 0)


time_label = Label(canvas, font = ('ds-digital', 20), background='black', foreground="#02db47")
time_label.place(relx = 0.95,  
                   rely = 0.84, 
                   anchor = 's')

date_label = Label(canvas, font = ('ds-digital', 11, BOLD), background='black', foreground="#02db47")
date_label.place(relx = 0.04, rely = 0.02)

s_label = Label(canvas, font = ('ds-digital', 17), background='black', foreground="#ff1463")
s_label.place(relx = 0.921, rely = 0.14)

refresh()



mainloop()
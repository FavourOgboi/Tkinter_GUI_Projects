"""A simple converter app"""

from tkinter import *

root = Tk()
root.title("A Converter App")
root.configure(background = 'blue')

"""Functions"""
def convert():
    if entry.get().isnumeric():
        
        if click.get() == options[0]:
            solution = round(float(entry.get()) * 0.6214,2)
            mylab = Label(root,text = entry.get()+" km is converted to be " + str(solution) + "mile",background='yellow',fg='black')
            mylab.grid(row=1,column=0,padx = 11,sticky= W)
        if click.get() == options[1]:
            solution = round(float(entry.get()) * 2.20462,2)
            mylab = Label(root,text = entry.get()+" kg is converted to be " + str(solution) + "pound",background='yellow',fg='black')
            mylab.grid(row=1,column=0,padx = 11,sticky= W)
        if click.get() == options[2]:
            solution = round(float(entry.get()) / 60,2)
            mylab = Label(root,text = entry.get()+" seconds is converted to be " + str(solution) + "minutes",background='yellow',fg='black')
            mylab.grid(row=1,column=0,padx = 11,sticky= W)

    else:
        
        mylab = Label(root,text = "Please Enter A Number",background='yellow',fg='black')
        mylab.grid(row=1,column=0,padx = 11,sticky= W)

"""Value"""
entry = Entry(root , width = 40 , borderwidth = 5,bg="white",fg='black')
entry.grid(row = 0,column = 0,padx = 10,pady = 10)


"""Dropdown Box"""

options = [
    "km to mile",
    "kg to pound",
    "sec to min"
]

click = StringVar()
# Default
click.set(options[0])

drop = OptionMenu(root , click , *options)
drop.grid(row = 0, column= 1)


"""Button"""
button = Button(root,text="Convert",command = convert,borderwidth= 3)
button.grid(row = 0,column = 2,stick = N+E+W+S,padx= 8,pady=8,)


root.mainloop()

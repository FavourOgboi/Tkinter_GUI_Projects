"""A simple stopwatch app"""

import threading
from tkinter import *
from tkinter.ttk import *
from win10toast import ToastNotifier
from playsound import playsound
import time


root = Tk()
root.title("Stopwatch")
root.configure(background = 'black')


def stat():
    start = 1
    global hour,minute,sec

    hour = hourentry.get()
    minute = minentry.get()
    sec = secentry.get()
    
    if hourentry.get().isnumeric() and minentry.get().isnumeric() and secentry.get().isnumeric():
        
        label.config(text = hour +":"+ minute +":"+ sec)

        label.after(1000, update)

    else:
        labe = Label(root,text = "Warning: An option is left unfilled! ( please fill up the entry boxes )",background='yellow',foreground='black',borderwidth=3)
        labe.grid(row = 4 , column = 0,columnspan=6,padx=(10,10),pady=(10,10),sticky=N+E+W+S)


def update():

    # For seconds only
    if int(hour) == 0 and int(minute) == 0 and int(sec) != 0:

        global new_sec,seccal

        seccal = int(secentry.get()) - 1
        new_sec = str(seccal)
        secentry.delete(0,END)
        secentry.insert(0,new_sec)
        label.config(text = hour +":"+ minute +":"+ new_sec)
        
        if int(new_sec) != 0:
            stat()
        else:
            pass

    # for minute only    
    elif int(hour) == 0 and int(minute) != 0 and int(sec) == 0:
        
        global new_min,mincal

        if ((int(minentry.get()) * 60) / 60 ) == 1:  # if min = 1

            seccal = (int(minentry.get()) * 60)
            mincal = str(int(minentry.get()) - 1)
            minentry.delete(0,END)
            minentry.insert(0,mincal)
            new_min = str(seccal - 1)
            secentry.delete(0,END)
            secentry.insert(0,new_min)

            label.config(text = hour +":"+ mincal +":"+ new_min)
            
            if int(new_min) != 0:
                stat()
            else:
                pass
        
        # if min > 1
        elif ((int(minentry.get()) * 60) / 60 ) != 1:

            seccal = (int(minentry.get()) * 60)
            mincal = str(int(minentry.get()) - 1)
            minentry.delete(0,END)
            minentry.insert(0,mincal)
            secentry.delete(0,END)
            value = str(59)
            secentry.insert(0,value)
            new_min = str(seccal - 1)
            
            label.config(text = hour +":"+ mincal +":"+ value)

            if int(new_min) != 0:
                stat()
            else:
                pass

    # for min and sec (for returned)
    elif int(hour) == 0 and int(minute) != 0 and int(sec) != 0:

        # work on the sec first
        seccal = int(secentry.get()) - 1
        new_sec = str(seccal)
        secentry.delete(0,END)
        secentry.insert(0,new_sec)
        label.config(text = hour +":"+ minute +":"+ new_sec)
        
        if int(new_sec) != 0:
            stat()
        else:
            if int(minentry.get()) > 0:
                stat()
            else:
                pass
        
    # for hours only
    elif int(hour) != 0 and int(minute) == 0 and int(sec) == 0:

        global hourcal,new_hour,mvalue,svalue

        if ((int(hourentry.get()) * 60 * 60) / (60*60) ) == 1:  # if hour = 1
            seccount = str((int(hourentry.get()) * 60 * 60))
            new_hour = str(int(hourentry.get()) - 1)
            hourentry.delete(0,END)
            hourentry.insert(0,new_hour)

            mvalue = str(59)
            minentry.delete(0,END)
            minentry.insert(0,mvalue)
            

            svalue = str(59)
            secentry.delete(0,END)
            secentry.insert(0,svalue)

            label.config(text = hour +":"+ minute +":"+ sec)
            
            if int(seccount) != 0:
                stat()
            else:
                pass
        
        # if hours > 1
        elif ((int(hourentry.get()) * 60 * 60) / (60*60) ) > 1:  # if hour = 1

            hourcal = (int(hourentry.get()) * 60 * 60)
            new_hour = str(int(hourentry.get()) - 1)
            hourentry.delete(0,END)
            hourentry.insert(0,new_hour)

            mvalue = str(59)
            minentry.delete(0,END)
            minentry.insert(0,mvalue)
            

            svalue = str(59)
            secentry.delete(0,END)
            secentry.insert(0,svalue)

            stat()

    # for hours and min and sec 
    elif int(hour) != 0 and int(minute) != 0 and int(sec) != 0:
        
        # work on second
        seccount = str((int(hourentry.get()) * 60 * 60))
        new_hour = hourentry.get()
        new_min = minentry.get()
        new_sec = int(secentry.get()) - 1
        secentry.delete(0,END)
        secentry.insert(0,new_sec)

        label.config(text = hour +":"+ minute +":"+ sec)
            
        if int(seccount) != 0:
            stat()
        else:
            pass

    # for hour and min
    elif int(hour) != 0 and int(minute) != 0 and int(sec) == 0:

        # work on the minute first

        if ((int(minentry.get()) * 60) / 60 ) == 1:  # if min = 1

            seccal = (int(minentry.get()) * 60)
            mincal = str(int(minentry.get()) - 1)
            minentry.delete(0,END)
            minentry.insert(0,mincal)
            new_min = str(seccal - 1)
            secentry.delete(0,END)
            secentry.insert(0,new_min)

            label.config(text = hour +":"+ mincal +":"+ new_min)
            
            if int(new_min) != 0:
                stat()
            else:
                pass
     
        # if min > 1
        elif ((int(minentry.get()) * 60) / 60 ) != 1:

            seccal = (int(minentry.get()) * 60)
            mincal = str(int(minentry.get()) - 1)
            minentry.delete(0,END)
            minentry.insert(0,mincal)
            secentry.delete(0,END)
            value = str(59)
            secentry.insert(0,value)
            new_min = str(seccal - 1)
            
            label.config(text = hour +":"+ mincal +":"+ value)

            if int(new_min) != 0:
                stat()
            else:
                pass

    # for hours and sec
    elif int(hour) != 0 and int(minute) == 0 and int(sec) != 0:
        
        seccal = int(secentry.get()) - 1
        new_sec = str(seccal)
        secentry.delete(0,END)
        secentry.insert(0,new_sec)

        label.config(text = hour +":"+ minute +":"+ new_sec)
        
        if int(new_sec) != 0:
            stat()
        else:
            stat()

def pause():
    global hourcal,mincal,seccal
    hourcal = hourentry.get()
    mincal = minentry.get()
    seccal = secentry.get()
    hourentry.delete(0,END)
    minentry.delete(0,END)
    secentry.delete(0,END)

    label.config(text = hourcal+":"+mincal+":"+seccal)

def resume():
    
    if hourentry.get().isnumeric() and minentry.get().isnumeric() and secentry.get().isnumeric():
        pass
    
    elif hourentry.get() == '' and minentry.get() == '' and secentry.get() == '':

        hourentry.insert(0,hourcal)
        minentry.insert(0,mincal)
        secentry.insert(0,seccal)

        stat()
    else:
        stat()

text = Label(root,text= "TIMER",font=('Young 50',60),background='black',foreground='blue')
text.grid(row=0,column=0,columnspan=6,padx= (10,10))

labelhour = Label(root,text="HOURS:",borderwidth=2,background='yellow')
labelhour.grid(row=1,column=0,sticky=E,padx=(28,0))
hourentry = Entry(root,width=20)
hourentry.grid(row=1,column=1,sticky=W+N+S+E,pady=5)

labelmin = Label(root,text="MINUTES:",background='yellow',borderwidth=2)
labelmin.grid(row=1,column=2,sticky=E,pady=5)
minentry = Entry(root,width=20)
minentry.grid(row=1,column=3,sticky=W+N+S+E,pady=5)

labelsec = Label(root,text="SECONDS:",background='yellow',borderwidth=2)
labelsec.grid(row=1,column=4,padx=(28,0),pady=5)
secentry = Entry(root,width=20)
secentry.grid(row=1,column=5,sticky=W,padx=(0,28))


label = Label(root,text = "00:00:00",font=('Helvetica',48),foreground='red',background='black')
label.grid(row=2,column=0,columnspan=6)



start = Button(root,text= "Start timer",command=stat)
pausee = Button(root,text= "Pause Timer",command=pause)
resumee = Button(root,text= "Resume Timer",command=resume)
quit = Button(root,text= "Quit Timer",command=root.quit)
start.grid(row=3,column=1)
pausee.grid(row=3,column=2)
resumee.grid(row=3,column=3)
quit.grid(row=3,column=4)

root.mainloop()
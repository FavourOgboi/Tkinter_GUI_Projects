from tkinter import *
import time

root = Tk()
root.title('CLock')
root.geometry('600x400')
root.configure(background = 'black')
# Time.strftime(docs)
def clock():
    global day
    hour = time.strftime("%I")
    minute = time.strftime("%M")
    sec = time.strftime("%S")
    day = time.strftime("%A")
    ampm = time.strftime("%p")
    timezone = time.strftime("%Z")
    label.config(text = hour +":"+ minute +":"+ sec +" "+ ampm )
    label.after(1000,clock)
    labe.config(text = timezone)
    label2.config(text = day)

label = Label(root,text = "",font=('Helvetica',48),fg='green',bg='yellow')
label.pack(pady=20)

labe = Label(root,text = 'day' ,font=('Helvetica',14))
labe.pack(pady=10)

label2 = Label(root,text = 'day' ,font=('Helvetica',14))
label2.pack(pady=20)


clock()
# label.after(5000,update) # update is a func

# 1000msec = 1sec

root.mainloop()
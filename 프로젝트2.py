from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Calculator')
root.geometry('261x100')

def button_pressed(value):
    num_entry.insert('end',value)
    print(value,"pressed")

entry_value=StringVar(root,value='')

num_entry = ttk.Entry(root,textvariable=entry_value,width=20)
num_entry.grid(row=0,columnspan=3)


button1 = ttk.Button(root,text='7',command=lambda:button_pressed('7'))
button1.grid(row=1,column=0)
button1 = ttk.Button(root,text='8',command=lambda:button_pressed('8'))
button1.grid(row=1,column=1)
button1 = ttk.Button(root,text='9',command=lambda:button_pressed('9'))
button1.grid(row=1,column=2)


button1 = ttk.Button(root,text='4',command=lambda:button_pressed('4'))
button1.grid(row=2,column=0)
button1 = ttk.Button(root,text='5',command=lambda:button_pressed('5'))
button1.grid(row=2,column=1)
button1 = ttk.Button(root,text='6',command=lambda:button_pressed('6'))
button1.grid(row=2,column=2)

button1 = ttk.Button(root,text='1',command=lambda:button_pressed('1'))
button1.grid(row=3,column=0)
button1 = ttk.Button(root,text='2',command=lambda:button_pressed('2'))
button1.grid(row=3,column=1)
button1 = ttk.Button(root,text='3',command=lambda:button_pressed('3'))
button1.grid(row=3,column=2)

root.mainloop()

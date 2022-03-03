import tkinter, calendar
from tkinter import ttk
from datetime import date
from tkinter.messagebox import showinfo
window = tkinter.Tk()

window.title("Days by date calculator")
window.geometry("500x75")

month = {calendar.month_name[i] : i for i in range(1,13)}

for i in range(3):
    window.columnconfigure(i, weight=3)

today = date.today()

def goTime():
    global comboBox1, comboBox2, yearBox, today
    custom = date(int(yearBox.get()), month[comboBox2.get()], int(comboBox1.get()))
    difference = (custom-today).days
    if difference == 0:
        showinfo(message="Dit is vandaag")
    elif difference < 0:
        showinfo(message="Dit is {} dagen geleden".format(str(abs(difference))))
    else:
        showinfo(message="Dit is {} dagen in de toekomst".format(str(difference)))


textlabel = tkinter.Label(window, text="Date:")

button = tkinter.Button(window, text="Go", command=goTime)



text1 = tkinter.StringVar(value =str(int(today.strftime("%d"))))
comboBox1 = ttk.Combobox(window, textvariable=text1)

text2 = tkinter.StringVar(value=str(calendar.month_name[int(today.strftime("%m"))]))
comboBox2 = ttk.Combobox(window, textvariable=text2)

text3 = tkinter.StringVar(value=str(today.strftime("%Y")))
yearBox = ttk.Entry(window, textvariable=text3)

comboBox1['state'] = "readonly"
comboBox1['values'] = list(range(1,32))

comboBox2['state'] = "readonly"
comboBox2['values'] = list(calendar.month_name)[1:]

textlabel.grid(column=1, row=1)
comboBox1.grid(column=0,row=2)

comboBox2.grid(column=1,row=2)

yearBox.grid(column=2,row=2)

button.grid(column=1, row=3)

window.mainloop()
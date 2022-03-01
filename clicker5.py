import tkinter

colors = ["gray", "red", "green"]
lastButton = ""
num = 0



def changeWindow(color=None):
    global num
    if type(color) is str:
        window.configure(bg=color)
    else:
        if num == 0:
            window.configure(bg=colors[0])
        elif num < 0:
            window.configure(bg=colors[1])
        else:
            window.configure(bg=colors[2])


def yellowWindow(event):
    window.configure(bg="yellow")


def labelClick(event):
    global num
    if lastButton == "Up":
        num *= 3
    else:
        num /= 3
    stringvar.set(str(int(num)))


def goUp(event=None):
    global lastButton, num, checkVar
    lastButton = "Up"
    num += 1
    stringvar.set(str(int(num)))
    changeWindow()
    checkVar.set("0")
    checker.config(state="active")


def goDown(event=None):
    global lastButton, num, checkVar
    lastButton = "Down"
    num -= 1
    stringvar.set(str(int(num)))
    changeWindow()
    checkVar.set("0")
    checker.config(state="active")


def checkerChanger():
    global checkVar, num
    if checkVar.get() == "1":
        window.after(5, checkerChanger)
        if lastButton == "Up":
            num += 1
        else:
            num -= 1
        stringvar.set(str(int(num)))
        changeWindow()
        




window = tkinter.Tk()

checkVar = tkinter.StringVar(value="0")
up = tkinter.Button(window, text="Up", command=goUp)
down = tkinter.Button(window, text="down", command=goDown)
checker = tkinter.Checkbutton(window,text='',command=checkerChanger, variable = checkVar, onvalue="1", offvalue="0", state="disabled")

window.title("Clicker")
window.geometry("200x100")

window.bind("<Up>", goUp)
window.bind("+", goUp)

window.bind("<Down>", goDown)
window.bind("-", goDown)

window.bind("<space>", labelClick)

stringvar = tkinter.StringVar(value=str(num))

label1 = tkinter.Label(
    window,
    bg="white",
    fg="orange"
)

label1.bind("<Enter>", yellowWindow)
label1.bind("<Leave>", changeWindow)
label1.bind("<Double-Button-1>", labelClick)

label1.configure(textvariable=stringvar)

checker.pack()
up.pack()
label1.pack()
down.pack()

window.mainloop()
import tkinter, random


commands = ["Press: w", "Press: a", "Press: s", "Press: d", "Press: space", "Click", "Double click", "Triple click"]
question = "Click"
maxTimer = 20
timer = 20
points = -2
gaming = True

window = tkinter.Tk()
label1 = tkinter.Label(
    window,
    bg="white",
    fg="black"
)
label2 = tkinter.Label( #points/Time
    window,
    bg="black",
    fg="white"
)
timerBox = tkinter.Entry(window, textvariable = tkinter.StringVar(window,value="20"))

stringvar = tkinter.StringVar(value="Klik hier om te beginnen")
stringvar2 = tkinter.StringVar(value="Time Remaining: {}                {} points".format(0, 0))

def nextCommand(point):
    global question, points
    if gaming:
        points += point
        label1.place(relx=random.uniform(0.3, 1.0),rely=random.uniform(0.1,0.9),relwidth=0.3,anchor="ne")
        question = random.choice(commands)
        stringvar.set(question)
        stringvar2.set("Time Remaining: {}                {} points".format(timer, points))
        if "space" in question:
            question = " "
        elif "w" in question:
            question = "w"
        elif "a" in question:
            question = "a"
        elif "d" in question:
            question = "d"
        elif "s" in question:
            question = "s"


def startGame():
    global gaming, question, timer, points
    gaming = True
    timer = maxTimer
    points = -2
    yes.place(relx=1, rely=1,relwidth=0.2,anchor='ne')
    no.place(relx=1, rely=1,relwidth=0.2,anchor='ne')
    label1.place(relx=0.75,rely=0.5,relwidth=0.5,anchor="ne")
    stringvar.set("Klik hier om te beginnen")
    stringvar2.set("Time Remaining: {}                {} points".format(maxTimer, 0))
    question = "Click"

def tick():
    global timer
    timer -= 1
    if timer == 0:        
        return stopGame()
    stringvar2.set("Time Remaining: {}                {} points".format(timer, points))
    window.after(1000, tick)


def command(event):
    if event.char == question:
        nextCommand(1)

def click(event):
    global timer, maxTimer
    if points == -2:
        window.after(1000, tick)
        try:
            maxTimer = int(timerBox.get())
        except:
            maxTimer = 20
        timer = maxTimer
        timerBox.place(relx=1, rely=1,relwidth=0.2,anchor='ne')
    if question == "Click":
        nextCommand(2)
        

def doubleclick(event):
    if question == "Double click":
        nextCommand(2)

def tripleclick(event):
    if question == "Triple click":
        nextCommand(2)


def stopGame():
    global gaming
    gaming = False
    label1.place(relx = 0.75, rely=0.5, relwidth = 0.5, anchor = 'ne')
    stringvar.set("Score: {}\nWil je opnieuw spelen?".format(points))
    stringvar2.set("Time Remaining: {}                {} points".format(0, points))
    yes.place(relx = 0.45, rely=0.75,relwidth=0.2,anchor='ne')
    no.place(relx = 0.75, rely=0.75,relwidth=0.2,anchor='ne')


window.title("FPS")
window.geometry("400x200")

yes = tkinter.Button(window,bg="black", fg="white",command = startGame,text="Yes")
no = tkinter.Button(window,bg="black",fg="white", command = lambda : window.destroy(),text="No")  

window.bind("w", command)
window.bind("a", command)
window.bind("s", command)
window.bind("d", command)
window.bind("<space>", command)


label1.place(relx=0.75,rely=0.5,relwidth=0.5,anchor="ne")
timerBox.place(relx = 0.45, rely=0.75, relwidth=0.2, anchor ='ne')


label1.bind("<Button-1>", click)
label1.bind("<Double-Button-1>", doubleclick)
label1.bind("<Triple-Button-1>", tripleclick)

label1.config(textvariable=stringvar)
label2.config(textvariable=stringvar2)

label2.pack()

window.mainloop()


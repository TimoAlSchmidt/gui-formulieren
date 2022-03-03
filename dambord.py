import tkinter

window = tkinter.Tk()

window.title("Dambord")
window.geometry("500x500")
window.config(bg="orange")

for i in range(10):
    window.columnconfigure(i, weight=10)

black = tkinter.Label(window, bg="black")

for y in range(10):
    for x in range(10):
        if (x+y)%2==1:
            white = tkinter.Label(window, bg="white",width=20, height=2)
            white.grid(column=x,row=y,sticky=tkinter.E)
        else:
            black = tkinter.Label(window, bg="black",width=20, height=2)
            black.grid(column=x,row=y,sticky=tkinter.E)

window.mainloop()
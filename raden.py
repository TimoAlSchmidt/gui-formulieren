import tkinter, random, string
from tkinter import ttk
from tkinter.messagebox import showinfo, askyesno, WARNING

window = tkinter.Tk()

window.title("Wordguess")
window.geometry("500x75")
for i in range(10):
    window.columnconfigure(i, weight=9)
guess = []
word = ""
score = 0

def removeWidgets():
    for widget in window.winfo_children():
        widget.destroy()

def reset():
    global woord
    removeWidgets()
    
    woord = tkinter.StringVar()
    startEntry = tkinter.Entry(window, textvariable=woord)

    startButton = tkinter.Button(window, text="Stel woord in", command=startRaden)

    startEntry.grid(row=0,column=0)
    startButton.grid(row=1,column=0)


def randomLetters(letter):
    upper = string.ascii_uppercase
    listWithLetters = [letter]
    while len(listWithLetters) < 5:
        let = random.choice(upper)
        if let not in listWithLetters:
            listWithLetters.append(let)
    return listWithLetters


def gok():
    global guess, word, score
    gokker = []
    for let in guess:
        gokker.append(let.get())
    worder = list(word)

    if worder == gokker:
        answer = askyesno(title="Winner!",message="Gefeliciteerd, je hebt het woord geraden, je score is {}. Wil je opnieuw spelen?".format(score))
        if not answer:
            window.destroy()
        else:
            reset()
    else:
        num = 0
        for i in range(len(worder)):
            if worder[i] != gokker[i]:
                score -= 2
            else:
                num += 1
        if score > 0:
            showinfo(title="Oops...",message="Dat is niet correct. Je hebt {} letters correct.".format(num))
        else:
            showinfo(title="Oh nee...",message="Dat is niet correct. Je hebt geen score meer. Het spel is voorbij.")
            window.destroy()


def startRaden():
    global guess, word, score
    word = woord.get().upper()
    uppercase = string.ascii_uppercase
    if len(word) < 4:
        showinfo(title="Te kort!", message="Het woord moet minimaal 4 letters lang zijn!",icon=WARNING)
    elif len(word) > 7:
        showinfo(title="Te lang!", message="Het woord moet maximaal 7 letters lang zijn!",icon=WARNING)
    else:
        score = len(word) * len(word)
        removeWidgets()
        guess = []
        for i in range(len(word)):
            letter = tkinter.StringVar()
            guess.append(letter)
            letters = randomLetters(word[i])
            random.shuffle(letters)
            letter.set(letters[0])
            spin = tkinter.Spinbox(window,values=letters,wrap=True, textvariable=letter, state="readonly")
            spin.grid(row=1,column=i)
        
        guessButton = tkinter.Button(window,text="Doe een gok",command=gok)
        guessButton.grid(row=2, column=int(len(word)/2))


reset()


window.mainloop()
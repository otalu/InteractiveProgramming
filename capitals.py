"""
Parses through the Wikipedia pages of countries and returns a dictionary of
their capitals.

Authors = Anupama Krishnan, Onur Talu
"""

import tkinter
from tkinter import *
from tkinter import messagebox
import random
import countries


distance = 0
wrong = 0


def game():
    dictCapitals = countries.dictCountries
    country = random.choice(list(dictCapitals.keys()))

    window = Tk()
    window.title("Do you know your capitals?")
    window.geometry("500x250")

    asktext = "What is the capital of %s?" % country
    question = tkinter.Label(window, text=asktext)
    question.place(x=5, y=5)

    def result(txt):
        global distance
        global wrong
        if txt == dictCapitals[country]:
            distance += 1
            if distance < 10:
                restart()
            else:
                msg = messagebox.showinfo('Congratulations', "Your Final Score is %s" % score)
                window.quit()
                window.destroy()

        else:
            msg = messagebox.showinfo('NO', "WRONG! Try again.")
            wrong += 1

    def restart():
        msg = messagebox.showinfo('YES!', "You're Right")
        window.destroy()
        game()

    def choose_correct():
        val = [0, 1, 2, 3]
        correct = random.choice(val)
        return correct

    def score():
        factor = 10
        current = (distance - wrong) * factor
        return current

    score = score()
    scoretext = "Current Score = %s" % score
    scoreboard = tkinter.Label(window, text=scoretext)
    scoreboard.place(x=300, y=225)

    Atxt = 0
    Btxt = 0
    Ctxt = 0
    Dtxt = 0
    buttons = [Atxt, Btxt, Ctxt, Dtxt]
    correct = choose_correct()
    buttons[correct] = dictCapitals[country]

    if buttons[0] != buttons[correct]:
        buttons[0] = random.choice(list(dictCapitals.values()))
    if buttons[1] != buttons[correct]:
        buttons[1] = random.choice(list(dictCapitals.values()))
    if buttons[2] != buttons[correct]:
        buttons[2] = random.choice(list(dictCapitals.values()))
    if buttons[3] != buttons[correct]:
        buttons[3] = random.choice(list(dictCapitals.values()))

    Atxt = buttons[0]
    Btxt = buttons[1]
    Ctxt = buttons[2]
    Dtxt = buttons[3]

    A = Button(window, text=Atxt, command=lambda: result(Atxt))
    A.place(x=50, y=50)

    B = Button(window, text=Btxt, command=lambda: result(Btxt))
    B.place(x=50, y=100)

    C = Button(window, text=Ctxt, command=lambda: result(Ctxt))
    C.place(x=50, y=150)

    D = Button(window, text=Dtxt, command=lambda: result(Dtxt))
    D.place(x=50, y=200)

    window.mainloop()


if __name__ == "__main__":
    game()

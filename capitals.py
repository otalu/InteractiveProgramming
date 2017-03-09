"""
Makes a 10 questions long trivia game that asks what the capital of a country
is and then gives three random capitals along with the right one in a
randomized order.
Every correct answer is 10 and every false answer is -10 points. Game doesn't
continue unless each question is answered correctly.
It takes the capital-country information from a dictionary in the
script countries.py.

Authors = Anupama Krishnan, Onur Talu
"""

import tkinter  # imports the gui package
from tkinter import *
from tkinter import messagebox
import random
import countries


wrong = 0  # sets the initial number of wrong answered to 0
qno = 1  # sets the initial value for the question number to 1


def game():
    """
    Main game function.
    Takes in the dictCapitals from countries.py
    Creates a window with a question, four choices for the question and
    the current score of the player.
    """
    dictCapitals = countries.dictCountries
    country = random.choice(list(dictCapitals.keys()))

    window = Tk()
    window.title("Do you know your capitals?")
    window.geometry("500x250")

    asktext = "%s) What is the capital of %s?" % (qno, country)
    question = tkinter.Label(window, text=asktext)
    question.place(x=5, y=5)

    def result(txt):
        """
        Compares the answer input by the user and the correct answer. If the
        number of questions asked is less than 10, it asks another question.
        """
        global wrong, qno
        if txt == dictCapitals[country]:
            qno += 1
            if qno <= 10:
                restart()
            else:
                msg = messagebox.showinfo('Congratulations', "Your Final Score is %s" % score)
                window.quit()
                window.destroy()

        else:
            msg = messagebox.showinfo('NO', "WRONG! Try again.")
            wrong += 1

    def restart():
        """
        Asks another question when called.
        """
        msg = messagebox.showinfo('YES!', "You're Right")
        window.destroy()
        game()

    def choose_correct():
        """
        Chooses a random number to be the correct answer, so that the correct
        asnwer is not always e.g. the second choice.
        """
        val = [0, 1, 2, 3]
        correct = random.choice(val)
        return correct

    def score():
        """
        Determines the score of the user.
        """
        factor = 10
        current = (qno - wrong - 1) * factor
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

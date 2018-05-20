#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    # for Python2
    from Tkinter import *
except ImportError:
    # for Python3
    from tkinter import *

from random import *

window = Tk()

pos = 0
tour = 5

# Fonctions qui créent les cercles lorsqu'on appuie sur un bouton
def btnBlue(this, btn):
    global pos
    if not pos >= 4:
        this.create_oval(10 + 50 * pos, 10, 40 + 50 * pos, 40, fill="blue")
        pos += 1
        listInput.append("blue")
    if pos == 4:
        btn.config(state=NORMAL)


def btnRed(this, btn):
    global pos
    if not pos >= 4:
        this.create_oval(10 + 50 * pos, 10, 40 + 50 * pos, 40, fill="red")
        pos += 1
        listInput.append("red")
    if pos == 4:
        btn.config(state=NORMAL)


def btnBlack(this, btn):
    global pos
    if not pos >= 4:
        this.create_oval(10 + 50 * pos, 10, 40 + 50 * pos, 40, fill="black")
        pos += 1
        listInput.append("black")
    if pos == 4:
        btn.config(state=NORMAL)


def btnGreen(this, btn):
    global pos
    if not pos >= 4:
        this.create_oval(10 + 50 * pos, 10, 40 + 50 * pos, 40, fill="green")
        pos += 1
        listInput.append("green")
    if pos == 4:
        btn.config(state=NORMAL)


def btnYellow(this, btn):
    global pos
    if not pos >= 4:
        this.create_oval(10 + 50 * pos, 10, 40 + 50 * pos, 40, fill="yellow")
        pos += 1
        listInput.append("yellow")
    if pos == 4:
        btn.config(state=NORMAL)


def btnWhite(this, btn):
    global pos
    if not pos >= 4:
        this.create_oval(10 + 50 * pos, 10, 40 + 50 * pos, 40, fill="white")
        pos += 1
        listInput.append("white")
    if pos == 4:
        btn.config(state=NORMAL)


# Fonction principale qui s'active lorsqu'on appuie sur validé
def master(sol, canOut, canIn, btn):
    global tour
    listColors = []
    solutions = []
    for i in range(0, len(listInput)):
        listColors.append(listInput[i])
    for p in range(0, len(sol)):
        solutions.append(sol[p])
    i = 0
    # bpbc = bonne place bonne couleur; mpbc = mauvaise place bonne couleur
    bpbc = 0
    mpbc = 0
    while i < 4:
        if solutions[i] == listInput[i]:
            solutions[i] = 0
            listInput[i] = 1
            bpbc += 1
            i += 1
        else:
            i += 1
    j = 0
    while j < 4:
        l = 0
        while l < 4:
            if solutions[l] == listInput[j]:
                mpbc += 1
                solutions[l] = 0
                listInput[j] = 1
                l = 4
            else:
                l += 1
        j += 1

    posx1 = [10, 30, 10, 30]
    posy1 = [10, 10, 30, 30]
    posx2 = [20, 40, 20, 40]
    posy2 = [20, 20, 40, 40]
    for i in range(0, bpbc):
        canOut.create_oval(posx1[i], posy1[i] + 50 * tour, posx2[i], posy2[i] + 50 * tour, fill="red")
    for j in range(bpbc, bpbc + mpbc):
        canOut.create_oval(posx1[j], posy1[j] + 50 * tour, posx2[j], posy2[j] + 50 * tour, fill="white")
    index = 0
    for k in listColors:
        canIn.create_oval(10 + 50 * index, 10 + 50 * tour, 40 + 50 * index, 40 + 50 * tour, fill=k)
        index += 1
    for m in range(0, len(listInput)):
        listInput.pop()
    for n in range(0, len(listColors)):
        listColors.pop()
    canIn.create_rectangle(2, 2, 198, 48, fill="white", width=0)
    btn.config(state=DISABLED)
    global pos
    pos = 0
    tour -= 1
    text.set("Il vous reste " + str(tour) + " tour(s) !")
    if tour == 0 or bpbc == 4:
        colBlue.config(state=DISABLED)
        colGreen.config(state=DISABLED)
        colYellow.config(state=DISABLED)
        colRed.config(state=DISABLED)
        colWhite.config(state=DISABLED)
        colBlack.config(state=DISABLED)
        print("end")
        if bpbc == 4:
            text.set("Vous avez gagné !")
        else:
            text.set("Vous avez perdu. La solution était :")
            ind = 0
            for k in sol:
                canIn.create_oval(10 + 50 * ind, 10, 40 + 50 * ind, 40, fill=k)
                ind += 1

# Fonction qui initialise la fenêtre
def init():
    global pos
    pos = 0
    global listInput
    listInput = []
    solutions = []
    colors = ["green", "white", "blue", "black", "yellow", "red"]
    for i in range(0, 4):
        solutions.append(colors[randint(0, 5)])
    print(solutions)

    # Frame text
    Frame1 = Frame(window, borderwidth=2, relief=GROOVE)
    Frame1.pack(side=TOP, padx=5, pady=5)

    # Frame Color selection + Frame2
    Frame3 = Frame(window, bd=2, relief=GROOVE)
    Frame3.pack(side=TOP, padx=5, pady=5)

    # Frame Input + Output
    Frame2 = Frame(Frame3, bd=2, relief=GROOVE)
    Frame2.pack(side=LEFT, padx=5, pady=5)

    # Frame buttons
    Frame4 = Frame(window, bd=2, height=50, width=250, relief=GROOVE)
    Frame4.pack(side=BOTTOM)

    # Text
    global text
    text = StringVar()
    text.set("Commencez")
    label = Label(Frame1, textvariable=text, padx=5, pady=5)
    label.pack()

    # Input
    can2 = Canvas(Frame2, bd=2, height=300, width=200, relief=GROOVE)
    for i in range(0, 6):
        can2.create_rectangle(0, 50 * i, 200, 50 * i + 50, width=2)
    can2.pack(side=LEFT)

    # Output
    can3 = Canvas(Frame2, bd=2, height=300, width=50, relief=GROOVE)
    for i in range(0, 6):
        can3.create_rectangle(0, 50 * i, 50, 50 * i + 50, width=2)
    can3.pack(side=RIGHT)

    # Color Selection
    global colBlue, colYellow, colBlack, colGreen, colRed, colWhite
    can4 = Canvas(Frame3, bd=2, height=250, width=50, relief=GROOVE, )
    colBlue = Button(can4, text="Blue", padx=5, pady=5, bg="blue", fg="white", command=lambda: btnBlue(can2, btnValid))
    colBlue.pack(side=TOP, fill=BOTH)
    colYellow = Button(can4, text="Yellow", padx=5, pady=5, bg="yellow", command=lambda: btnYellow(can2, btnValid))
    colYellow.pack(side=TOP, fill=BOTH)
    colRed = Button(can4, text="Red", padx=5, pady=5, bg="red", command=lambda: btnRed(can2, btnValid))
    colRed.pack(side=TOP, fill=BOTH)
    colWhite = Button(can4, text="White", padx=5, pady=5, bg="white", command=lambda: btnWhite(can2, btnValid))
    colWhite.pack(side=TOP, fill=BOTH)
    colBlack = Button(can4, text="Black", padx=5, pady=5, bg="black", fg="white",
                      command=lambda: btnBlack(can2, btnValid))
    colBlack.pack(side=TOP, fill=BOTH)
    colGreen = Button(can4, text="Green", padx=5, pady=5, bg="green", command=lambda: btnGreen(can2, btnValid))
    colGreen.pack(side=TOP, fill=BOTH)
    can4.pack(fill=BOTH)

    # Reinitialisation
    btnReinit = Button(Frame4, text="Reinitialisation", padx=5, pady=5,
                       command=lambda: reinit(Frame1, Frame2, Frame3, Frame4))
    btnReinit.pack(side=LEFT, fill=BOTH)
    # Quit
    btnQuit = Button(Frame4, text="Quit", padx=5, pady=5, command=window.quit)
    btnQuit.pack(side=LEFT, fill=BOTH)
    # Validation
    btnValid = Button(Frame4, text="Validation", padx=5, pady=5,
                      command=lambda: master(solutions, can3, can2, btnValid))
    btnValid.config(state=DISABLED)
    btnValid.pack(side=RIGHT, fill=BOTH)

# Fonction qui réinitialise
def reinit(F1, F2, F3, F4):
    F1.destroy()
    F2.destroy()
    F3.destroy()
    F4.destroy()
    global tour
    tour = 5
    init()


init()
window.mainloop()

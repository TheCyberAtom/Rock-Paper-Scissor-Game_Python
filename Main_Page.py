from tkinter import *
import random

root = Tk(className=' ROCK PAPER SCISSOR Game')
root.geometry('1000x800')

# variables
values = ['Rock', 'Paper', 'Scissor']


def click_rock():
    user_rock = 'Rock'
    cpu(user_rock)


def click_paper():
    user_paper = 'Paper'
    cpu(user_paper)


def click_scissor():
    user_scissor = 'Scissor'
    cpu(user_scissor)


def cpu(result):
    res.delete('1.0', 'end')
    cpu_selection = random.choice(values)
    if cpu_selection == 'Rock':
        cpu_l = Label(root, image=image_r)
        cpu_l.grid(row=3, column=4)
    if cpu_selection == 'Paper':
        cpu_l = Label(root, image=image_p)
        cpu_l.grid(row=3, column=4)
    if cpu_selection == 'Scissor':
        cpu_l = Label(root, image=image_s)
        cpu_l.grid(row=3, column=4)

    if result == cpu_selection:
        res.insert(INSERT, "User Choose : ")
        res.insert(INSERT, result)
        res.insert(INSERT, "\nCPU Choose : ")
        res.insert(INSERT, result)
        res.insert(INSERT, "\n\tTIE")
    else:
        if result == "Rock":
            res.insert(INSERT, "User Choose : ")
            res.insert(INSERT, result)

            if cpu_selection == "Paper":
                res.insert(INSERT, "\nCPU Choose : ")
                res.insert(INSERT, cpu_selection)
                res.insert(INSERT, "\n\tCPU WON")
            if cpu_selection == "Scissor":
                res.insert(INSERT, "\nCPU Choose : ")
                res.insert(INSERT, cpu_selection)
                res.insert(INSERT, "\n\tUSER WON")

        if result == "Paper":
            res.insert(INSERT, "User Choose : ")
            res.insert(INSERT, result)

            if cpu_selection == "Rock":
                res.insert(INSERT, "\nCPU Choose : ")
                res.insert(INSERT, cpu_selection)
                res.insert(INSERT, "\n\tUSER WON")
            if cpu_selection == "Scissor":
                res.insert(INSERT, "\nCPU Choose : ")
                res.insert(INSERT, cpu_selection)
                res.insert(INSERT, "\n\tCPU WON")

        if result == "Scissor":
            res.insert(INSERT, "User Choose : ")
            res.insert(INSERT, result)

            if cpu_selection == "Rock":
                res.insert(INSERT, "\nCPU Choose : ")
                res.insert(INSERT, cpu_selection)
                res.insert(INSERT, "\n\tCPU WON")
            if cpu_selection == "Paper":
                res.insert(INSERT, "\nCPU Choose : ")
                res.insert(INSERT, cpu_selection)
                res.insert(INSERT, "\n\tUSER WON")


# Images
image_r = PhotoImage(file="rock.png")
image_p = PhotoImage(file="paper.png")
image_s = PhotoImage(file="scissor.png")

# Label
title = Label(root, text="ROCK PAPER SCISSOR", font=('Orbitron', 20), fg='purple')
title.grid(row=0, column=3)

vs = Label(root, text="VS", font=('Orbitron', 100), fg='red')
vs.grid(row=3, column=3)

# result
res = Text(root, font=('arial black', 25), bg='black', fg='white', width=25)
res.grid(row=5, column=3)

user_label = Label(root, text="USER Choice : ", font=('Orbitron', 20), fg='blue')
user_label.grid(row=1, column=0, pady=20)

cpu_label = Label(root, text="CPU Choose : ", font=('Orbitron', 20), fg='blue')
cpu_label.grid(row=1, column=4, pady=20)

r_button = Button(root, image=image_r, activebackground='green', command=click_rock)
r_button.grid(row=2, column=0)

p_button = Button(root, image=image_p, activebackground='green', command=click_paper)
p_button.grid(row=3, column=0)

s_button = Button(root, image=image_s, activebackground='green', command=click_scissor)
s_button.grid(row=4, column=0)


root.mainloop()

from tkinter import *
from tkinter import messagebox

import random

root = Tk()
root.title("rock, scissors, paper")
root.geometry('700x600')
root.resizable(1,1)
root.config(bg="green")

blank_image = PhotoImage(file="resources/blank.png")
rock_player = PhotoImage(file="resources/rock_player.png")
rock_player_ado = rock_player.subsample(3,3)



paper_player=PhotoImage(file="resources/paper_player.png")
paper_player_ado = paper_player.subsample(3,3)

scissors_player=PhotoImage(file="resources/scissor_player.png")
scissors_player_ado = scissors_player.subsample(3,3)

rock_computer = PhotoImage(file="resources/rock_computer.png")
paper_computer = PhotoImage(file="resources/paper_computer.png")
scissors_computer = PhotoImage(file="resources/scissor_computer.png")

def rock():
    global player_option
    player_option = 1
    player_image.configure(image = rock_player)
    matchProcceess()


def paper():
    global player_option
    player_option = 2
    player_image.configure(image = paper_player)
    matchProcceess()


def scissors():
    global player_option
    player_option = 3
    player_image.configure(image = scissors_player)
    matchProcceess()

def matchProcceess():
    computer_option = random.randint(1,3)
    if computer_option == 1:
        computer_image.configure(image=rock_computer)
        rockCom()
    elif computer_option == 2:
        computer_image.configure(image=paper_computer)
        paperCom()
    elif computer_option == 3:
        computer_image.configure(image=scissors_computer)
        scissorsCom()


def rockCom():
    if player_option == 1:
        status_label.config(text="Game tie")
    elif player_option ==2:
        status_label.config(text="player win")
    elif player_option==3:
        status_label.config(text="bot win")
    else:
        messagebox.showerror('error',"bad numbers or symbol")



def paperCom():
    if player_option == 1:
        status_label.config(text="bot win")
    elif player_option ==2:
        status_label.config(text="Game tie")
    elif player_option==3:
        status_label.config(text="player win")
    else:
        messagebox.showerror('error',"bad numbers or symbol")


def scissorsCom():
    if player_option == 1:
        status_label.config(text="player win")
    elif player_option ==2:
        status_label.config(text="bot win")
    elif player_option==3:
        status_label.config(text="Game tie")
    else:
        messagebox.showerror('error',"bad numbers or symbol")

def exitApps():
    root.destroy()
    exit()

player_image = Label(root, image=blank_image)
computer_image = Label(root, image=blank_image)
player_label = Label(root, text="player")
player_label.grid(row=1,column=1)
player_label.config(bg="cyan",fg="black", font=("Times New Roman",14,"bold"))


computer_label = Label(root,text="bot")
computer_label.grid(row=1,column=3)
computer_label.config(bg="black",fg="cyan", font=("Times New Roman",14,"bold"))

status_label = Label(root,text="")
status_label.grid(row=3,column=2, padx=25, pady=25)
status_label.config(bg="blue",fg="black", font=("Times New Roman",14,"bold"))

player_image.grid(row=2,column=1,pady=20,padx=30)
computer_image.grid(row=2,column=3,pady=20,padx=30)

rock = Button(root,image=rock_player_ado,command=rock)
paper = Button(root,image=paper_player_ado,command=paper)
scissors = Button(root,image=scissors_player_ado,command=scissors)
button_quit = Button(root, text="Exit", bg='red', fg='white', font=("Times New Roman",16,"bold"), command=exitApps)
rock.grid(row=4,column=1, pady=30)
paper.grid(row=4,column=2, pady=30)
scissors.grid(row=4,column=3, pady=30)
button_quit.grid(row=5,column=2)
root.mainloop()


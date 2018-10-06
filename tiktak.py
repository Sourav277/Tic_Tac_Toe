import PIL
from PIL import Image
import os
import tkinter as t
from tkinter import *
from tkinter import messagebox
root=t.Tk()
root.title(" Tic Tac Toe ")
root.geometry("250x270")
root.tk_setPalette(background='#000000')
root.resizable(0,0)
root.iconbitmap("") #icon .ico
global text
text=True
def press(button):
        global text
        if(text==True and button["text"]==""):
            button["text"]="X"
            text=False
            Check_win()



        elif(text==False and button["text"]==""):
            button["text"]="O"
            text=True
            Check_win()







def Reset():
    button1["text"]=""
    button2["text"]=""
    button3["text"]=""
    button4["text"]=""
    button5["text"]=""
    button6["text"]=""
    button7["text"]=""
    button8["text"]=""
    button9["text"]=""



def  Check_win():
    global X_wins,O_wins

    if(button1["text"]==button2["text"]==button3["text"]):

            if 'X' in button1['text']:
                label=messagebox.showinfo("Tic Tac","X wins")
                X_wins+=1
                labe20=t.Label(root,text="X=")
                labe20.grid(row=6,column=2)
                labe21=t.Label(root,text=X_wins)
                labe21.grid(row=6,column=3)

            if 'O' in button1['text']:
                label=messagebox.showinfo("Tic Tac","O wins")
                O_wins+=1
                label22=t.Label(root,text="O = ")
                label22.grid(row=7,column=2)
                label23=t.Label(root,text=O_wins)
                label23.grid(row=7,column=3)


    if(button4["text"]==button5["text"]==button6["text"]):

            if 'X' in button4['text']:
                label=messagebox.showinfo("Tic Tac","X wins")
                X_wins+=1
                labe20=t.Label(root,text="X = ")
                labe20.grid(row=6,column=2)
                labe21=t.Label(root,text=X_wins)
                labe21.grid(row=6,column=3)

            if 'O' in button4['text']:
                label=messagebox.showinfo("Tic Tac","O wins")
                O_wins+=1
                label22=t.Label(root,text="O = ")
                label22.grid(row=7,column=2)
                label23=t.Label(root,text=O_wins)
                label23.grid(row=7,column=3)

    if(button7["text"]==button8["text"]==button9["text"]):

            if 'X' in button7['text']:
                label=messagebox.showinfo("Tic Tac","X wins")
                X_wins+=1
                labe20=t.Label(root,text="X = ")
                labe20.grid(row=6,column=2)
            labe21=t.Label(root,text=X_wins)
            labe21.grid(row=6,column=3)

            if 'O' in button7['text']:
                label=messagebox.showinfo("Tic Tac","O wins")
                O_wins+=1
                label22=t.Label(root,text="O = ")
                label22.grid(row=7,column=2)
                label23=t.Label(root,text=O_wins)
                label23.grid(row=7,column=3)

    if(button1["text"]==button4["text"]==button7["text"]):

            if 'X' in button1['text']:
                label=messagebox.showinfo("Tic Tac","X wins")
                X_wins+=1
                labe20=t.Label(root,text="X = ")
                labe20.grid(row=6,column=2)
                labe21=t.Label(root,text=X_wins)
                labe21.grid(row=6,column=3)

            if 'O' in button1['text']:
                label=messagebox.showinfo("Tic Tac","O wins")
                O_wins+=1
                label22=t.Label(root,text="O = ")
                label22.grid(row=7,column=2)
                label23=t.Label(root,text=O_wins)
                label23.grid(row=7,column=3)


    if(button2["text"]==button5["text"]==button8["text"]):

            if 'X' in button2['text']:
                label=messagebox.showinfo("Tic Tac","X wins")
                X_wins+=1
                labe20=t.Label(root,text="X = ")
                labe20.grid(row=6,column=2)
                labe21=t.Label(root,text=X_wins)
                labe21.grid(row=6,column=3)

            if 'O' in button2['text']:
                label=messagebox.showinfo("Tic Tac","O wins")
                O_wins+=1
                label22=t.Label(root,text="O = ")
                label22.grid(row=7,column=2)
                label23=t.Label(root,text=O_wins)
                label23.grid(row=7,column=3)

    if(button3["text"]==button6["text"]==button9["text"]):

            if 'X' in button3['text']:
                label=messagebox.showinfo("Tic Tac","X wins")
                X_wins+=1
                labe20=t.Label(root,text="X = ")
                labe20.grid(row=6,column=2)
                labe21=t.Label(root,text=X_wins)
                labe21.grid(row=6,column=3)

            if 'O' in button3['text']:
                label=messagebox.showinfo("Tic Tac","O wins")
                O_wins+=1
                label22=t.Label(root,text="O = ")
                label22.grid(row=7,column=2)
                label23=t.Label(root,text=O_wins)
                label23.grid(row=7,column=3)

    if(button1["text"]==button5["text"]==button9["text"]):

            if 'X' in button1['text']:
                label=messagebox.showinfo("Tic Tac","X wins")
                X_wins+=1
                labe20=t.Label(root,text="X = ")
                labe20.grid(row=6,column=2)
                labe21=t.Label(root,text=X_wins)
                labe21.grid(row=6,column=3)

            if 'O' in button1['text']:
                label=messagebox.showinfo("Tic Tac","O wins")
                O_wins+=1
                label22=t.Label(root,text="O = ")
                label22.grid(row=7,column=2)
                label23=t.Label(root,text=O_wins)
                label23.grid(row=7,column=3)

    if(button3["text"]==button5["text"]==button7["text"]):
            if 'X' in button3['text']:
                label=messagebox.showinfo("Tic Tac","X wins")
                X_wins+=1
                labe20=t.Label(root,text="X = ")
                labe20.grid(row=6,column=2)
                labe21=t.Label(root,text=X_wins)
                labe21.grid(row=6,column=3)

            if 'O' in button3['text']:
                label=messagebox.showinfo("Tic Tac","O wins")
                O_wins+=1
                label22=t.Label(root,text="O = ")
                label22.grid(row=7,column=2)
                label23=t.Label(root,text=O_wins)
                label23.grid(row=7,column=3)


def exit():
    root.destroy()


global X_wins,Y_wins
X_wins=0
O_wins=0

label22=t.Label(root,text="O = ")
label22.grid(row=7,column=2)
label23=t.Label(root,text=O_wins)
label23.grid(row=7,column=3)

label20=t.Label(root,text="X = ")
label20.grid(row=6,column=2)
label21=t.Label(root,text=X_wins)
label21.grid(row=6,column=3)

label30=t.Label(root,text="Score : ")
label30.grid(row=6,column=1)

label1=t.Label(root,text="Welcome",font=("Arial 10 bold italic "))
label1.grid(row=0,column=1,padx=0,pady=0)

label2=t.Label(root,text="To Tic",font=("Arial 10 bold italic"))
label2.grid(row=0,column=2,padx=0,pady=0)

label3=t.Label(root,text="Tac Toe!",font=("Arial 10 bold italic"))
label3.grid(row=0,column=3,padx=0,pady=0)
button1=t.Button(root,text="",font=('Arial 10 bold'),width=5,height=1,bg='#0e1111',command=lambda :press(button1))
button1.grid(row=1,column=1,padx=5,pady=5)

button2=t.Button(root,text="",font=('Arial 10 bold'),width=5,height=1,bg='#0e1111',command=lambda :press(button2))
button2.grid(row=1,column=2,padx=5,pady=5)

button3=t.Button(root,text="",font=('Arial 10 bold'),width=5,height=1,bg='#0e1111',command=lambda :press(button3))
button3.grid(row=1,column=3,padx=5,pady=5)


button4=t.Button(root,text="",font=('Arial 10 bold'),width=5,height=1,bg='#0e1111',command=lambda :press(button4))
button4.grid(row=2,column=1,padx=5,pady=5)

button5=t.Button(root,text="",font=('Arial 10 bold'),width=5,height=1,bg='#0e1111',command=lambda :press(button5))
button5.grid(row=2,column=2,padx=5,pady=5)

button6=t.Button(root,text="",font=('Arial 10 bold'),width=5,height=1,bg='#0e1111',command=lambda :press(button6))
button6.grid(row=2,column=3,padx=5,pady=5)

button7=t.Button(root,text="",font=('Arial 10 bold'),width=5,height=1,bg='#0e1111',command=lambda :press(button7))
button7.grid(row=3,column=1,padx=5,pady=5)

button8=t.Button(root,text="",font=('Arial 10 bold'),width=5,height=1,bg='#0e1111',command=lambda :press(button8))
button8.grid(row=3,column=2,padx=5,pady=5)
button9=t.Button(root,text="",font=('Arial 10 bold'),width=5,height=1,bg='#0e1111',command=lambda :press(button9))
button9.grid(row=3,column=3,padx=5,pady=5)


button10=t.Button(root,text='RESET',bg='#0e1111',fg='red',command=lambda:Reset())
button10.grid(row=4,columnspan="3",sticky=t.E+t.W,padx=10,pady=5)


button11=t.Button(root,text='EXIT',bg='#0e1111',fg='red',command=lambda:exit())
button11.grid(row=5,columnspan="3",sticky=t.E+t.W,padx=10,pady=5)
root.mainloop()

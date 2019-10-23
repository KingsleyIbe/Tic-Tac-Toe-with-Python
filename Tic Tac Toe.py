#first, import tkinker liberary, that will enable us build our GUI.
from tkinter import *
    
from tkinter import messagebox

game = Tk()
game.title("Tic Tac Toe")
game.geometry("1100x600+0+0")
game.configure(background ='Cadet Blue')

Tops = Frame(game, bg ='Cadet Blue', pady =2, width =1350, height =100, relief =RIDGE)
Tops.grid(row=0, column=0)

lblTitle = Label(Tops, font=('arial',22,'bold'), text="Biatech Tic Tac Toe", bd=21,bg='Cadet Blue', fg='Cornsilk',justify=CENTER)
lblTitle.grid(row=0, column=0)

MainFrame = Frame(game, bg ='Cadet Blue', pady =2, width =1350, height=100, relief =RIDGE)
MainFrame.grid(row=1, column=0)

LeftFrame = Frame(MainFrame, bd=10, width =750, height=500, pady=2, padx=10, bg="Cadet Blue", relief=RIDGE)
LeftFrame.pack(side=LEFT)

RightFrame = Frame(MainFrame, bd=10, width =560, height=500, pady=2, padx=10, bg="Cadet Blue")
RightFrame.pack(side=RIGHT)

RightFrame1 = Frame(RightFrame, bd=10, width =560, height=500, pady=2, padx=10, bg="Cadet Blue")
RightFrame1.grid(row=0, column=0)

RightFrame2 = Frame(RightFrame, bd=10, width =560, height=500, pady=2, padx=10, bg="Cadet Blue")
RightFrame2.grid(row=1, column=0)


PlayerX=IntVar()
PlayerO=IntVar()
Turn = StringVar()

global winner
winner = None

def clear_score():
    
    PlayerX.set(0)
    PlayerO.set(0)
Turn.set(" ")

buttons = StringVar()
click = True

def checker(buttons):
    global click
    if buttons["text"] == " " and click == True:
        buttons["text"] = "X"
        click = False
        scorekeeper()
        myturn()
        
        
    elif buttons["text"] == " " and click == False:
        buttons["text"] = "O"
        click = True
        scorekeeper()
        myturn()
        
def myturn():
    if (click == False):
        Turn = "X's Turn"
        print(Turn)
    else:
        Turn = "O's Turn"
        print(Turn)
        
def scorekeeper():
       
    if(b_one["text"]=="X" and b_two["text"]=="X" and b_three["text"]=="X"):
        b_one.configure(background ="red")
        b_two.configure(background ="red")
        b_three.configure(background ="red")
        n = float(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        messagebox.showinfo("Winner X","You have just WON the Game!")
        

    if(b_one["text"]=="O" and b_two["text"]=="O" and b_three["text"]=="O"):
        b_one.configure(background ="Cadet blue")
        b_two.configure(background ="Cadet blue")
        b_three.configure(background ="Cadet blue")
        n = float(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        messagebox.showinfo("Winner O", "You have just won the Game!")
        
    if(b_four["text"]=="X" and b_five["text"]=="X" and b_six["text"]=="X"):
        b_four.configure(background ="powder blue")
        b_five.configure(background ="powder blue")
        b_six.configure(background ="powder blue")
        n = float(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        messagebox.showinfo("Winner X", "You have just won the Game!")

    if(b_seven["text"]=="X" and b_eight["text"]=="X" and b_nine["text"]=="X"):
        b_seven.configure(background ="gold")
        b_eight.configure(background ="gold")
        b_nine.configure(background ="gold")
        n = float(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        messagebox.showinfo("Winner X", "You have just won the Game!")

    if(b_one["text"]=="X" and b_five["text"]=="X" and b_nine["text"]=="X"):
        b_one.configure(background ="white")
        b_five.configure(background ="white")
        b_nine.configure(background ="white")
        n = float(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        messagebox.showinfo("Winner X", "You have just won the Game!")

    if(b_three["text"]=="X" and b_five["text"]=="X" and b_seven["text"]=="X"):
        b_three.configure(background ="brown")
        b_five.configure(background ="brown")
        b_seven.configure(background ="brown")
        n = float(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        messagebox.showinfo("Winner X", "You have just won the Game!")
        

    if(b_one["text"]=="X" and b_four["text"]=="X" and b_seven["text"]=="X"):
        b_one.configure(background ="pink")
        b_four.configure(background ="pink")
        b_seven.configure(background ="pink")
        n = float(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        messagebox.showinfo("Winner X", "You have just won the Game!")
    

    if(b_two["text"]=="X" and b_five["text"]=="X" and b_eight["text"]=="X"):
        b_two.configure(background ="orange")
        b_five.configure(background ="orange")
        b_eight.configure(background ="orange")
        n = float(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        messagebox.showinfo("Winner X", "You have just won the Game!")

    if(b_three["text"]=="X" and b_six["text"]=="X" and b_nine["text"]=="X"):
        b_three.configure(background ="sky blue")
        b_six.configure(background ="sky blue")
        b_nine.configure(background ="sky blue")
        n = float(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        messagebox.showinfo("Winner X", "You have just won the Game!")


    if(b_four["text"]=="O" and b_five["text"]=="O" and b_six["text"]=="O"):
        b_four.configure(background ="blue")
        b_five.configure(background ="blue")
        b_six.configure(background ="blue")
        n = float(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        messagebox.showinfo("Winner O", "You have just won the Game!")


    if(b_seven["text"]=="O" and b_eight["text"]=="O" and b_nine["text"]=="O"):
        b_seven.configure(background ="powder blue")
        b_eight.configure(background ="powder blue")
        b_nine.configure(background ="powder blue")
        n = float(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        messagebox.showinfo("Winner O", "You have just won the Game!")

    if(b_one["text"]=="O" and b_five["text"]=="O" and b_nine["text"]=="O"):
        b_one.configure(background ="purple")
        b_five.configure(background ="purple")
        b_nine.configure(background ="purple")
        n = float(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        messagebox.showinfo("Winner O", "You have just won the Game!")

    if(b_three["text"]=="O" and b_five["text"]=="O" and b_seven["text"]=="O"):
        b_three.configure(background ="silver")
        b_five.configure(background ="silver")
        b_seven.configure(background ="silver")
        n = float(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        messagebox.showinfo("Winner O", "You have just won the Game!")

    if(b_one["text"]=="O" and b_four["text"]=="O" and b_seven["text"]=="O"):
        b_one.configure(background ="yellow")
        b_four.configure(background ="yellow")
        b_seven.configure(background ="yellow")
        n = float(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        messagebox.showinfo("Winner O", "You have just won the Game!")

    if(b_two["text"]=="O" and b_five["text"]=="O" and b_eight["text"]=="O"):
        b_two.configure(background ="green")
        b_five.configure(background ="green")
        b_eight.configure(background ="green")
        n = float(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        messagebox.showinfo("Winner O", "You have just won the Game!")

    if(b_three["text"]=="O" and b_six["text"]=="O" and b_nine["text"]=="O"):
        b_three.configure(background ="powder blue")
        b_six.configure(background ="powder blue")
        b_nine.configure(background ="powder blue")
        n = float(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        messagebox.showinfo("Winner O", "You have just won the Game!")
        
        
    if(b_two["text"]=="O" and  b_four["text"]=="O" and b_seven["text"]=="O" and b_nine["text"]== "O" and b_one["text"]=="X" and b_three["text"]=="X" and b_five["text"]=="X" and b_six["text"]=="X" and b_eight["text"]=="X"or
        b_one["text"]=="O" and b_four["text"]=="O" and b_five["text"]=="O" and b_seven["text"]=="O" and b_nine["text"]=="O" and b_one["text"]=="X" and b_three["text"]=="X" and b_six["text"]=="X" and b_eight["text"]=="X" or
       b_two["text"]=="O" and b_five["text"]=="O" and b_six["text"]=="O" and b_seven["text"]=="O" and b_one["text"]=="X" and b_three["text"]=="X" and b_four["text"]=="X" and b_eight["text"]=="X" and b_nine["text"]=="X" or
       b_one["text"]=="O" and b_three["text"]=="O" and b_five["text"]=="O" and b_eight["text"]=="O" and b_two["text"]=="X" and b_four["text"]=="X" and b_six["text"]=="X" and b_seven["text"]=="X" and b_nine["text"]=="X" or
       b_one["text"]=="O" and b_three["text"]=="O" and b_six["text"]=="O" and b_eight["text"]=="O" and b_two["text"]=="X" and b_five["text"]=="X" and b_four["text"]=="X" and b_seven["text"]=="X" and b_nine["text"]=="X" or
       b_two["text"]=="O" and b_four["text"]=="O" and b_five["text"]=="O" and b_nine["text"]=="O" and b_one["text"]=="X" and b_three["text"]=="X" and b_six["text"]=="X" and b_eight["text"]=="X" and b_seven["text"]=="X" or
       b_one["text"]=="O" and b_six["text"]=="O" and b_seven["text"]=="O" and b_eight["text"]=="O" and b_two["text"]=="X" and b_three["text"]=="X" and b_four["text"]=="X" and b_five["text"]=="X" and b_nine["text"]=="X" or
       b_two["text"]=="O" and b_three["text"]=="O" and b_four["text"]=="O" and b_seven["text"]=="O" and b_nine["text"]=="O" and b_one["text"]=="X" and b_five["text"]=="X" and b_six["text"]=="X" and b_eight["text"]=="X" or
       b_one["text"]=="O" and b_two["text"]=="O" and b_six["text"]=="O" and b_seven["text"]=="O" and b_eight["text"]=="X" and b_three["text"]=="X" and b_four["text"]=="X" and b_five["text"]=="X" and b_nine["text"]=="X" or
       b_three["text"]=="O" and b_two["text"]=="O" and b_four["text"]=="O" and b_eight["text"]=="O" and b_nine["text"]=="O" and b_one["text"]=="X" and b_five["text"]=="X" and b_six["text"]=="X" and b_seven["text"]=="X" or
       b_one["text"]=="O" and b_three["text"]=="O" and b_six["text"]=="O" and b_seven["text"]=="O" and b_eight["text"]=="X" and b_two["text"]=="X" and b_four["text"]=="X" and b_five["text"]=="X" and b_nine["text"]=="X"):

   # else:
     #   winner = None   
       messagebox.showinfo("Draw Game")
       reset()
        
        
def reset():
    b_one['text']=" "
    b_two['text']=" "
    b_three['text']=" "
    b_four['text']=" "
    b_five['text']=" "
    b_six['text']=" "
    b_seven['text']=" "
    b_eight['text']=" "
    b_nine['text']=" "

    b_one.configure(backgroud ="gainsboro")
    b_two.configure(backgroud ="gainsboro")
    b_three.configure(backgroud ="gainsboro")
    b_four.configure(backgroud ="gainsboro")
    b_five.configure(backgroud ="gainsboro")
    b_six.configure(backgroud ="gainsboro")
    b_seven.configure(backgroud ="gainsboro")
    b_eight.configure(backgroud ="gainsboro")
    b_nine.configure(backgroud ="gainsboro")


def NewGame():
    
    reset()
    clear_score()
    
   
                    
lblPlayerX =Label(RightFrame1, font=('arial',22,'bold'), text="Player X:",padx=10, bg="Cadet Blue")
lblPlayerX.grid(row=0, column=0,sticky=W)
txtPlayerX=Entry(RightFrame1, font=('arial',22,'bold'),bd=2,fg="black",textvariable=PlayerX, width=7,
                 justify=LEFT).grid(row=0,column=1)

lblPlayerO =Label(RightFrame1, font=('arial',22,'bold'), text="Player O:",padx=10, bg="Cadet Blue")
lblPlayerO.grid(row=1, column=0,sticky=W)
txtPlayerO=Entry(RightFrame1, font=('arial',22,'bold'),bd=2,fg="black",textvariable=PlayerO, width=7,
                 justify=LEFT).grid(row=1,column=1)

lblPlayerTurn =Label(RightFrame1, font=('arial',22,'bold'), text="Whose Turn?",padx=10, bg="Cadet Blue")
lblPlayerTurn.grid(row=2, column=0,sticky=W)
txtPlayerTurn=Entry(RightFrame1, font=('arial',14,'bold'),bd=2,fg="black",textvariable=Turn, width=16,
                 justify=LEFT).grid(row=2,column=1)


btnReset = Button(RightFrame2, text="Reset",font=('Times 18 bold'), height = 2, width=8, bg='gainsboro', command = reset)
btnReset.grid(row=0, column=0, pady=40)


btnNewGame = Button(RightFrame2, text="New Game",font=('Times 18 bold'), height = 2, width=8, bg='gainsboro', command = NewGame)
btnNewGame.grid(row=1, column=0, padx=40)

b_one=Button(LeftFrame, text=" ",font=('Times 26 bold'), height = 3, width=8, bg='gainsboro', command=lambda:checker(b_one))
b_one.grid(row=1, column=0, sticky = S+N+E+W)

b_two = Button(LeftFrame, text=" ",font=('Times 26 bold'), height = 3, width=8, bg='gainsboro', command=lambda:checker(b_two))
b_two.grid(row=1, column=1, sticky = S+N+E+W)

b_three = Button(LeftFrame, text=" ",font=('Times 26 bold'), height = 3, width=8, bg='gainsboro', command=lambda:checker(b_three))
b_three.grid(row=1, column=2, sticky = S+N+E+W)

b_four = Button(LeftFrame, text=" ",font=('Times 26 bold'), height = 3, width=8, bg='gainsboro', command=lambda:checker(b_four))
b_four.grid(row=2, column=0, sticky = S+N+E+W)

b_five = Button(LeftFrame, text=" ",font=('Times 26 bold'), height = 3, width=8, bg='gainsboro', command=lambda:checker(b_five))
b_five.grid(row=2, column=1, sticky = S+N+E+W)

b_six = Button(LeftFrame, text=" ",font=('Times 26 bold'), height = 3, width=8, bg='gainsboro', command=lambda:checker(b_six))
b_six.grid(row=2, column=2, sticky = S+N+E+W)

b_seven = Button(LeftFrame, text=" ",font=('Times 26 bold'), height = 3, width=8, bg='gainsboro', command=lambda:checker(b_seven))
b_seven.grid(row=3, column=0, sticky = S+N+E+W)

b_eight = Button(LeftFrame, text=" ",font=('Times 26 bold'), height = 3, width=8, bg='gainsboro', command=lambda:checker(b_eight))
b_eight.grid(row=3, column=1, sticky = S+N+E+W)

b_nine = Button(LeftFrame, text=" ",font=('Times 26 bold'), height = 3, width=8, bg='gainsboro', command=lambda:checker(b_nine))
b_nine.grid(row=3, column=2, sticky = S+N+E+W)

game.mainloop()

checker(b_one)



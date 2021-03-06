import tkinter.messagebox
from tkinter import *
import socket
########## Draw Frame ############
root =Tk()
##root.geometry("1287x750+300+50")
root.title("GAME OX")
w=1287
h=740
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
     # calculate position x, y
x = (ws/2) - (w/2)    
y = (hs/2) - (h/2)-50

root.geometry('%dx%d+%d+%d' % (w,h,x, y))
root.configure(background = '#2b5797')
##สีเหลือง #edb44e
##แดง #B22222
##สีน้ำเงิน #2b5797

### GET HOST IP ###
host_name = socket.gethostname() 
host_ip = socket.gethostbyname(host_name)
def text_change_offline():
    lblTitle["text"] = 'Game OX (Offline)'
    lblPlayerX["text"] = 'Player1  X'
    lblPlayerO["text"] = 'Player2  O'
    lblIP.grid_forget()
    entryPlayer.grid_forget()
    btnConnect.grid_forget()
    lblIPHost.grid_forget()
    btnConnect1.grid_forget()
    entryHost.grid_forget()
    btnHost.grid_forget()
    btnPvP.grid_forget()

def text_change_online():
    lblTitle["text"] = 'Game OX (Online)'
    lblPlayerX["text"] = 'H or P  X'
    lblPlayerO["text"] = 'Player  O'
    btnHost.grid(row=0,column=0)
    btnPvP.grid(row=0,column=1)
    MainFrame.grid(row=3, column=0)
    
def click_host():
    global host_ip
    lblTitle["text"] = 'Game OX (Online)'
    lblPlayerX["text"] = 'Host    X'
    lblPlayerO["text"] = 'Player  O'
    lblIPHost.grid(row=2,column=0)
    entryHost.grid(row=2,column=1,padx=5)
    btnConnect1.grid(row=2,column=2)
    ### Hide ##
    lblIP.grid_forget()
    entryPlayer.grid_forget()
    btnConnect.grid_forget()
    #btnHost.grid_forget()
    # btnPvP.grid_forget()

def click_player():
    lblTitle["text"] = 'Game OX (Online)'
    lblPlayerX["text"] = 'Host   X'
    lblPlayerO["text"] = 'Player O'
    lblIP.grid(row=1,column=0)
    entryPlayer.grid(row=1,column=1)
    btnConnect.grid(row=1,column=2,padx=5)
    ### Hide ####
    lblIPHost.grid_forget()
    entryHost.grid_forget()
    btnConnect1.grid_forget()
    #btnHost.grid_forget()
    #btnPvP.grid_forget()
    
TopTop = Frame(root, bg = '#2b5797', pady=2,width=1350, height=100, relief=RIDGE)
TopTop.grid(row=0, column=0)
lblTitle = Label(TopTop,font=('arial',30,'bold'), text="Game OX", bd=21,bg="#2b5797",fg="Cornsilk",justify=CENTER)
lblTitle.grid(row=0,column=0)

Tops = Frame(root, bg = '#2b5797', pady=2,width=1350, height=100, relief=RIDGE)
Tops.grid(row=1, column=0)
# ####offline#####
# btnHvP = Button(Tops,text="Offline", font=('Times 26 bold'), height = 1, width=10,bg="#edb44e",command=text_change_offline)
# btnHvP.grid(row=1,column=0,pady=10,padx=5)
# ##online btn###
# btnPvP = Button(Tops,text="Online", font=('Times 26 bold'), height = 1, width=10,bg="#edb44e",command=text_change_online)
# btnPvP.grid(row=1,column=1,pady=10)
#### host or player ####
btnHost = Button(Tops,text="Host", font=('Times 15 bold'), height = 1, width=10,bg="#edb44e",command=click_host)
btnHost.grid(row=0,column=0)
btnHost.grid_forget()
btnPvP = Button(Tops,text="Player", font=('Times 15 bold'), height = 1, width=10,bg="#edb44e",command=click_player)
btnPvP.grid(row=0,column=1)
btnPvP.grid_forget()

#### IP player#####  
BottomFrame = Frame(root, pady=2,width=1350, height=100, relief=RIDGE,bg ='#2b5797')
BottomFrame.grid(row=2, column=0)
lblIP = Label(BottomFrame,font=('arial',12,'bold'), text="IP", bd=21,bg="#B22222",fg="Cornsilk",justify=CENTER)
lblIP.grid(row=1,column=0)
lblIP.grid_forget()
entryPlayer = Entry(BottomFrame,font=('arial',12,'bold'),textvariable="", bd=21,bg="#B22222",fg="Cornsilk",justify=CENTER)
entryPlayer.grid(row=1,column=1)
entryPlayer.grid_forget()
btnConnect = Button(BottomFrame,text="Player", font=('Times 22 bold'), height = 1, width=20,bg="#edb44e")
btnConnect.grid(row=1,column=2,padx=5)
btnConnect.grid_forget()
######Show IP Host ######
lblIPHost = Label(BottomFrame,font=('arial',12,'bold'), text="IP", bd=21,bg="#B22222",fg="Cornsilk",justify=CENTER)
lblIPHost.grid(row=2,column=0)
lblIPHost.grid_forget()
entryHost = Label(BottomFrame,font=('arial',12,'bold'), text=str(host_ip),bd=21,bg="#B22222",fg="Cornsilk",justify=CENTER)
entryHost.grid(row=2,column=1)
entryHost.grid_forget()
btnConnect1 = Button(BottomFrame,text="Host", font=('Times 22 bold'), height = 1, width=20,bg="#edb44e")
btnConnect1.grid(row=2,column=2,padx=5)
btnConnect1.grid_forget()

##### middle ####
MainFrame = Frame(root, pady=2,width=20, height=200, relief=RIDGE,bg ='#B22222')
MainFrame.grid(row=2, column=0)

LeftFrame = Frame(MainFrame , bd=10, width=200, height=200,pady=5,padx=10,bg="#2b5797" , relief=RIDGE)
LeftFrame.pack(side=LEFT,expand = True, fill = BOTH)

RightFrame = Frame(MainFrame , bd=10, width=200, height=300,padx=10,pady=20,bg="#2b5797" , relief=RIDGE)
RightFrame.pack(side=RIGHT,expand = True, fill = BOTH)

RightFrame1 = Frame(RightFrame , bd=10, width=200, height=200,padx=10,pady=2,bg="#edb44e" , relief=RIDGE)
RightFrame1.grid(row=0,column=0)
RightFrame1.grid_columnconfigure(0, weight=1)

RightFrame2 = Frame(RightFrame , bd=10, width=200, height=200,padx=10,pady=2,bg="#2b5797" , relief=RIDGE)
RightFrame2.grid(row=1,column=0,pady=10)

RightFrame3 = Frame(RightFrame , bd=10, width=200, height=200,padx=10,pady=2,bg="#2b5797" , relief=RIDGE)
RightFrame3.grid(row=2,column=0,pady=10)

RightFrame4 = Frame(RightFrame , bd=10, width=200, height=200,padx=10,pady=2,bg="#2b5797" , relief=RIDGE)
RightFrame4.grid(row=3,column=0,pady=20)


##### set player #####
PlayerX=IntVar()
PlayerO=IntVar()

PlayerX.set(0)
PlayerO.set(0)
    
lblPlayerX = Label(RightFrame1,font=('arial',26,'bold'), text="Player1  X", padx=2,pady=2,bg="#edb44e")
lblPlayerX.grid(row=0,column=0,sticky=W)
txtPlayerX=Label(RightFrame1,font=('arial',26,'bold'), bd=2,fg="black",textvariable= PlayerX, width=14,
                 justify=CENTER).grid(row=0,column=1)


lblPlayerO = Label(RightFrame1,font=('arial',26,'bold'), text="Player2  O", padx=2,pady=2,bg="#edb44e")
lblPlayerO.grid(row=1,column=0,sticky=W)
txtPlayerO=Label(RightFrame1,font=('arial',26,'bold'), bd=2,fg="black",textvariable= PlayerO, width=14,
                 justify=CENTER).grid(row=1,column=1)


##### set click O X && reset new game ####
buttons = StringVar()
click = True
draw = 0

def checker(buttons): 
    global click
    if buttons["text"] == " " and click == True:
        buttons["text"] = "X"
        click = False
        scorekeeper()
    elif buttons["text"] == " " and click == False:
        buttons["text"] = "O"
        click = True
        scorekeeper()
        
def scorekeeper():
    global draw
    draw +=1
    print("Draw point: ",draw)
    if(button1["text"]=="X" and button2["text"]=="X" and button3["text"]=="X"):
        button1.configure(background="powder blue")
        button2.configure(background="powder blue")
        button3.configure(background="powder blue")
        n = float(PlayerX.get())
        score = (n+1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X", "You Won")
        draw = 0
    
    if(button4["text"]=="X" and button5["text"]=="X" and button6["text"]=="X"):
        button4.configure(background="Red")
        button5.configure(background="Red")
        button6.configure(background="Red")
        n = float(PlayerX.get())
        score = (n+1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X", "You Won")
        draw = 0
        
    if(button7["text"]=="X" and button8["text"]=="X" and button9["text"]=="X"):
        button7.configure(background="Cadet blue")
        button8.configure(background="Cadet blue")
        button9.configure(background="Cadet blue")
        n = float(PlayerX.get())
        score = (n+1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X", "You Won")
        draw = 0
    
    if(button3["text"]=="X" and button5["text"]=="X" and button7["text"]=="X"):
        button3.configure(background="Red")
        button5.configure(background="Red")
        button7.configure(background="Red")
        n = float(PlayerX.get())
        score = (n+1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X", "You Won")
        draw = 0
    
    if(button1["text"]=="X" and button5["text"]=="X" and button9["text"]=="X"):
        button1.configure(background="Cadet blue")
        button5.configure(background="Cadet blue")
        button9.configure(background="Cadet blue")
        n = float(PlayerX.get())
        score = (n+1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X", "You Won")
        draw = 0
    
    if(button1["text"]=="X" and button4["text"]=="X" and button7["text"]=="X"):
        button1.configure(background="Red")
        button4.configure(background="Red")
        button7.configure(background="Red")
        n = float(PlayerX.get())
        score = (n+1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X", "You Won")
        draw = 0
    
    if(button2["text"]=="X" and button5["text"]=="X" and button8["text"]=="X"):
        button2.configure(background="Cadet blue")
        button5.configure(background="Cadet blue")
        button8.configure(background="Cadet blue")
        n = float(PlayerX.get())
        score = (n+1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X", "You Won")
        draw = 0
    
    if(button3["text"]=="X" and button6["text"]=="X" and button9["text"]=="X"):
        button3.configure(background="Red")
        button6.configure(background="Red")
        button9.configure(background="Red")
        n = float(PlayerX.get())
        score = (n+1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X", "You Won")
        draw = 0
        
    
    #### O side ###
    if(button1["text"]=="O" and button2["text"]=="O" and button3["text"]=="O"):
        button1.configure(background="powder blue")
        button2.configure(background="powder blue")
        button3.configure(background="powder blue")
        n = float(PlayerO.get())
        score = (n+1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Winner O", "You Won")
        draw = 0
    
    if(button4["text"]=="O" and button5["text"]=="O" and button6["text"]=="O"):
        button4.configure(background="Red")
        button5.configure(background="Red")
        button6.configure(background="Red")
        n = float(PlayerO.get())
        score = (n+1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Winner O", "You Won")
        draw = 0
        
    if(button7["text"]=="O" and button8["text"]=="O" and button9["text"]=="O"):
        button7.configure(background="Cadet blue")
        button8.configure(background="Cadet blue")
        button9.configure(background="Cadet blue")
        n = float(PlayerO.get())
        score = (n+1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Winner O", "You Won")
        draw = 0
        
    if(button3["text"]=="O" and button5["text"]=="O" and button7["text"]=="O"):
        button3.configure(background="Red")
        button5.configure(background="Red")
        button7.configure(background="Red")
        n = float(PlayerO.get())
        score = (n+1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Winner O", "You Won")
        draw = 0
        
    if(button1["text"]=="O" and button5["text"]=="O" and button9["text"]=="O"):
        button1.configure(background="Cadet blue")
        button5.configure(background="Cadet blue")
        button9.configure(background="Cadet blue")
        n = float(PlayerO.get())
        score = (n+1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Winner O", "You Won")
        draw = 0
        
    if(button1["text"]=="O" and button4["text"]=="O" and button7["text"]=="O"):
        button1.configure(background="Red")
        button4.configure(background="Red")
        button7.configure(background="Red")
        n = float(PlayerO.get())
        score = (n+1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Winner O", "You Won")
        draw = 0
        
    if(button2["text"]=="O" and button5["text"]=="O" and button8["text"]=="O"):
        button2.configure(background="Cadet blue")
        button5.configure(background="Cadet blue")
        button8.configure(background="Cadet blue")
        n = float(PlayerO.get())
        score = (n+1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Winner O", "You Won")
        draw = 0
    
    if(button3["text"]=="O" and button6["text"]=="O" and button9["text"]=="O"):
        button3.configure(background="Red")
        button6.configure(background="Red")
        button9.configure(background="Red")
        n = float(PlayerO.get())
        score = (n+1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Winner O", "You Won")
        draw = 0
    
    if(draw==9):
        tkinter.messagebox.showinfo("Draw !!!!","Click OK to reset")
        reset()
        draw = 0
    
    
    
        
def reset():
    global draw
    draw = 0
    button1['text']=" "
    button2['text']=" "
    button3['text']=" "
    button4['text']=" "
    button5['text']=" "
    button6['text']=" "
    button7['text']=" "
    button8['text']=" "
    button9['text']=" "
    
    button1.configure(background="#edb44e")
    button2.configure(background="#edb44e")
    button3.configure(background="#edb44e")
    button4.configure(background="#edb44e")
    button5.configure(background="#edb44e")
    button6.configure(background="#edb44e")
    button7.configure(background="#edb44e")
    button8.configure(background="#edb44e")
    button9.configure(background="#edb44e")

def enable_button():
    button1['state'] = 'normal'
    button2['state'] = 'normal'
    button3['state'] = 'normal'
    button4['state'] = 'normal'
    button5['state'] = 'normal'
    button6['state'] = 'normal'
    button7['state'] = 'normal'
    button8['state'] = 'normal'
    button9['state'] = 'normal'
    
    
def NewGame_Online():
    reset()
    PlayerX.set(0)
    PlayerO.set(0)
    text_change_online()
    enable_button()

def NewGame_Offline():
    reset()
    PlayerX.set(0)
    PlayerO.set(0)
    text_change_offline()
    enable_button()

### neew game btn ####
btnNewGameOff = Button(RightFrame2, text="New Game in Offline Mode", font=('Times 15 bold'), height = 1, width=20,bg="#B22222",fg="white", command=NewGame_Offline)
btnNewGameOff.grid(row=0,column=0)
btnNewGameOn = Button(RightFrame2, text="New Game in Online Mode", font=('Times 15 bold'), height = 1, width=20,bg="DeepPink1",fg="white", command=NewGame_Online)
btnNewGameOn.grid(row=1,column=0,pady=5)

btnReset = Button(RightFrame3, text="Reset", font=('Times 15 bold'), height = 1, width=20,bg="SpringGreen4" ,command=reset,fg="white")
btnReset.grid(row=0,column=0)
############# Draw 3x3 button ######
button1 = Button(LeftFrame, text=" ", font=('Times 26 bold'),state=DISABLED, height = 3, width=8,bg='#edb44e', command=lambda:checker(button1))
button1.grid(row=1,column=0, stick = S+N+E+W)

button2 = Button(LeftFrame, text=" ", font=('Times 26 bold'),state=DISABLED, height = 3, width=8,bg='#edb44e', command=lambda:checker(button2))
button2.grid(row=1,column=1, stick = S+N+E+W)

button3 = Button(LeftFrame, text=" ", font=('Times 26 bold'),state=DISABLED, height = 3, width=8,bg='#edb44e', command=lambda:checker(button3))
button3.grid(row=1,column=2, stick = S+N+E+W)

button4 = Button(LeftFrame, text=" ", font=('Times 26 bold'),state=DISABLED, height = 3, width=8,bg='#edb44e', command=lambda:checker(button4))
button4.grid(row=2,column=0, stick = S+N+E+W)

button5 = Button(LeftFrame, text=" ", font=('Times 26 bold'),state=DISABLED, height = 3, width=8,bg='#edb44e', command=lambda:checker(button5))
button5.grid(row=2,column=1, stick = S+N+E+W)

button6 = Button(LeftFrame, text=" ", font=('Times 26 bold'),state=DISABLED, height = 3, width=8,bg='#edb44e', command=lambda:checker(button6))
button6.grid(row=2,column=2, stick = S+N+E+W)

button7 = Button(LeftFrame, text=" ", font=('Times 26 bold'),state=DISABLED, height = 3, width=8,bg='#edb44e', command=lambda:checker(button7))
button7.grid(row=3,column=0, stick = S+N+E+W)

button8 = Button(LeftFrame, text=" ", font=('Times 26 bold'),state=DISABLED, height = 3, width=8,bg='#edb44e', command=lambda:checker(button8))
button8.grid(row=3,column=1, stick = S+N+E+W)

button9 = Button(LeftFrame, text=" ", font=('Times 26 bold'),state=DISABLED, height = 3, width=8,bg='#edb44e', command=lambda:checker(button9))
button9.grid(row=3,column=2, stick = S+N+E+W)


##### Hall of Frame's Window#####
def openhof():
    #window = Toplevel(root)
    window =Tk()
    window.geometry("900x400+500+300")
    window.title("Hall of Fame")
    window.configure(background = '#2b5797')
    Topfr = Frame(window, bg = '#2b5797',width=100, height=50)
    Topfr.pack(side=TOP)
    MainFrame = Frame(window, bg = '#B22222',width=200, height=500)
    MainFrame.pack(side=TOP)
    #### Top Frame #####
    TopHFrame = Frame(MainFrame, bg = 'black',width=200, height=500)
    TopHFrame.pack(side=TOP)
    lblTitle = Label(TopHFrame,font=('arial',50,'bold'), text="Hall of Fame", bd=15,bg="#B22222",fg="Cornsilk",justify=CENTER)
    lblTitle.grid(row=0,column=0)
    #### Middle #####
    MiddleHFrame = Frame(MainFrame, bg = '#B22222',width=200, height=500)
    MiddleHFrame.pack(side=TOP)
    
    MHFrame = Frame(MiddleHFrame, bg = 'white',width=200, height=500)
    MHFrame.pack(side=TOP)
    
    MHFrameLeft = Frame(MHFrame, bg = 'black',width=200, height=500)
    MHFrameLeft.pack(side=LEFT)
    
    MHFrameRight = Frame(MHFrame, bg = 'red',width=200, height=500)
    MHFrameRight.pack(side=RIGHT)
    #=======IP left=============
    lblIP = Label(MHFrameLeft,font=('arial',20,'bold'), text="IP",bg="White",width=15,borderwidth=2, relief="solid")
    lblIP.grid(row=0,column=0)
    txtIP = Label(MHFrameLeft,font=('arial',20,'bold'), text="198.160.45.525",bd=2,fg="black",width=15, relief="solid")
    txtIP.grid(row=1,column=0)
    txtIP1 = Label(MHFrameLeft,font=('arial',20,'bold'), text="198.160.45.535",bd=2,fg="black",width=15, relief="solid")
    txtIP1.grid(row=2,column=0)
    #========score right==============
    lblScore = Label(MHFrameRight,font=('arial',20,'bold'), text="Score",bg="White",width=15,borderwidth=2, relief="solid")
    lblScore.grid(row=0,column=1)
    txtScore = Label(MHFrameRight,font=('arial',20,'bold'), text="5",bd=2,fg="black",width=15, relief="solid")
    txtScore.grid(row=1,column=1)
    txtScore1 = Label(MHFrameRight,font=('arial',20,'bold'), text="2",bd=2,fg="black",width=15, relief="solid")
    txtScore1.grid(row=2,column=1)
    #=========== จำนวนที่เล่น ===============
    lblplaycount = Label(MHFrameRight,font=('arial',20,'bold'), text="play count",bg="White",width=15,borderwidth=2, relief="solid")
    lblplaycount.grid(row=0,column=2)
    txtplaycount1 = Label(MHFrameRight,font=('arial',20,'bold'), text="7",bd=2,fg="black",width=15, relief="solid")
    txtplaycount1.grid(row=1,column=2)
    txtplaycount2 = Label(MHFrameRight,font=('arial',20,'bold'), text="7",bd=2,fg="black",width=15, relief="solid")
    txtplaycount2.grid(row=2,column=2)
    

    
    #########Button go Back #####
    BottomHFrame = Frame(MainFrame, bg = 'lime green',width=700, height=100)
    BottomHFrame.pack(side=TOP)
    def close_window ():
        window.destroy()
    btnPG = Button(BottomHFrame, text="Exit", font=('Times 15 bold'), height = 1, width=15,bg="#edb44e",command=close_window)
    btnPG.grid(row=2,column=0)
    
    #window.resizable(width=False, height=False)

btnHall = Button(RightFrame4, text="Hall of Fame", font=('Times 15 bold'), height = 1, width=20,bg="#edb44e", command=openhof)
btnHall.pack()



root.mainloop()

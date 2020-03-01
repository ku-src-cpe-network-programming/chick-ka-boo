from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

import random
import time

root = Tk()
##root.geometry("1280x680+1600+250")

#w=1287
#h=712

w=1900
h=800


ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
    # calculate position x, y
x = (ws/2) - (w/2)    
y = (hs/2) - (h/2)

root.geometry('%dx%d+%d+%d' % (w, h, x, y))
#root.geometry("1280x720+0+0")
root.resizable(0, 0)
root.title("TEXAS สาขา Chick-ka-boo")
root.configure(background='#DD4132')
## น้ำเงิน #2b5797
##เหลือง #edb44e


Tops = Frame(root,width= 1000,height = 200, bd=2, relief="raise",bg='#DD4132')
Tops.pack(side=TOP)




fMainL = Frame(root,width= 1500,height = 2000, bd=2, relief="raise",bg='red')
fMainL.pack(side=LEFT)

fMainR = Frame(root,width= 2000,height = 650, bd=2, relief="raise",bg='#2b5797')
fMainR.pack(side=RIGHT)

fMLT = Frame(fMainL,width= 900,height = 320, bd=2, relief="raise",bg='red')
fMLT.pack(side=TOP)

fMLB = Frame(fMainL,width= 900,height = 320, bd=2, relief="raise" ,bg='pink')
fMLB.pack(side=BOTTOM)

fRemail = Frame(fMainR,width=100,height = 200, bd=2, relief="raise" ,bg="#2b5797")
fRemail.pack(side=TOP)
#===========frmae send file========================
fRsendfile = Frame(fMainR,width=2000,height = 200, bd=2, relief="raise" ,bg='#2b5797')
fRsendfile.pack(side=BOTTOM)
fRsendfile_0 = Frame(fRsendfile, bd=2, relief="raise" ,bg='black')
fRsendfile_0.grid(row=0,column=0)
fRsendfile_1 = Frame(fRsendfile, bd=2, relief="raise" ,bg='black')
fRsendfile_1.grid(row=0,column=1)
#========================================

fReceipt = Frame(fMainR,width= 440,height = 450, bd=2, relief="raise" ,bg="#2b5797")
fReceipt.pack(side=TOP)

fButton = Frame(fMainR,width= 440,height = 240, bd=2, relief="raise",bg='black')
fButton.pack(side=BOTTOM)
#===============ฝั่ง รายการอาหาร=========================
fChicken0 = Frame(fMLT, bd=2, relief="raise",bg='white')
fChicken0.pack(side=TOP)
fChicken00 = Frame(fMLT, bd=2, relief="raise",bg='white')
fChicken00.pack(side=TOP)

fChicken1 = Frame(fMLT,width= 400,height = 500, bd=2, relief="raise",bg='white')
fChicken1.pack(side=TOP)
fChicken11 = Frame(fMLT,width= 400,height = 500, bd=2, relief="raise",bg='white')
fChicken11.pack(side=TOP)

fChicken2 = Frame(fMLT,width= 400,height = 250, bd=2, relief="raise",bg='white')
fChicken2.pack(side=TOP)
fChicken22 = Frame(fMLT,width= 400,height = 250, bd=2, relief="raise",bg='white')
fChicken22.pack(side=TOP)
#===========================================================================
fCost1 = Frame(fMLB,width= 1000,height = 330, bd=2, relief="raise",bg='Dark Orange')
fCost1.pack(side=LEFT)
fCost2 = Frame(fMLB,width= 1000,height = 320, bd=2, relief="raise",bg='Dark Orange')
fCost2.pack(side=LEFT)
fCost3 = Frame(fMLB,width= 1000,height = 320, bd=2, relief="raise",bg='Dark Orange')
fCost3.pack(side=LEFT)


##=============email server=====================
lblServer = Label(fRemail,font=('TH Sarabun New',15,'bold'),text = "เซิร์ฟเวอร์",bg="#2b5797",bd=5,fg="#edb44e")
lblEmail = Label(fRemail,font=('TH Sarabun New',15,'bold'),text = "อีเมล",bg="#2b5797",bd=5,fg="#edb44e")
lblServer.grid(row=1,column=0)
lblEmail.grid(row=2,column=0)
lblSendfile = Label(fRsendfile_0,font=('TH Sarabun New',18,'bold'),text = "ส่งไฟล์: สำหนักงานใหญ่",bg="#2b5797",bd=10,fg="#edb44e")
lblSendfile.grid(row=3,column=0)
##========== ส่วน หัว ป้ายชื่อ =========================================
lblInfo = Label(Tops,font=('TH Sarabun New',35,'bold'),text = " TEXAS CHICKEN  (Chick-ka-boo)",bg="#2b5797",bd=10,fg="#edb44e")
lblInfo.grid(row=0,column=1)


logoSizeX=80
logoSizeY=80
image = Image.open("logotexas.png")
image = image.resize((logoSizeX, logoSizeY))
photo = ImageTk.PhotoImage(image)
logo = Label(Tops,width=logoSizeX,height=logoSizeY,image=photo)
logo.image = photo # keep a reference!
logo.grid(row=0,column=0)


#============================= FTP Server =====================
EntryServer = StringVar()

widthEntryServer=48
txtServer = Entry(fRemail ,font=('TH Sarabun New',12,'bold'),bd=5,width=widthEntryServer,justify='left',textvariable=EntryServer, state = NORMAL)
txtServer.grid(row=1,column =1)

#============================= E-Mail =====================
EntryEmail = StringVar()

txtEmail = Entry(fRemail ,font=('TH Sarabun New',12,'bold'),bd=5,width=widthEntryServer,justify='left',textvariable=EntryEmail, state = NORMAL)
txtEmail.grid(row=2,column =1)

#============================= Function =====================
def serverAccess():
    print("Server\t: "+EntryServer.get())

def emailAccess():
    print("E-Mail\t: "+EntryEmail.get())

def sendFile():
    print("E-Mail\t: "+EntryEmail.get())

def qExit():
    qExit= messagebox.askyesno("Quit System!!!", "Do you want to quit?")
    if qExit > 0:
        root.destroy()
        return
def Reset():
    FrameChickenReset()
    FrameCostReset()
    txtReceipt.delete("1.0",END)

def FrameChickenReset():
    for x in VarChickenList:
        x.set("0")

    for x in EntryChickenList:
        x.set("0")

    txtChicken0.configure(state = DISABLED)
    txtChicken1.configure(state = DISABLED)
    txtChicken2.configure(state = DISABLED)
    txtChicken3.configure(state = DISABLED)
    txtChicken4.configure(state = DISABLED)
    txtChicken5.configure(state = DISABLED)
    txtChicken6.configure(state = DISABLED)
    #txtChicken7.configure(state = DISABLED)
    txtChicken8.configure(state = DISABLED)
    txtChicken9.configure(state = DISABLED)
    txtChicken10.configure(state = DISABLED)
   

def FrameCostReset():
    CostofChicken.set("")
    ServiceCharge.set("")
    PaidTax.set("")
    SubTotal.set("")
    TotalCost.set("")
    CostofChicken.set("")
    RecieveMoney.set("")
    ChangeMoney.set("")

def chkbutton_value(chkValue,txtLabel,Entry):
    if chkValue.get() == 1:
        txtLabel.configure(state=NORMAL)
    elif chkValue.get() == 0:
        txtLabel.configure(state=DISABLED)
        Entry.set("0")


def CostofItem():
       TotalChickenCost = 0
       ChickenPriceList = [50,50,50,50,50,50,50,50,50,50,50,50]

       for i in range(12) :
             TotalChickenCost += int(EntryChickenList[i].get())* float(ChickenPriceList[i])

       ChickensPrice = str('%.2f'%(TotalChickenCost)), "บาท"
       CostofChicken.set(ChickensPrice)
       SC =  str('%.2f'%(1.59)), "บาท"
       ServiceCharge.set(SC)

       CostPlus = TotalChickenCost + 1.59

       SubTotalofItems = str('%.2f'%(CostPlus)), "บาท"
       SubTotal.set(SubTotalofItems)

       Tax = str('%.2f'%(CostPlus*0.15)), "บาท"
       PaidTax.set(Tax)
       TT = CostPlus * 0.15
       TC = str('%.2f'%(CostPlus + TT)), "บาท"
       TotalCost.set(TC)

def Receipt():
    if Chicken0 == true :
        #Chicken0 == 0
    #else:
        txtReceipt.delete("1.0",END)
        x = random.randint(10908,500876)
        randomRef = str(x)
        ReceiptRef.set("BILL"+randomRef)
        txtReceipt.insert(END,'ใบเสร็จ หมายเลข:\t\t\t'+ ReceiptRef.get()  + '\t\t' + DateofOrder.get() + "\n")
        txtReceipt.insert(END,'รายการ\t\t\t\t\t'+ 'จำนวน \n\n')
        for i in range(12) :
            if int(EntryChickenList[i].get()) > 0 :
                txtReceipt.insert(END, ChickenList[i] +'\t\t\t\t\t'+ EntryChickenList[i].get() + '\n')

        txtReceipt.insert(END,'\nราคารวม : \t\t'+ CostofChicken.get() + '\n')
        txtReceipt.insert(END,'ค่าบริการ : \t\t'+ ServiceCharge.get() + '\n')

#====================== Variable Chicken =====================
ReceiptRef = StringVar()
DateofOrder = StringVar()
DateofOrder.set(time.strftime("%d/%m/%Y"))

ChickenList = ["ไก่ทอดสไปซี่","ไก่ทอดต้มยำ","ไก่นุ่ม","ข้าวยำไก่แซ่บ",
            "ไก่ทอดชุดครอบครัว","ชุดไก่สารพัด","ไก่ทอดเกาหลี","ชุดไก่ปิคนิก",
            "ชุดไก่ปิกนิก","เคบับไก่","เบอร์เกอร์ไก่","Ice-Cream Chicken"]

VarChicken0 = IntVar()
VarChicken1 = IntVar()
VarChicken2 = IntVar()
VarChicken3 = IntVar()
VarChicken4 = IntVar()
VarChicken5 = IntVar()
VarChicken6 = IntVar()
VarChicken7 = IntVar()
VarChicken8 = IntVar()
VarChicken9 = IntVar()
VarChicken10 = IntVar()
VarChicken11 = IntVar()

VarChickenList = [VarChicken0,VarChicken1,VarChicken2,VarChicken3,
               VarChicken4,VarChicken5,VarChicken6,VarChicken7,
               VarChicken8,VarChicken9,VarChicken10,VarChicken11]

for x in VarChickenList:
    x.set("0")

EntryChicken0 = StringVar()
EntryChicken1 = StringVar()
EntryChicken2 = StringVar()
EntryChicken3 = StringVar()
EntryChicken4 = StringVar()
EntryChicken5 = StringVar()
EntryChicken6 = StringVar()
EntryChicken7 = StringVar()
EntryChicken8 = StringVar()
EntryChicken9 = StringVar()
EntryChicken10 = StringVar()
EntryChicken11 = StringVar()

EntryChickenList = [EntryChicken0,EntryChicken1,EntryChicken2,EntryChicken3,
                 EntryChicken4,EntryChicken5,EntryChicken6,EntryChicken7,
                 EntryChicken8,EntryChicken9,EntryChicken10,EntryChicken11]

for x in EntryChickenList:
    x.set("0")
#====================image chicka bool===============
#================column 0=================
menuSizeX=200
menuSizeY=117
menuSizeX2=268
img_0 = Image.open("menu00.jpg")
img_0 =  img_0.resize((menuSizeX, menuSizeY))
photo_0 = ImageTk.PhotoImage(img_0)
img_00 = Label(fChicken0,width=menuSizeX,height=menuSizeY,image=photo_0,bg='white')
img_00.image = photo_0 # keep a reference!
img_00.grid(row=0,column=0)

img_1 = Image.open("menu01.jpg")
img_1 =  img_1.resize((menuSizeX, menuSizeY))
photo_1 = ImageTk.PhotoImage(img_1)
img_11 = Label(fChicken0,width=menuSizeX,height=menuSizeY,image=photo_1,bg='white')
img_11.image = photo_1 # keep a reference!
img_11.grid(row=0,column=2)

img_2 = Image.open("menu02.jpg")
img_2 =  img_2.resize((menuSizeX, menuSizeY))
photo_2 = ImageTk.PhotoImage(img_2)
img_22 = Label(fChicken0,width=menuSizeX,height=menuSizeY,image=photo_2,bg='white')
img_22.image = photo_2 # keep a reference!
img_22.grid(row=0,column=4)

img_3 = Image.open("menu03.jpg")
img_3 =  img_3.resize((menuSizeX, menuSizeY))
photo_3 = ImageTk.PhotoImage(img_3)
img_33 = Label(fChicken0,width=menuSizeX,height=menuSizeY,image=photo_3,bg='white')
img_33.image = photo_3 # keep a reference!
img_33.grid(row=0,column=6)
#================column 2=================
img_4 = Image.open("menu04.jpg")
img_4 =  img_4.resize((menuSizeX2, menuSizeY))
photo_4 = ImageTk.PhotoImage(img_4)
img_44 = Label(fChicken1,width=menuSizeX2,height=menuSizeY,image=photo_4,bg='white')
img_44.image = photo_4 # keep a reference!
img_44.grid(row=0,column=1)

img_5 = Image.open("menu05.jpg")
img_5 =  img_5.resize((menuSizeX2, menuSizeY))
photo_5 = ImageTk.PhotoImage(img_5)
img_55 = Label(fChicken1,width=menuSizeX2,height=menuSizeY,image=photo_5,bg='white')
img_55.image = photo_5 # keep a reference!
img_55.grid(row=0,column=2)

img_6 = Image.open("menu06.jpg")
img_6 =  img_6.resize((menuSizeX2, menuSizeY))
photo_6 = ImageTk.PhotoImage(img_6)
img_66 = Label(fChicken1,width=menuSizeX2,height=menuSizeY,image=photo_6,bg='white')
img_66.image = photo_6 # keep a reference!
img_66.grid(row=0,column=3)
#================column 4=================
img_8 = Image.open("menu07.jpg")
img_8 =  img_8.resize((menuSizeX2, menuSizeY))
photo_8 = ImageTk.PhotoImage(img_8)
img_88 = Label(fChicken2,width=menuSizeX2,height=menuSizeY,image=photo_8,bg='white')
img_88.image = photo_8 # keep a reference!
img_88.grid(row=0,column=1)

img_9 = Image.open("menu08.jpg")
img_9 =  img_9.resize((menuSizeX2, menuSizeY))
photo_9 = ImageTk.PhotoImage(img_9)
img_99 = Label(fChicken2,width=menuSizeX2,height=menuSizeY,image=photo_9,bg='white')
img_99.image = photo_9 # keep a reference!
img_99.grid(row=0,column=2)

img_10 = Image.open("menu09.jpg")
img_10 =  img_10.resize((menuSizeX2, menuSizeY))
photo_10 = ImageTk.PhotoImage(img_10)
img_10 = Label(fChicken2,width=menuSizeX2,height=menuSizeY,image=photo_10,bg='white')
img_10.image = photo_10 # keep a reference!
img_10.grid(row=0,column=3)

#====================================== Chicken ====================================
"""CoffeeChicken = Checkbutton(fChicken, text="Coffee Chicken \t",variable = var9,onvalue = 1, offvalue=0,
                    font=('TH Sarabun New',18,'bold')).grid(row= 0, column=0)"""
Chicken0 = Checkbutton(fChicken00 , text=ChickenList[0],variable = VarChickenList[0] ,onvalue = 1, offvalue=0,
                    font=('TH Sarabun New',14,'bold'),command=lambda:chkbutton_value(VarChickenList[0],txtChicken0,EntryChickenList[0])).grid(row= 0,column=0, sticky=W)
Chicken1 = Checkbutton(fChicken00 , text=ChickenList[1],variable = VarChickenList[1],onvalue = 1, offvalue=0,
                    font=('TH Sarabun New',14,'bold'),command=lambda:chkbutton_value(VarChickenList[1],txtChicken1,EntryChickenList[1])).grid(row= 0,column=3, sticky=W)
Chicken2 = Checkbutton(fChicken00 , text=ChickenList[2],variable = VarChickenList[2],onvalue = 1, offvalue=0,
                    font=('TH Sarabun New',14,'bold'),command=lambda:chkbutton_value(VarChickenList[2],txtChicken2,EntryChickenList[2])).grid(row= 0,column=5, sticky=W)
Chicken3 = Checkbutton(fChicken00 , text=ChickenList[3],variable = VarChickenList[3],onvalue = 1, offvalue=0,
                    font=('TH Sarabun New',14,'bold'),command=lambda:chkbutton_value(VarChickenList[3],txtChicken3,EntryChickenList[3])).grid(row= 0,column=7, sticky=W)

Chicken4 = Checkbutton(fChicken11 , text=ChickenList[4],variable = VarChickenList[4],onvalue = 1, offvalue=0,
                    font=('TH Sarabun New',14,'bold'),command=lambda:chkbutton_value(VarChickenList[4],txtChicken4,EntryChickenList[4])).grid(row= 1,column=0, sticky=W)
Chicken5 = Checkbutton(fChicken11, text=ChickenList[5],variable = VarChickenList[5],onvalue = 1, offvalue=0,
                    font=('TH Sarabun New',14,'bold'),command=lambda:chkbutton_value(VarChickenList[5],txtChicken5,EntryChickenList[5])).grid(row= 1,column=2, sticky=W)
Chicken6 = Checkbutton(fChicken11, text=ChickenList[6],variable = VarChickenList[6],onvalue = 1, offvalue=0,
                    font=('TH Sarabun New',14,'bold'),command=lambda:chkbutton_value(VarChickenList[6],txtChicken6,EntryChickenList[6])).grid(row= 1,column=4, sticky=W)
#Chicken7 = Checkbutton(fChicken1 , text=ChickenList[7],variable = VarChickenList[7],onvalue = 1, offvalue=0,
                    #font=('TH Sarabun New',14,'bold'),command=lambda:chkbutton_value(VarChickenList[7],txtChicken7,EntryChickenList[7])).grid(row= 7, sticky=W)

Chicken8 = Checkbutton(fChicken22, text=ChickenList[8],variable = VarChickenList[8],onvalue = 1, offvalue=0,
                    font=('TH Sarabun New',14,'bold'),command=lambda:chkbutton_value(VarChickenList[8],txtChicken8,EntryChickenList[8])).grid(row= 1,column=0, sticky=W)
Chicken9 = Checkbutton(fChicken22 , text=ChickenList[9],variable = VarChickenList[9],onvalue = 1, offvalue=0,
                    font=('TH Sarabun New',14,'bold'),command=lambda:chkbutton_value(VarChickenList[9],txtChicken9,EntryChickenList[9])).grid(row= 1,column=2, sticky=W)
Chicken10 = Checkbutton(fChicken22 , text=ChickenList[10],variable = VarChickenList[10],onvalue = 1, offvalue=0,
                    font=('TH Sarabun New',14,'bold'),command=lambda:chkbutton_value(VarChickenList[10],txtChicken10,EntryChickenList[10])).grid(row= 1,column=4, sticky=W)
#Chicken11 = Checkbutton(fChicken2 , text=ChickenList[11],variable = VarChickenList[11],onvalue = 1, offvalue=0,
                    #font=('TH Sarabun New',12,'bold'),command=lambda:chkbutton_value(VarChickenList[11],txtChicken11,EntryChickenList[11])).grid(row= 11, sticky=W)

#=======================Enter Widgets for Chicken =======================
txtChicken0 = Entry(fChicken00 ,font=('TH Sarabun New',12,'bold'),bd=5,width=13,justify='right',textvariable=EntryChickenList[0],state = DISABLED)
txtChicken0.grid(row=0,column =2)
txtChicken1 = Entry(fChicken00 ,font=('TH Sarabun New',12,'bold'),bd=5,width=16,justify='right',textvariable=EntryChickenList[1],state = DISABLED)
txtChicken1.grid(row=0,column =4)
txtChicken2 = Entry(fChicken00 ,font=('TH Sarabun New',12,'bold'),bd=5,width=22,justify='right',textvariable=EntryChickenList[2],state = DISABLED)
txtChicken2.grid(row=0,column =6)
txtChicken3 = Entry(fChicken00 ,font=('TH Sarabun New',12,'bold'),bd=5,width=13,justify='right',textvariable=EntryChickenList[3],state = DISABLED)
txtChicken3.grid(row=0,column =8)

txtChicken4 = Entry(fChicken11 ,font=('TH Sarabun New',12,'bold'),bd=5,width=19,justify='right',textvariable=EntryChickenList[4],state = DISABLED)
txtChicken4.grid(row=1,column =1)
txtChicken5 = Entry(fChicken11 ,font=('TH Sarabun New',12,'bold'),bd=5,width=26,justify='right',textvariable=EntryChickenList[5],state = DISABLED)
txtChicken5.grid(row=1,column =3)
txtChicken6 = Entry(fChicken11 ,font=('TH Sarabun New',12,'bold'),bd=5,width=25,justify='right',textvariable=EntryChickenList[6],state = DISABLED)
txtChicken6.grid(row=1,column =5)
#txtChicken7 = Entry(fChicken1 ,font=('TH Sarabun New',12,'bold'),bd=5,width=6,justify='left',textvariable=EntryChickenList[7],state = DISABLED)
#txtChicken7.grid(row=7,column =1)

txtChicken8 = Entry(fChicken22 ,font=('TH Sarabun New',12,'bold'),bd=5,width=27,justify='right',textvariable=EntryChickenList[7],state = DISABLED)
txtChicken8.grid(row=1,column =1)
txtChicken9 = Entry(fChicken22 ,font=('TH Sarabun New',12,'bold'),bd=5,width=31,justify='right',textvariable=EntryChickenList[8],state = DISABLED)
txtChicken9.grid(row=1,column =3)
txtChicken10 = Entry(fChicken22 ,font=('TH Sarabun New',12,'bold'),bd=5,width=26,justify='right',textvariable=EntryChickenList[9],state = DISABLED)
txtChicken10.grid(row=1,column =5)

#===============================Variable Calculation =====================
PaidTax = StringVar()
SubTotal = StringVar()
TotalCost = StringVar()
CostofChicken = StringVar()
ServiceCharge = StringVar()
RecieveMoney = StringVar()
ChangeMoney = StringVar()

#================================== Receipt Information ===================
lblReceipt = Label(fReceipt,font=('TH Sarabun New',13,'bold'), text="ใบเสร็จ", bd=2,anchor='w' ,fg="#edb44e",bg="#2b5797")
lblReceipt.grid(row=0,column=0, sticky=W)
txtReceipt = Text(fReceipt,font=('TH Sarabun New',12,'bold'), bd=2,width=73,height=17,bg="white")
txtReceipt.grid(row=1,column=0)

#=================================== Cost Items Information============
lblthx = Label(fCost1,font=('TH Sarabun New',12,'bold'),text="Your order Texas",bd=5,bg="Dark Orange")
lblthx.grid(row=0,column=0,sticky=W)
lblthx = Label(fCost1,font=('TH Sarabun New',12,'bold'),text="Chicken (Chick-ka-boo)",bd=5,bg="Dark Orange")
lblthx.grid(row=0,column=1,sticky=W)
lblCostofChicken = Label(fCost1,font=('TH Sarabun New',12,'bold'),text="ราคารวม",bd=5,bg="Dark Orange")
lblCostofChicken.grid(row=1,column=0,sticky=W)
txtCostofChicken=Entry(fCost1,font=('TH Sarabun New',12,'bold'),bd=5,justify='right',
                      textvariable=CostofChicken,bg="white")
txtCostofChicken.grid(row=1,column=1,sticky=W)

lblServiceCharge = Label(fCost1,font=('TH Sarabun New',12,'bold'),text="ค่าบริการ",bd=5,bg="Dark Orange")
lblServiceCharge.grid(row=2,column=0,sticky=W)
txtServiceCharge=Entry(fCost1,font=('TH Sarabun New',12,'bold'),bd=5,justify='right',
                       textvariable=ServiceCharge,bg="white")
txtServiceCharge.grid(row=2,column=1,sticky=W)

#=========================== Payment Information========================
lblPaidTax = Label(fCost2,font=('TH Sarabun New',12,'bold'),text="ภาษี",bd=5,bg="Dark Orange")
lblPaidTax.grid(row=0,column=0,sticky=W)
txtPaidTax=Entry(fCost2,font=('TH Sarabun New',12,'bold'),bd=5,justify='right',
                 textvariable=PaidTax,bg="white")
txtPaidTax.grid(row=0,column=1,sticky=W)

lblSubTotal = Label(fCost2,font=('TH Sarabun New',12,'bold'),text="ราคารวมค่าบริการ",bd=5,bg="Dark Orange")
lblSubTotal.grid(row=1,column=0,sticky=W)
txtSubTotal=Entry(fCost2,font=('TH Sarabun New',12,'bold'),bd=5,justify='right',
                  textvariable=SubTotal,bg="white")
txtSubTotal.grid(row=1,column=1,sticky=W)

lblTotalCost = Label(fCost2,font=('TH Sarabun New',12,'bold'),text="ราคารวมทั้งหมด",bd=5,bg="Dark Orange")
lblTotalCost.grid(row=2,column=0,sticky=W)
txtTotalCost=Entry(fCost2,font=('TH Sarabun New',12,'bold'),bd=5,justify='right',
                   textvariable=TotalCost,bg="white")
txtTotalCost.grid(row=2,column=1,sticky=W)

lblRecieveMoney = Label(fCost3,font=('TH Sarabun New',12,'bold'),text="รับเงิน",bd=5,bg="Dark Orange")
lblRecieveMoney.grid(row=0,column=0,sticky=W)
txtRecieveMoney=Entry(fCost3,font=('TH Sarabun New',12,'bold'),bd=5,justify='right',
                   textvariable=RecieveMoney,bg="white")
txtRecieveMoney.grid(row=0,column=1,sticky=W)

lblChangeMoney = Label(fCost3,font=('TH Sarabun New',12,'bold'),text="เงินทอน",bd=5,bg="Dark Orange")
lblChangeMoney.grid(row=1,column=0,sticky=W)
txtChangeMoney=Entry(fCost3,font=('TH Sarabun New',12,'bold'),bd=5,justify='right',
                   textvariable=ChangeMoney,bg="white")
txtChangeMoney.grid(row=1,column=1,sticky=W)



lblEmpty = Label(fCost3,font=('TH Sarabun New',12,'bold'),text="",bd=5,bg="Dark Orange")
lblEmpty.grid(row=2,column=0,sticky=W)
#================================== Button =========================
widthButtonTotal=4
padxButtonTotal=32
btnTotal=Button(fButton,padx=padxButtonTotal, fg="black",font=('TH Sarabun New',18,'bold'),width=widthButtonTotal,
                text="คิดเงิน",command=CostofItem).grid(row=0, column=0)
btnReceipt=Button(fButton,padx=padxButtonTotal, fg="black",font=('TH Sarabun New',18,'bold'),width=widthButtonTotal,
                text="พิมพ์ใบเสร็จ",command=Receipt).grid(row=0, column=1)
btnReset=Button(fButton,padx=padxButtonTotal, fg="black",font=('TH Sarabun New',18,'bold'),width=widthButtonTotal,
                text="ล้าง",command=Reset).grid(row=0, column=2)
btnExit=Button(fButton,padx=padxButtonTotal, fg="black",font=('TH Sarabun New',18,'bold'),width=widthButtonTotal,
                text="ออก",command=qExit).grid(row=0, column=3)
    #===== btn email server=============
btnServer=Button(fRemail,padx=22, fg="black",font=('TH Sarabun New',12,'bold'),width=5,
                text="เปลี่ยนเซิฟเวอร์",command=serverAccess).grid(row=1, column=2)
btnEmail=Button(fRemail,padx=22, fg="black",font=('TH Sarabun New',12,'bold'),width=5,
                text="เปลี่ยนอีเมล์",command=emailAccess).grid(row=2, column=2)
btnSendFile=Button(fRsendfile_1,padx=30, fg="black",font=('TH Sarabun New',18,'bold'),width=5,
                text="ยืนยัน",command=sendFile).grid(row=3, column=1)




root.mainloop()

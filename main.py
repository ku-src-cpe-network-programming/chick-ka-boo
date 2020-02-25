from tkinter import *
from tkinter import messagebox
import random
import time

root = Tk()
root.geometry("1280x680+1600+250")
root.title("Chick-ka-boo")
root.configure(background='cyan')

Tops = Frame(root,width= 1350,height = 100, bd=5, relief="raise")
Tops.pack(side=TOP)

fMainL = Frame(root,width= 900,height = 650, bd=5, relief="raise")
fMainL.pack(side=LEFT)

fMainR = Frame(root,width= 440,height = 650, bd=5, relief="raise")
fMainR.pack(side=RIGHT)

fMLT = Frame(fMainL,width= 900,height = 320, bd=5, relief="raise")
fMLT.pack(side=TOP)

fMLB = Frame(fMainL,width= 900,height = 320, bd=5, relief="raise")
fMLB.pack(side=BOTTOM)

fReceipt = Frame(fMainR,width= 440,height = 450, bd=5, relief="raise")
fReceipt.pack(side=TOP)
fButton = Frame(fMainR,width= 440,height = 240, bd=5, relief="raise")
fButton.pack(side=BOTTOM)

fChickenLeft = Frame(fMLT,width= 400,height = 330, bd=5, relief="raise")
fChickenLeft.pack(side=LEFT)
fChickenRight = Frame(fMLT,width= 400,height = 320, bd=5, relief="raise")
fChickenRight.pack(side=RIGHT)

fCost1 = Frame(fMLB,width= 440,height = 330, bd=5, relief="raise")
fCost1.pack(side=LEFT)
fCost2 = Frame(fMLB,width= 440,height = 320, bd=5, relief="raise")
fCost2.pack(side=RIGHT)

Tops.configure(background='pink')
fMainL.configure(background='blue')
fMainR.configure(background='blue')

lblInfo = Label(Tops,font=('TH Sarabun New',25,'bold'),text = "Chick-ka-boo",bg="yellow",bd=5)
lblServer = Label(Tops,font=('TH Sarabun New',25,'bold'),text = "Server",bg="yellow",bd=5)
lblInfo.grid(row=0,column=0)
lblServer.grid(row=1,column=0)


#============================= FTP Server =====================
VarServer = IntVar()
EntryServer = StringVar()

txtServer = Entry(Tops ,font=('TH Sarabun New',18,'bold'),bd=5,width=6,justify='left',textvariable=EntryServer, state = NORMAL)
txtServer.grid(row=1,column =1)

#============================= Function =====================
def serverAccess():
    print("Server: "+EntryServer.get())
    
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
    txtChicken7.configure(state = DISABLED)
    txtChicken8.configure(state = DISABLED)
    txtChicken9.configure(state = DISABLED)
    txtChicken10.configure(state = DISABLED)
    txtChicken11.configure(state = DISABLED)
    
def FrameCostReset():
    CostofChicken.set("")
    ServiceCharge.set("")
    PaidTax.set("")
    SubTotal.set("")
    TotalCost.set("")
    CostofChicken.set("")
                 
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
                                                             
       ChickensPrice = "B", str('%.2f'%(TotalChickenCost))
       CostofChicken.set(ChickensPrice)
       SC = "B", str('%.2f'%(1.59))
       ServiceCharge.set(SC)

       CostPlus = TotalChickenCost + 1.59
        
       SubTotalofItems = "B", str('%.2f'%(CostPlus))
       SubTotal.set(SubTotalofItems)

       Tax = "B" , str('%.2f'%(CostPlus*0.15))
       PaidTax.set(Tax)
       TT = CostPlus * 0.15
       TC = "B" , str('%.2f'%(CostPlus + TT))
       TotalCost.set(TC)

def Receipt():
    txtReceipt.delete("1.0",END)
    x = random.randint(10908,500876)
    randomRef = str(x)
    ReceiptRef.set("BILL"+randomRef)
    txtReceipt.insert(END,'Receipt Ref:\t\t\t'+ ReceiptRef.get()  + '\t\t' + DateofOrder.get() + "\n")
    txtReceipt.insert(END,'Items\t\t\t\t\t'+ 'Cost of Items \n\n')   
    for i in range(12) :
        if int(EntryChickenList[i].get()) > 0 :
            txtReceipt.insert(END, ChickenList[i] +'\t\t\t\t\t'+ EntryChickenList[i].get() + '\n')        

    txtReceipt.insert(END,'\nCost of Chickens : \t\t'+ CostofChicken.get() + '\n')
    txtReceipt.insert(END,'Service Charge : \t\t'+ ServiceCharge.get() + '\n')
    
#====================== Variable Chicken =====================
ChickenList = ["Coffee Chicken","Red Velvet Chicken","Black Forest Chicken","Boston Cream Chicken",
            "Lagos Chocolate","Kilburn Chocolate Chicken","Carton Hill Chicken","Queen Park Chicken",
            "Chicken Lad Manow","Chicken Boil","Fire Rice Chicken","Ice-Cream Chicken"]

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
    
#====================================== Chicken ====================================
"""CoffeeChicken = Checkbutton(fChicken, text="Coffee Chicken \t",variable = var9,onvalue = 1, offvalue=0,
                    font=('TH Sarabun New',18,'bold')).grid(row= 0, column=0)"""    
Chicken0 = Checkbutton(fChickenLeft , text=ChickenList[0],variable = VarChickenList[0] ,onvalue = 1, offvalue=0,
                    font=('TH Sarabun New',18,'bold'),command=lambda:chkbutton_value(VarChickenList[0],txtChicken0,EntryChickenList[0])).grid(row= 0, sticky=W)
Chicken1 = Checkbutton(fChickenLeft , text=ChickenList[1],variable = VarChickenList[1],onvalue = 1, offvalue=0,
                    font=('TH Sarabun New',18,'bold'),command=lambda:chkbutton_value(VarChickenList[1],txtChicken1,EntryChickenList[1])).grid(row= 1, sticky=W)
Chicken2 = Checkbutton(fChickenLeft , text=ChickenList[2],variable = VarChickenList[2],onvalue = 1, offvalue=0,
                    font=('TH Sarabun New',18,'bold'),command=lambda:chkbutton_value(VarChickenList[2],txtChicken2,EntryChickenList[2])).grid(row= 2, sticky=W)
Chicken3 = Checkbutton(fChickenLeft , text=ChickenList[3],variable = VarChickenList[3],onvalue = 1, offvalue=0,
                    font=('TH Sarabun New',18,'bold'),command=lambda:chkbutton_value(VarChickenList[3],txtChicken3,EntryChickenList[3])).grid(row= 3, sticky=W)
Chicken4 = Checkbutton(fChickenLeft , text=ChickenList[4],variable = VarChickenList[4],onvalue = 1, offvalue=0,
                    font=('TH Sarabun New',18,'bold'),command=lambda:chkbutton_value(VarChickenList[4],txtChicken4,EntryChickenList[4])).grid(row= 4, sticky=W)
Chicken5 = Checkbutton(fChickenLeft , text=ChickenList[5],variable = VarChickenList[5],onvalue = 1, offvalue=0,
                    font=('TH Sarabun New',18,'bold'),command=lambda:chkbutton_value(VarChickenList[5],txtChicken5,EntryChickenList[5])).grid(row= 5, sticky=W)
Chicken6 = Checkbutton(fChickenLeft , text=ChickenList[6],variable = VarChickenList[6],onvalue = 1, offvalue=0,
                    font=('TH Sarabun New',18,'bold'),command=lambda:chkbutton_value(VarChickenList[6],txtChicken6,EntryChickenList[6])).grid(row= 6, sticky=W)
Chicken7 = Checkbutton(fChickenLeft , text=ChickenList[7],variable = VarChickenList[7],onvalue = 1, offvalue=0,
                    font=('TH Sarabun New',18,'bold'),command=lambda:chkbutton_value(VarChickenList[7],txtChicken7,EntryChickenList[7])).grid(row= 7, sticky=W)

Chicken8 = Checkbutton(fChickenRight , text=ChickenList[8],variable = VarChickenList[8],onvalue = 1, offvalue=0,
                    font=('TH Sarabun New',18,'bold'),command=lambda:chkbutton_value(VarChickenList[8],txtChicken8,EntryChickenList[8])).grid(row= 8, sticky=W)
Chicken9 = Checkbutton(fChickenRight , text=ChickenList[9],variable = VarChickenList[9],onvalue = 1, offvalue=0,
                    font=('TH Sarabun New',18,'bold'),command=lambda:chkbutton_value(VarChickenList[9],txtChicken9,EntryChickenList[9])).grid(row= 9, sticky=W)
Chicken10 = Checkbutton(fChickenRight , text=ChickenList[10],variable = VarChickenList[10],onvalue = 1, offvalue=0,
                    font=('TH Sarabun New',18,'bold'),command=lambda:chkbutton_value(VarChickenList[10],txtChicken10,EntryChickenList[10])).grid(row= 10, sticky=W)
Chicken11 = Checkbutton(fChickenRight , text=ChickenList[11],variable = VarChickenList[11],onvalue = 1, offvalue=0,
                    font=('TH Sarabun New',18,'bold'),command=lambda:chkbutton_value(VarChickenList[11],txtChicken11,EntryChickenList[11])).grid(row= 11, sticky=W)

#=======================Enter Widgets for Chicken =======================
txtChicken0 = Entry(fChickenLeft ,font=('TH Sarabun New',18,'bold'),bd=5,width=6,justify='left',textvariable=EntryChickenList[0],state = DISABLED)
txtChicken0.grid(row=0,column =1)
txtChicken1 = Entry(fChickenLeft ,font=('TH Sarabun New',18,'bold'),bd=5,width=6,justify='left',textvariable=EntryChickenList[1],state = DISABLED)
txtChicken1.grid(row=1,column =1)
txtChicken2 = Entry(fChickenLeft ,font=('TH Sarabun New',18,'bold'),bd=5,width=6,justify='left',textvariable=EntryChickenList[2],state = DISABLED)
txtChicken2.grid(row=2,column =1)
txtChicken3 = Entry(fChickenLeft ,font=('TH Sarabun New',18,'bold'),bd=5,width=6,justify='left',textvariable=EntryChickenList[3],state = DISABLED)
txtChicken3.grid(row=3,column =1)
txtChicken4 = Entry(fChickenLeft ,font=('TH Sarabun New',18,'bold'),bd=5,width=6,justify='left',textvariable=EntryChickenList[4],state = DISABLED)
txtChicken4.grid(row=4,column =1)
txtChicken5 = Entry(fChickenLeft ,font=('TH Sarabun New',18,'bold'),bd=5,width=6,justify='left',textvariable=EntryChickenList[5],state = DISABLED)
txtChicken5.grid(row=5,column =1)
txtChicken6 = Entry(fChickenLeft ,font=('TH Sarabun New',18,'bold'),bd=5,width=6,justify='left',textvariable=EntryChickenList[6],state = DISABLED)
txtChicken6.grid(row=6,column =1)
txtChicken7 = Entry(fChickenLeft ,font=('TH Sarabun New',18,'bold'),bd=5,width=6,justify='left',textvariable=EntryChickenList[7],state = DISABLED)
txtChicken7.grid(row=7,column =1)

txtChicken8 = Entry(fChickenRight ,font=('TH Sarabun New',18,'bold'),bd=5,width=6,justify='left',textvariable=EntryChickenList[7],state = DISABLED)
txtChicken8.grid(row=8,column =1)
txtChicken9 = Entry(fChickenRight ,font=('TH Sarabun New',18,'bold'),bd=5,width=6,justify='left',textvariable=EntryChickenList[7],state = DISABLED)
txtChicken9.grid(row=9,column =1)
txtChicken10 = Entry(fChickenRight ,font=('TH Sarabun New',18,'bold'),bd=5,width=6,justify='left',textvariable=EntryChickenList[7],state = DISABLED)
txtChicken10.grid(row=10,column =1)
txtChicken11 = Entry(fChickenRight ,font=('TH Sarabun New',18,'bold'),bd=5,width=6,justify='left',textvariable=EntryChickenList[7],state = DISABLED)
txtChicken11.grid(row=11,column =1)












#===============================Variable Calculation =====================
PaidTax = StringVar()
SubTotal = StringVar()
TotalCost = StringVar()
CostofChicken = StringVar()
ServiceCharge = StringVar()

#================================== Receipt Information ===================
lblReceipt = Label(fReceipt,font=('TH Sarabun New',12,'bold'), text="Receipt", bd=2,anchor='w')
lblReceipt.grid(row=0,column=0, sticky=W)
txtReceipt = Text(fReceipt,font=('TH Sarabun New',11,'bold'), bd=5,width=59,height=22,bg="white")
txtReceipt.grid(row=1,column=0)

#=================================== Cost Items Information============
lblCostofChicken = Label(fCost1,font=('TH Sarabun New',18,'bold'),text="Cost of Chickens",bd=5)
lblCostofChicken.grid(row=0,column=0,sticky=W)
txtCostofChicken=Entry(fCost1,font=('TH Sarabun New',18,'bold'),bd=5,justify='left',
                      textvariable=CostofChicken)
txtCostofChicken.grid(row=0,column=1,sticky=W)

lblServiceCharge = Label(fCost1,font=('TH Sarabun New',18,'bold'),text="Service Charge",bd=5)
lblServiceCharge.grid(row=2,column=0,sticky=W)
txtServiceCharge=Entry(fCost1,font=('TH Sarabun New',18,'bold'),bd=5,justify='left',
                       textvariable=ServiceCharge)
txtServiceCharge.grid(row=2,column=1,sticky=W)

#=========================== Payment Information========================
lblPaidTax = Label(fCost2,font=('TH Sarabun New',18,'bold'),text="Paid Tax",bd=5)
lblPaidTax.grid(row=0,column=0,sticky=W)
txtPaidTax=Entry(fCost2,font=('TH Sarabun New',18,'bold'),bd=5,justify='left',
                 textvariable=PaidTax)
txtPaidTax.grid(row=0,column=1,sticky=W)

lblSubTotal = Label(fCost2,font=('TH Sarabun New',18,'bold'),text="Sub Total",bd=5)
lblSubTotal.grid(row=1,column=0,sticky=W)
txtSubTotal=Entry(fCost2,font=('TH Sarabun New',18,'bold'),bd=5,justify='left',
                  textvariable=SubTotal)
txtSubTotal.grid(row=1,column=1,sticky=W)

lblTotalCost = Label(fCost2,font=('TH Sarabun New',18,'bold'),text="Total",bd=5)
lblTotalCost.grid(row=2,column=0,sticky=W)
txtTotalCost=Entry(fCost2,font=('TH Sarabun New',18,'bold'),bd=5,justify='left',
                   textvariable=TotalCost)
txtTotalCost.grid(row=2,column=1,sticky=W)
#================================== Button =========================
btnTotal=Button(fButton,padx=16, fg="black",font=('TH Sarabun New',18,'bold'),width=5,
                text="Total",command=CostofItem).grid(row=0, column=0)
btnReceipt=Button(fButton,padx=16, fg="black",font=('TH Sarabun New',18,'bold'),width=5,
                text="Receipt",command=Receipt).grid(row=0, column=1)
btnReset=Button(fButton,padx=16, fg="black",font=('TH Sarabun New',18,'bold'),width=5,
                text="Reset",command=Reset).grid(row=0, column=2)
btnExit=Button(fButton,padx=16, fg="black",font=('TH Sarabun New',18,'bold'),width=5,
                text="Exit",command=qExit).grid(row=0, column=3)

btnServer=Button(Tops,padx=16, fg="black",font=('TH Sarabun New',18,'bold'),width=5,
                text="Access",command=serverAccess).grid(row=1, column=3)


root.mainloop()

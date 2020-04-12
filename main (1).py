from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from PIL import Image
from PIL import ImageTk
from ftplib import FTP

import random
import time
import math

import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders


root = Tk()
##root.geometry("1280x680+1600+250")

w=1287
h=712

ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
    # calculate position x, y
x = (ws/2) - (w/2)    
y = (hs/2) - (h/2)

root.geometry('%dx%d+%d+%d' % (w, h, x, y))
#root.geometry("1280x720+0+0")
##root.resizable(0, 0)
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
lblSendfile = Label(fRsendfile_0,font=('TH Sarabun New',18,'bold'),text = "ส่งไฟล์: สำนักงานใหญ่",bg="#2b5797",bd=10,fg="#edb44e")
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
    global ftp_user,ftp_pass
    print("Server\t: "+EntryServer.get())
    x = simpledialog.askstring(title="secret ftp setting",prompt="Format: user,pass")
    print(x)
    if x != None:
        (x1,x2)=x.split(',')
        print(x1,x2)
    (ftp_user,ftp_pass)=(x1,x2)
    print(ftp_user,ftp_pass)

def emailAccess():
    global email_user,email_pass
    print("E-Mail\t: "+EntryEmail.get())
    x = simpledialog.askstring(title="secret email setting",prompt="Format: user,pass")
    print(x)
    if x != None:
        (x1,x2)=x.split(',')
        print(x1,x2)
    (email_user,email_pass)=(x1,x2)
    print(email_user,email_pass)
    
def sendFile():
    print("E-Mail\t: "+EntryEmail.get())
    global ftp_user,ftp_pass,email_user,email_pass,ChickenList
    shop = "Chick-ka-boo"
    filename = time.strftime(shop+"%Y%b%d")+".txt"
    with open(filename, 'r',encoding="utf-8") as f:
        lines = f.read().splitlines()
        last_line = lines[-2]
        report_sum,report_chick=last_line.split()
##        print (report_sum,report_chick)
##        print(type(report_chick))
        report_chick=(eval(str(report_chick)))
##        print((report_chick))
##        print(type(report_chick))
        for i in range(10):
                print(ChickenList[i],':',report_chick[i],'ชิ้น\n')
    if(EntryEmail.get()!='' and EntryServer.get()!=''):
        
        try:
            ftp = FTP(EntryServer.get())
            ftp.login(user=ftp_user,passwd=ftp_pass)
            if shop not in ftp.nlst():
                ftp.mkd(shop)
            ftp.cwd(shop)
            filename = time.strftime(shop+"%Y%b%d")+".txt"
            attachment = open(filename, "rb")
            ftp.storbinary('STOR '+filename,attachment)
        except:
            messagebox.showerror("เกิดข้อผิดพลาดในการส่งไฟล์ FTP", "กรุณาตรวจสอบความถูกต้องของ FTP server แล้วลองอีกครั้ง")
            return 0
        try:
##            fromaddr = "thanarak.s@ku.th" 
            fromaddr = email_user
            toaddr = EntryEmail.get()
            # instance of MIMEMultipart 
            msg = MIMEMultipart() 
            # storing the senders email address   
            msg['From'] = fromaddr 
            # storing the receivers email address  
            msg['To'] = toaddr 
            # storing the subject  
            msg['Subject'] = "Chick-ka-boo ยอดขายประจำวันของ "+time.strftime(shop+"%Y%b%d")
            # string to store the body of the mail 
            body = "ยอดขายรวมของวัน "+str(report_sum)+"\n"
            for i in range(10):
                print(ChickenList[i],':',report_chick[i],'ชิ้น\n')
                body+=str(ChickenList[i])+' : ' +str(report_chick[i])+' ชิ้น\n'
            # attach the body with the msg instance 
            msg.attach(MIMEText(body, 'plain')) 
            # open the file to be sent  
            filename = time.strftime(shop+"%Y%b%d")+".txt"
            attachment = open(filename, "rb") 
            # instance of MIMEBase and named as p 
            p = MIMEBase('application', 'octet-stream') 
            # To change the payload into encoded form 
            p.set_payload((attachment).read()) 
            # encode into base64 
            encoders.encode_base64(p) 
            p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
            # attach the instance 'p' to instance 'msg' 
            msg.attach(p) 
            # creates SMTP session 
            s = smtplib.SMTP('smtp.gmail.com', 587) 
            # start TLS for security 
            s.starttls() 
            # Authentication 
            s.login(fromaddr, email_pass) 
            # Converts the Multipart msg into a string 
            text = msg.as_string() 
            # sending the mail 
            s.sendmail(fromaddr, toaddr, text) 
            # terminating the session 
            s.quit()
        except:
            messagebox.showerror("เกิดข้อผิดพลาดในการส่งเมล", "กรุณาตรวจสอบความถูกต้องของ e-mail แล้วลองอีกครั้ง")
            return 0
        messagebox.showinfo("Sucsees", "ส่งไฟล์ และ Email สำเร็จ ")
    else:
        str_error=''
        if(EntryEmail.get()==''):
            str_error=str_error+'Email '
        if(EntryServer.get()==''):
            str_error=str_error+'Ftp_server '
        messagebox.showerror("กรุณากรอกข้อมูลให้ครบถ้วน", "ไม่ได้กรอก "+str_error)
def qExit():
    qExit= messagebox.askyesno("ออกจากระบบ","คุณต้องการออกจากระบบไหม?")
    if qExit > 0:
        root.destroy()
        return
def Reset():
    FrameChickenReset()
    FrameCostReset()
    txtReceipt.delete("1.0",END)
##    x = simpledialog.askstring(title="secret ftp setting",prompt="Format: user,pass")
##    print(x)
##    if x != None:
##        (x1,x2)=x.split(',')
##        print(x1,x2)

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
    ReceiveMoney.set("0")
    ChangeMoney.set("")

def chkbutton_value(chkValue,txtLabel,Entry):
    if chkValue.get() == 1:
        
        txtLabel.configure(state=NORMAL)
    elif chkValue.get() == 0:
        txtLabel.configure(state=DISABLED)
        Entry.set("0")

sum_total=0
sum_chick=[0,0,0,0,0,0,0,0,0,0]
total=0
NumOrder=0
ftp_user='boat'
ftp_pass='12345'
email_user='thanarak.s@ku.th'
email_pass='Shadowpizzax1!'
ChickensPrice=0
ChickPriceList = [50,50,50,50,200,150,100,80,80,70,50,50]
Service=0
changeM=0
changeMoney=""

def CostofItem():
    global NumOrder
    NumOrder=0
    for i in VarChickenList:
        if(i.get()!=0):
            NumOrder=NumOrder+1
    if NumOrder>8:
        messagebox.showerror("สั่งได้ไม่เกิน 8 อย่าง", "กรุณากรอกข้อมูลใหม่ ")
        Reset()
        return 0
    if VarChickenList[0].get() != 0 or VarChickenList[1].get() != 0 or VarChickenList[2].get() != 0 or VarChickenList[3].get() != 0 or VarChickenList[4].get() != 0 or VarChickenList[5].get() != 0 or VarChickenList[6].get() != 0 or VarChickenList[8].get() != 0 or VarChickenList[9].get() != 0 or VarChickenList[10].get() != 0:
        TotalChickenCost = 0
        global ChickPriceList,Service,changeM,total,ChickensPrice,changeMoney
        for i in range(12):
            try:
                x = int(EntryChickenList[i].get())
                if(x<0):
                    messagebox.showerror("มีการใส่ค่าตัวเลขติดลบ", "กรุณาตรวจสอบความถูกต้อง และ ใส่ตัวเลขใหม่")
                    EntryChickenList[i].set("0")
                    return 0
            except:
                messagebox.showerror("มีการใส่ค่าที่ไม่ถูกต้อง", "กรุณาตรวจสอบความถูกต้อง และ ใส่ตัวเลขใหม่")
                EntryChickenList[i].set("0")
                return 0
            TotalChickenCost += int(EntryChickenList[i].get())* float(ChickPriceList[i])
        ChickensPrice = str('%.2f'%(TotalChickenCost)), "บาท"
        CostofChicken.set(ChickensPrice)

        if(TotalChickenCost!=0):
            SC =  str('%.2f'%(Service)), "บาท"
            ServiceCharge.set(SC)
            CostPlus = TotalChickenCost + Service
            SubTotalofItems = str('%.2f'%(CostPlus)), "บาท"
            SubTotal.set(SubTotalofItems)
    
            Tax = str('%.2f'%(CostPlus*0.07)), "บาท"
            PaidTax.set(Tax)
            TT = CostPlus * 0.07
            total= CostPlus + TT
            TC = str('%.2f'%(CostPlus + TT)), "บาท"
            TotalCost.set(TC)
            changeM=float(ReceiveMoney.get())-total
            
            if(round(changeM,1)==0):
                changeMoney = "0.00 บาท"
            elif(round(changeM,1)<0):
                changeMoney = "***จ่ายยังไม่ครบ***"
            elif(round(changeM,1)>0):
                changeMoney = str('%.2f'%(changeM)),"บาท"
            ChangeMoney.set(changeMoney)
            

def number_format(num, places=0):
    return '{:20,.2f}'.format(num)

def ThaiBahtConversion(amount_number):
    amount_number = number_format(amount_number, 2).replace(" ","")
    pt = amount_number.find(".")
    number,fraction = "",""
    amount_number1 = amount_number.split('.')
    if (pt == False):
        number = amount_number
    else:
        amount_number = amount_number.split('.')
        number = amount_number[0]
        fraction = int(amount_number1[1]) 
    ret = ""
    number=eval(number.replace(",",""))
    baht = ReadNumber(number)
    if(number==0.0):
        return "ศูนย์บาทถ้วน"
    if (baht != ""):
        ret += baht + "บาท"
    satang = ReadNumber(fraction)
    if (satang != ""):
        ret += satang + "สตางค์"
    else:
        ret += "ถ้วน"
    return ret
 
#อ่านจำนวนตัวเลขภาษาไทย
def ReadNumber(number):
    position_call = ["แสน", "หมื่น", "พัน", "ร้อย", "สิบ", ""]
    number_call = ["", "หนึ่ง", "สอง", "สาม","สี่", "ห้า", "หก", "เจ็ด", "แปด", "เก้า"]
    number = number
    ret = ""
    if (number == 0): return ret
    if (number > 1000000):
        ret += ReadNumber(int(number / 1000000)) + "ล้าน"
        number = int(math.fmod(number, 1000000))
    divider = 100000
    pos = 0
    while(number > 0):
        d=int(number/divider)
        if (divider == 10) and (d == 2):
            ret += "ยี่"
        elif (divider == 10) and (d == 1):
            ret += ""
        elif ((divider == 1) and (d == 1) and (ret != "")):
            ret += "เอ็ด"
        else:
            ret += number_call[d]
        if(d):
            ret += position_call[pos]
        else:
            ret += ""
        number=number % divider
        divider=divider / 10
        pos += 1
    return ret

totalday=0       
def Receipt():
    global NumOrder,sum_total,sum_chick
    if VarChickenList[0].get() != 0 or VarChickenList[1].get() != 0 or VarChickenList[2].get() != 0 or VarChickenList[3].get() != 0 or VarChickenList[4].get() != 0 or VarChickenList[5].get() != 0 or VarChickenList[6].get() != 0 or VarChickenList[8].get() != 0 or VarChickenList[9].get() != 0 or VarChickenList[10].get() != 0:
        if(round(changeM,1)>=0):
            for i in EntryChickenList:
                print(i.get())
            shop = "Chick-ka-boo"
            fileName = time.strftime(shop+"%Y%b%d")+".txt"
            rg = open(fileName,'a',encoding="utf-8")
            txtReceipt.delete("1.0",END)
            x = random.randint(10908,500876)
            randomRef = str(x)
            ReceiptRef.set("BILL"+randomRef)
            txtReceipt.insert(END,'หมายเลขใบเสร็จ :\t\t\t'+ ReceiptRef.get()  + '\t\t' + DateofOrder.get() + "\n")
            txtReceipt.insert(END,'รายการ\t'+ str('%d'%(NumOrder))+'\t\t'+ 'จำนวน \t'+ str('%.2f'%total)+'\t'+ " ราคา  \n\n")
            NumOrder+=1
            rg.write('หมายเลขใบเสร็จ:'+ReceiptRef.get()+ '\t\t' + DateofOrder.get() + "\n")
            rg.write('รายการ\t'+ str('%d'%(NumOrder))+'\t\t'+ 'จำนวน \t'+ str('%.2f'%total)+'\t'+ " ราคา  \n\n")
            for i in range(10) :
                if int(EntryChickenList[i].get()) > 0 :
                    sum_chick[i]+=int(EntryChickenList[i].get())
                    txtReceipt.insert(END, ChickenList[i] +'\t\t'+'('+str(ChickPriceList[i])+')'+'\t'+ str(int(EntryChickenList[i].get())) + "\t\t" + str( '%.2f'%(ChickPriceList[i]* int(EntryChickenList[i].get()) ) ) +'\n')
                    rg.write(ChickenList[i] +'\t\t'+'('+str(ChickPriceList[i])+')'+'\t'+ str(int(EntryChickenList[i].get())) + "\t\t" + str( '%.2f'%(ChickPriceList[i]* int(EntryChickenList[i].get()) ) ) +'\n')

##            txtReceipt.insert(END,'\nค่าบริการ : \t\t'+ str('%.2f'%Service)+ "\tบาท\t( "+ThaiBahtConversion(Service) + ' )\n')        
            txtReceipt.insert(END,'ราคารวมสุทธิ : \t\t'+ str('%.2f'%total)+ "\tบาท\t( "+ThaiBahtConversion(total) + ' )\n')
            sum_total=sum_total+total
            txtReceipt.insert(END,'รับเงิน : \t\t'+ str('%.2f'%float(ReceiveMoney.get())) +"\tบาท\t( "+ThaiBahtConversion(float(ReceiveMoney.get())) + ' )\n')
            txtReceipt.insert(END,'เงินทอน : \t\t'+ str('%.2f'%abs(round(changeM,2))) +"\tบาท\t( "+ThaiBahtConversion(changeM) + ' )\n')

##            rg.write('\nค่าบริการ : \t\t'+ str('%.2f'%Service)+ "\tบาท\t( "+ThaiBahtConversion(Service) + ' )\n')
            rg.write('ราคารวมสุทธิ : \t\t'+ str('%.2f'%total)+ "\tบาท\t( "+ThaiBahtConversion(total) + ' )\n')
            rg.write('รับเงิน : \t\t\t'+ str('%.2f'%float(ReceiveMoney.get())) +"\tบาท\t( "+ThaiBahtConversion(float(ReceiveMoney.get())) + ' )\n')
            rg.write('เงินทอน : \t\t\t'+ str('%.2f'%abs(round(changeM,2))) +"\tบาท\t( "+ThaiBahtConversion(changeM) + ' )\n')
            rg.write("---------------------------------------------------------------\n")
            str1 = "["
            for i in range(10):
                str1+=str(sum_chick[i])
                if i !=9:
                    str1+=','
            str1+=']'
            rg.write(str(sum_total)+' '+str1+'\n')
            rg.write("---------------------------------------------------------------\n")
            rg.close()
        elif(round(changeM,1)<0):
            txtReceipt.delete("1.0",END)
            txtReceipt.insert(END,"***ยังจ่ายเงินไม่ครบ***")

#====================== Variable Chicken =====================
ReceiptRef = StringVar()
DateofOrder = StringVar()
DateofOrder.set(time.strftime("%d/%m/%Y"))

ChickenList = ["ไก่ทอดสไปซี่ 50 บาท","ไก่ทอดต้มยำ 50 บาท","ไก่นุ่ม 50 บาท","ข้าวยำไก่แซ่บ 50 บาท",
            "ไก่ทอดชุดครอบครัว 200 บาท","ชุดไก่สารพัด 150 บาท","ไก่ทอดเกาหลี 100 บาท","ชุดไก่ปิคนิก 80 บาท",
            "เคบับไก่ 80 บาท","เบอร์เกอร์ไก่ 70 บาท"]

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

Chicken8 = Checkbutton(fChicken22, text=ChickenList[7],variable = VarChickenList[8],onvalue = 1, offvalue=0,
                    font=('TH Sarabun New',14,'bold'),command=lambda:chkbutton_value(VarChickenList[8],txtChicken8,EntryChickenList[8])).grid(row= 1,column=0, sticky=W)
Chicken9 = Checkbutton(fChicken22 , text=ChickenList[8],variable = VarChickenList[9],onvalue = 1, offvalue=0,
                    font=('TH Sarabun New',14,'bold'),command=lambda:chkbutton_value(VarChickenList[9],txtChicken9,EntryChickenList[9])).grid(row= 1,column=2, sticky=W)
Chicken10 = Checkbutton(fChicken22 , text=ChickenList[9],variable = VarChickenList[10],onvalue = 1, offvalue=0,
                    font=('TH Sarabun New',14,'bold'),command=lambda:chkbutton_value(VarChickenList[10],txtChicken10,EntryChickenList[10])).grid(row= 1,column=4, sticky=W)
#Chicken11 = Checkbutton(fChicken2 , text=ChickenList[11],variable = VarChickenList[11],onvalue = 1, offvalue=0,
                    #font=('TH Sarabun New',12,'bold'),command=lambda:chkbutton_value(VarChickenList[11],txtChicken11,EntryChickenList[11])).grid(row= 11, sticky=W)

#=======================Enter Widgets for Chicken =======================
txtChicken0 = Entry(fChicken00 ,font=('TH Sarabun New',12,'bold'),bd=5,width=3,justify='right',textvariable=EntryChickenList[0],state = DISABLED)
txtChicken0.grid(row=0,column =2)
txtChicken1 = Entry(fChicken00 ,font=('TH Sarabun New',12,'bold'),bd=5,width=6,justify='right',textvariable=EntryChickenList[1],state = DISABLED)
txtChicken1.grid(row=0,column =4)
txtChicken2 = Entry(fChicken00 ,font=('TH Sarabun New',12,'bold'),bd=5,width=3,justify='right',textvariable=EntryChickenList[2],state = DISABLED)
txtChicken2.grid(row=0,column =6)
txtChicken3 = Entry(fChicken00 ,font=('TH Sarabun New',12,'bold'),bd=5,width=3,justify='right',textvariable=EntryChickenList[3],state = DISABLED)
txtChicken3.grid(row=0,column =8)

txtChicken4 = Entry(fChicken11 ,font=('TH Sarabun New',12,'bold'),bd=5,width=9,justify='right',textvariable=EntryChickenList[4],state = DISABLED)
txtChicken4.grid(row=1,column =1)
txtChicken5 = Entry(fChicken11 ,font=('TH Sarabun New',12,'bold'),bd=5,width=6,justify='right',textvariable=EntryChickenList[5],state = DISABLED)
txtChicken5.grid(row=1,column =3)
txtChicken6 = Entry(fChicken11 ,font=('TH Sarabun New',12,'bold'),bd=5,width=5,justify='right',textvariable=EntryChickenList[6],state = DISABLED)
txtChicken6.grid(row=1,column =5)
#txtChicken7 = Entry(fChicken1 ,font=('TH Sarabun New',12,'bold'),bd=5,width=6,justify='left',textvariable=EntryChickenList[7],state = DISABLED)
#txtChicken7.grid(row=7,column =1)

txtChicken8 = Entry(fChicken22 ,font=('TH Sarabun New',12,'bold'),bd=5,width=7,justify='right',textvariable=EntryChickenList[7],state = DISABLED)
txtChicken8.grid(row=1,column =1)
txtChicken9 = Entry(fChicken22 ,font=('TH Sarabun New',12,'bold'),bd=5,width=3,justify='right',textvariable=EntryChickenList[8],state = DISABLED)
txtChicken9.grid(row=1,column =3)
txtChicken10 = Entry(fChicken22 ,font=('TH Sarabun New',12,'bold'),bd=5,width=6,justify='right',textvariable=EntryChickenList[9],state = DISABLED)
txtChicken10.grid(row=1,column =5)

#===============================Variable Calculation =====================
PaidTax = StringVar()
SubTotal = StringVar()
TotalCost = StringVar()
CostofChicken = StringVar()
ServiceCharge = StringVar()
ReceiveMoney = StringVar()
ReceiveMoney.set("0")
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

lblReceiveMoney = Label(fCost3,font=('TH Sarabun New',12,'bold'),text="รับเงิน",bd=5,bg="Dark Orange")
lblReceiveMoney.grid(row=0,column=0,sticky=W)
txtReceiveMoney=Entry(fCost3,font=('TH Sarabun New',12,'bold'),bd=5,justify='right',
                   textvariable=ReceiveMoney,bg="white")
txtReceiveMoney.grid(row=0,column=1,sticky=W)

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
                text="เปลี่ยน user,pass ของ FTP เซิฟเวอร์",command=serverAccess).grid(row=1, column=2)
btnEmail=Button(fRemail,padx=22, fg="black",font=('TH Sarabun New',12,'bold'),width=5,
                text="เปลี่ยน user,pass ของอีเมล์",command=emailAccess).grid(row=2, column=2)
btnSendFile=Button(fRsendfile_1,padx=30, fg="black",font=('TH Sarabun New',18,'bold'),width=5,
                text="ยืนยัน",command=sendFile).grid(row=3, column=1)

root.mainloop()

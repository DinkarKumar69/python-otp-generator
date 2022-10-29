from logging import root
import numbers
from tkinter import *
import tkinter.messagebox as tmb
import requests
import random
import json

root = Tk()
rand = random.randint(1,999990)

msg = f"Your One Time Passsword(OTP) is {9939098317}"

def sms_send(a,msg):
    url = "https://www.fast2sms.com/dev/bulk"
    params ={
        "authorization":"5uNzsybWDniEwtCOeoKG3mM4aVU8xgSlBdZ6XJRjFQfqp9Hh1AS0WkBHLby93V2DdUrniGOjtFQlvN7J",
        "sender_id":"Cghpet",
        "message":msg,
        "language":"english",
        "route":"p",
        "numbers":a
    }
    rs = requests.get(url,params=params)

def send():
    a=num.get()
    if(a==""):
         tmb.showerror("Error", "Enter Your Mobile Number")
    elif(len(a)<10):
        tmb.showerror("Error","Invalid!Mobile Number")
        num.set("")
    else:
        b=tmb.askyesno("Info",f"Your Number is {a}")
        if (b==True):
            sms_send(a,msg)
        else:
            num.set("")

def check():
    c=otp.get()
    if(c==""):
        tmb.showerror("Error","Enter OTP")
    else:
        if(str(rand)==c):
            tmb.showinfo("Info","Successfull")
        else:
            tmb.showerror("Error", "Invalid OTP!")
            num.set("")
            otp.set("")

root.geometry("400x350")
root.title("OTP-Checker")

num=StringVar()
otp=StringVar()

f1=Frame(root)
Label(f1,text="Check Your OTP",font="SegoeUI 30 bold",fg="Grey").pack(padx=5,pady=10)
f1.pack(fill=BOTH)

f2=Frame(root)
Label(f2,text="Enter Your Number",font="SegoeUI 20 bold",fg="grey").pack(padx=5,pady=5)
e1=Entry(f2,textvariable=num,font="SegoeUI 14 bold",fg="black",bg="white",relief=SUNKEN,borderwidth=4,justify="center").pack(ipady=5)
f2.pack(fill=BOTH,padx=5,pady=10)

f3=Frame(root)
Label(f3,text="Enter OTP",font="SegoeUI 20 bold",fg="grey").pack(padx=5,pady=5)
e2=Entry(f3,textvariable=otp,font="SegoeUI 14 bold",fg="black",bg="white",relief=SUNKEN,borderwidth=5,justify="center").pack(ipady=5)
f3.pack(fill=BOTH,padx=5,pady=10)

f4=Frame(root)
Button(f4,text="Send OTP",command=send,font="SegoeUI 10 bold",fg="grey").pack(padx=20,pady=10,side=LEFT)
Button(f4,text="Check OTP",command=check,font="SegoeUI 10 bold",fg="grey").pack(padx=40,pady=10,side=LEFT)
f4.pack()


root.mainloop()

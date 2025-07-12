import time
import pygame as p
import random as r
import pywhatkit as pk
import pyautogui as pg

p.init()
p.display.set_caption("Mobile Express")
ps1=p.display.set_mode((400,400))
ps=p.image.load("images.png")
ps1.blit(ps,(10,50))
p.display.update()
time.sleep(5)
p.quit()

print("--------------------------------MOBILE EXPRESS----------------------------------")
name=input("ENTER YOUR NAME :")
age=int(input("ENTER YOUR AGE :"))
gender=input("ENTER YOUR GENDER :")
password=int(input("ENTER YOUR PASSWORD :"))

print("LOGIN FORM")

def h1():
    user=input("USER :")
    if user==name:
        p1= int(input("ENTER YOUR PASSWORD :"))
        if p1==password:
            print("LOGIN SUCCESSFUL")
        else:
            print("PASSWORD INCORRECT")
    else:
        print("USERNAME INCORRECT")
        h1()
h1()

print("AVAIABLE BRANDS")
a = ["1.VIVO", "2.OPPO", "3.SAMSUNG"]
for i in a:
    print(i)

def h_1():
    print("AVAIABLE BRANDS")
    a = ["1.VIVO", "2.OPPO", "3.SAMSUNG"]
    for i in a:
        print(i)

def payment():
    print("Available payment methods :")
    a=["1.Gpay","2.COD"]
    for i in a:
        print(i)
    pay1=int(input("select your payment method :"))
    if pay1==1:
        mob=int(input("Enter your mobile number :"))
        upi=int(input("Enter your upi id :"))
        amount=int(input("Enter the amount :"))
        if amount==q_1:
            print("order successful")
            bill = """
            **********************************
            Name        : {}
            mobile      : {}
            Product     : VIVO V15
            price       : {}
            **********************************
            """
            wm=bill.format(name1,mobile1,q_1)
            pk.sendwhatmsg_instantly("+91 7598152270",wm)
            time.sleep(5)
            pg.doubleClick()
        else:
            print("Enter the correct amount :")
            payment()
    elif pay1==2:
        print("DELIVERY CHARGE RS: 50")
        amount = int(input("Enter the amount :"))
        if amount == q_1:
            q0=q_1+50
            print("Total amount :",q0)
            print("order successful")
        else:
            print("Enter the correct amount :")
            payment()
    else:
        print("=============================== PAYMENT METHOD NOT AVAILABLE ==========================")
        payment()

def address():
    buy=input("ARE YOU READY TO BUY : YES/NO :")
    if buy=="yes":
        global name1,mobile1
        name1=input("ENTER YOUR FULL NAME :")
        mobile1=int(input("ENTER YOUR MOBILE NUMBER :"))
        state=input("ENTER YOUR STATE :")
        city=input("ENTER YOUR CITY :")
        door_no=int(input("ENTER YOUR DOOR NUMBER :"))
        street=input("ENTER YOUR STREET NAME :")
        payment()

    else:
        print("================ T H A N K Y O U =====================")

def im_p(im):
    p.init()
    p.display.set_caption("Mobile Express")
    ps1 = p.display.set_mode((200,250))
    ps = p.image.load(im)
    ps1.blit(ps,(10,10))
    p.display.update()
    time.sleep(5)
    p.quit()

def model():
    global q_1
    print("1.VIVOV5", "2.VIVOV11")
    model=int(input("enter your model :"))
    if model==1:
        print("VILVO MODES")
        b=r.randint(15000,20000)
        print("PRICE",b)
        im_p("oppo f7.jpg")
        q1=int(input("enter the quantity :"))
        q_1=q1*b
        print("TOTAL PRICE",q_1)
        address()
    elif model==2:
        print("VIVOV11")
        c=r.randint(20000,30000)
        print("PRICE",c)
        p.init()
        p.display.set_caption("Mobile Express")
        ps1=p.display.set_mode((400, 400))
        ps=p.image.load("vivo v11.jpg")
        ps1.blit(ps, (10, 10))
        p.display.update()
        time.sleep(5)
        p.quit()
        q1=int(input("enter the quantity :"))
        q_1=q1*c
        print("TOTAL PRICE :",q_1)
        address()

def h2():
    global q_1
    print("OPPO MODELS")
    print("1.OPPO F7","2.OPPO F27")
    model=int(input("SELECT YOUR BRAND"))
    if model==1:
        d=r.randint(5000,10000)
        print("PRICE :",d)
        p.init()
        p.display.set_caption("Mobile Express")
        ps1=p.display.set_mode((200,200))
        ps=p.image.load("oppo f7.jpg")
        ps1.blit(ps, (10, 10))
        p.display.update()
        time.sleep(5)
        p.quit()
        q1=int(input("enter the quantity :"))
        q_1=q1*d
        print("TOATL PRICE",q_1)
        address()

    elif model==2:
        e=r.randint(35000,40000)
        print(e)
        p.init()
        p.display.set_caption("Mobile Express")
        ps1=p.display.set_mode((200,200))
        ps=p.image.load("oppo f27.jpg")
        ps1.blit(ps, (10, 10))
        p.display.update()
        time.sleep(5)
        p.quit()
        q1=int(input("enter the quantity :"))
        q_1=q1*e
        print("TOTAL PRICE :",q_1)
        address()



def h3():
    global q_1
    print("SAMSUNG MODELS")
    print("1.SAMSUNG S20","2.SAMSUNGS24 ULTRA 5G")
    model=int(input("SELECT YOUR BRAND"))
    if model==1:
        f=r.randint(5000, 10000)
        print("PRICE",f)
        p.init()
        p.display.set_caption("Mobile Express")
        ps1=p.display.set_mode((200,200))
        ps=p.image.load("SAMSUNG S20.jpg")
        ps1.blit(ps, (10, 10))
        p.display.update()
        time.sleep(5)
        p.quit()
        q1=int(input("ENTER THE QUANTITY :"))
        q_1=q1*f
        print("TOTAL PRICE :",q_1)
        address()
    elif model==2:
        g=r.randint(35000, 40000)
        print("PRICE :",g)
        p.init()
        p.display.set_caption("Mobile Express")
        ps1=p.display.set_mode((200,200))
        ps=p.image.load("SAMSUNG S24 ULTRA 5G.jpg")
        ps1.blit(ps, (10, 10))
        p.display.update()
        time.sleep(5)
        p.quit()
        q1=int(input("ENTER THE QUANTITY :"))
        q_1=q1*g
        print("TOTAL PRICE :",q_1)
        address()

def brand():
    brand=int(input("SELECT YOUR BRAND"))
    if brand==1:
        print("vivo")
        model()

    elif brand==2:
        print("oppo")
        h2()

    elif brand==3:
        print("samsung")
        h3()
    else:
        print("Invalid brand ")
        brand()

brand()

























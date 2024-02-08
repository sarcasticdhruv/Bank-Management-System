import tkinter as tk
from operator import truediv
from prettytable import PrettyTable
from datetime import datetime
import random
import psycopg2
import time
import db_config

global name_ac

#configuring db
con=psycopg2.connect(
    database=db_config.DATABASE,
    user=db_config.USER,
    password=db_config.PASSWORD,
    port=db_config.PORT
)

#configuring tkinter gui
window=tk.Tk()
window.title("Bank Managment System")

# sign_in_label=

def intro():
    print("\n\t\t\t\t\tATM - Automated Teller Machine")
    for i in "\t\t\t\t\tIn Other WOrDs \"aNY tIME mONEY\"":
        time.sleep(0.1)
        print(i,end="")

    print("\n\n\t\t\t\tWelcome,My Name is",end=" ")
    for i in "MARCO":
        time.sleep(0.3)
        print(i,end=" ")
    print("\t+~^~+")
    print("\t\t\t\t\t\t\t\t|+ +|") 
    print("\t\t\t\t\t\t\t\t| - |")   
    print("\t\t\t\t\t\t\t\t+---+")   
    print("\n\t\t\tHow can I be at service",end="")
    for i in ".....":
        time.sleep(0.1)
        print(i,end="")
    print("\n")

def withdrawl(name_ac,warn):
    if warn[0]!=3:
        c_obj=con.cursor()
        c_obj.execute("select Pin,Amount,card from accounts where name='"+name_ac+"'")
        out=c_obj.fetchall()
        pin_ch=int(input("Enter your PIN : "))
        if out[0][0]==pin_ch:
            debit=float(input("Enter the Amount to Widhrawl (Rs): "))
            if int(out[0][1])-debit<0:
                print("Insufficient Funds!!!")
            
            if debit<100:
                print("Enter Amount more than Rs. 100\-")

            else:
                command=("update accounts set amount="+str(out[0][1]-debit)+" where name='"+name_ac+"'")
                c_obj.execute(command)
                con.commit()

                add_transac("debit",out[0][2],debit)

                print("Rs. ",debit,"\- debited Succesfully...")
                input("Press Enter to Continue.....")
                print("\n")
        else:
            print("Invalid PIN")
            warn[0]+=1

    else:
        print("Your Account has been Temporary Logged Out due to security reasons")

def deposit(name_ac,warn):
    if warn[0]!=3:
        c_obj=con.cursor()
        c_obj.execute("select Pin,Amount,card from accounts where name='"+name_ac+"'")
        out=c_obj.fetchall()
        pin_ch=int(input("Enter your PIN : "))
        if out[0][0]==pin_ch:
            credit=float(input("Enter the Amount to Deposited (Rs): "))
            command=("update accounts set amount="+str(out[0][1]+credit)+" where name='"+name_ac+"'")
            c_obj.execute(command)
            con.commit()

            add_transac("credit",out[0][2],credit)

            print("Rs. ",credit,"\- credited Succesfully...")
            input("Press Enter to Continue.....")
            print("\n")
        else:
            print("Invalid PIN")
            warn[0]+=1
            
    
    else:
        print("Your Account has been Temporary Logged Out due to security reasons")

def balance(name_ac):
    c_obj=con.cursor()
    c_obj.execute("select Pin,Amount from accounts where name='"+name_ac+"'")
    out=c_obj.fetchall()
    bal=out[0][1]
    print("\nYour Balance = Rs. ",bal,"/-\n")
    input("Press Enter to Continue.....")
    print("\n")

def auth():
    card=int(input("\nEnter your Card Number : "))
    c_obj=con.cursor()
    c_obj.execute("select card from accounts")
    out=c_obj.fetchall()
    for rec in out:
        if rec[0]==card:
            c_obj.execute("select name from accounts where card="+str(rec[0]))
            output=c_obj.fetchall()
            name_ac=output[0][0]
            ob=str(greet())
            print("\n",ob,name_ac,"\n")
            st=False
            return name_ac
        else:
            st=True
    if st:
        print("Invalid Card!!!\n")


def add_transac(it,card,amount):
    c_obj=con.cursor()

    t_id=random.randint(111111,999999)
    td=datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    info=(t_id,card,td,amount,it)
    c_obj.execute("insert into transactions(transaction_id,card,datetime,amount,type) values"+str(info))
    con.commit()

def show_transac(name_ac):
    c_obj=con.cursor()
    c_obj.execute("select card from accounts where name='"+name_ac+"'")
    out=c_obj.fetchall()
    #c_obj.execute("select transaction_id,amount,type,datetime from transactions where card="+str(out[0][0]))
    c_obj.execute("select row_number() over (order by datetime) as s_no,transaction_id,amount,type,datetime from transactions where card="+str(out[0][0]))
    
    table=PrettyTable(["S.No","Transaction ID","Amount (In Rs)","Transaction Type","Date Time"])
    out=c_obj.fetchall()
    print("\nTransactions : ")
    for row in out:
        table.add_row(row)
    
    print(table)

def greet():
    t=int(datetime.now().strftime("%H"))
    
    if t>=5 and t<12:
        greeting="Good Morning"
    elif t>=12 and t<16:
        greeting="Good Afternoon"
    elif t>=16 and t<=23:
        greeting="Good Evening"
    else:
        greeting="Hey there, "
    return greeting
#main
while True:
    intro()
    print("1. Login")
    print("2. Exit")
    ch=int(input("Choose.....: "))
    if ch==1:
        status="logged_out"
        warn=[0]
        while(True):
            
            if status=="logged_out":
                name_ac=auth()
                if name_ac:
                    status="logged_in"
                    continue
                else:
                    break
        
            print("\nWhat would you like to do?")
            print("1. CASH Widhdrawl")
            print("2. CASH Depsoit")
            print("3. Check Account Balance")
            print("4. Show Transactions")
            print("5. Logout")

            var=int(input("Choose from the above options [1-5]:- "))

            if var==1:
                withdrawl(name_ac,warn)

            elif var==2:
                deposit(name_ac,warn)

            elif var==3:
                balance(name_ac)

            elif var==4:
                show_transac(name_ac)

            elif var==5:
                print("Logged Out SUccesfully!\n")
                break

            else:
                print("Invalid Choice\nRETRY!!!")
    elif ch==2:
        break

    else:
        print("Invalid!!!")
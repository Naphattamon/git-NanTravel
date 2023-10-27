from tkinter import *
from tkinter import messagebox
import sqlite3
from tkinter import ttk
from tkmacosx import Button

def mainwindow() :
    main = Tk()
    w = 1300
    h = 800
    x = main.winfo_screenwidth()/2 - w/2
    y = main.winfo_screenheight()/2 - h/2
    main.geometry("%dx%d+%d+%d"%(w,h,x,y))
    main.configure(bg="White")
    main.title("PLAN NAN : ")
    main.option_add('*font',"Time 22 bold")
    main.rowconfigure((0),weight=1)
    main.columnconfigure((0),weight=1)
    return main

def createconnection() :
    global conn,cursor
    conn = sqlite3.connect('project.db')
    cursor = conn.cursor()

def wellcome() :
    global main,logo
    logo = logo.subsample(5)
    frm = Frame(main,bg="White")
    frm.grid(row=0,column=0,sticky='news')
    Label(frm,image=logo,bg="White").pack(pady=80)
    Label(frm,text='PLAN NAN',bg="White",font="Time 40 bold").pack()
    Button(frm,text=' > ',width=40,command = start).pack(pady=25)


def start():
    global main,logo
    logo = PhotoImage(file='logo/logo.png')
    logo = logo.subsample(7)
    frm = Frame(main,bg="White")
    frm.grid(row=0,column=0,sticky='news')
    Label(frm,image=logo,bg="White").pack(pady=80)
    Button(frm,text='Login',width=300,height=60,font="Time 25 bold",bg='black',fg='white',command=login).pack(pady=5)
    Button(frm,text='Registration',width=300,height=60,font="Time 25 bold",bg='black',fg='white',command=creatregister).pack(pady=5)
    Button(frm,text='Exit',width=300,height=60,font="Time 25 bold",bg='black',fg='white',command=exit).pack(pady=5)

def login():
    global main

    var_user.set('')
    var_pwd.set('')
   
    frm = Frame(main,bg="black")
    frm.grid(row=0,column=0,sticky='news')
    frm.rowconfigure((0),weight=1)
    frm.columnconfigure((0),weight=1)

    frm_bg = Frame(frm,bg="white")
    frm_bg.grid(row=0,column=0,padx=50,pady=50,sticky='news')
    frm_bg.rowconfigure((0,3),weight=1)
    frm_bg.columnconfigure((0,1),weight=1)

    global logo
    logo = PhotoImage(file='logo/logo.png')
    logo = logo.subsample(7)
    Label(frm_bg,image=logo,bg='white',bd=0).grid(row=0,column=0,columnspan=2)
    Label(frm_bg,text="USERNAME : ",bg='white').grid(row=1,column=0,padx=10,pady=20,sticky='e')
    Label(frm_bg,text="PASSWORD : ",bg='white').grid(row=2,column=0,padx=10,pady=20,sticky='e')
    Entry(frm_bg,width=20,textvariable=var_user).grid(row=1,column=1,padx=10,pady=20,sticky='w')
    Entry(frm_bg,width=20,show='*',textvariable=var_pwd).grid(row=2,column=1,padx=10,pady=20,sticky='w')
    Button(frm_bg,text='Login',height=50,font="Time 25 bold",bg='black',fg='white',command=loginclick).grid(row=3,column=1,columnspan=2,padx=50,pady=20,sticky='w')
    Button(frm_bg,text='Back',height=50,font="Time 25 bold",bg='black',fg='white',command=start).grid(row=3,column=0,padx=50,pady=20,sticky='e')


def loginclick() :
    if var_user.get() == "" :
        messagebox.showwarning("Admin:","Pleas enter username")
    else :
        sql = "select * from member where user=?"
        cursor.execute(sql,[var_user.get()])
        result = cursor.fetchall()
        if result :
            if var_pwd.get() == "" :
                messagebox.showwarning("Admin:","Please enter password")
            else :
                sql = "select * from member where user=? and pwd=? "
                cursor.execute(sql,[var_user.get(),var_pwd.get()])
                info = cursor.fetchone()
                if info :
                    messagebox.showinfo("Admin:","Login Successfully")
                    print(info)
                    name.set(info[1]+' '+info[1])
                    date.set(info[3])
                    gen.set(info[4])
                    choosemenu()
                else :
                    messagebox.showwarning("Admin:","Incorrect Password")
        else :
            messagebox.showerror("Admin:","Username not found\n Please register before Login")

def creatregister():
    global main
    frm = Frame(main,bg="black")
    frm.grid(row=0,column=0,sticky='news')
    frm.rowconfigure((0),weight=1)
    frm.columnconfigure((0),weight=1)

    frm_bg = Frame(frm,bg="lightgrey")
    frm_bg.grid(row=0,column=0,padx=50,pady=50,sticky='news')
    frm_bg.rowconfigure((0),weight=1)
    frm_bg.rowconfigure((1),weight=10)
    frm_bg.columnconfigure((0),weight=1)

    frm_top = Frame(frm_bg,bg='white')
    frm_top.grid(row=0,column=0,pady=5,padx=5,sticky='news')
    frm_top.rowconfigure((0,1),weight=1)
    frm_top.columnconfigure((0),weight=1)
    global logo
    logo = PhotoImage(file='logo/logo.png')
    logo = logo.subsample(20)
    Label(frm_top,image=logo,bg='white',bd=0).pack(pady=10)
    Label(frm_top,text="Registration Form",bg='white').pack()

    frm_register = Frame(frm_bg,bg='white')
    frm_register.grid(row=1,column=0,padx=5,pady=5,sticky='news')
    frm_register.rowconfigure((0,1,2,3,4,5,6,7,8,9,10,11),weight=1)
    frm_register.columnconfigure((0,1),weight=1)

    Label(frm_register,text='Full name : ',bg='white').grid(row=0,column=0,sticky='se',padx=10,pady=10)
    Label(frm_register,text='Last name : ',bg='white').grid(row=1,column=0,sticky='e',padx=10,pady=5)
    Label(frm_register,text="Birth Day : ",bg='white').grid(row=2,column=0,sticky='e',padx=10,pady=5)
    Label(frm_register,text="Username : ",bg='white').grid(row=8,column=0,sticky='e',padx=10,pady=5)
    Label(frm_register,text="Password : ",bg='white').grid(row=9,column=0,sticky='e',padx=10,pady=5)
    Label(frm_register,text="Confirm Password : ",bg='white').grid(row=10,column=0,sticky='e',padx=10,pady=5)
    
    fullname = Entry(frm_register,width=20,bg='#d3e0ea',textvariable=var_fname)
    fullname.grid(row=0,column=1,sticky='sw',padx=10,pady=10)
    lastname = Entry(frm_register,width=20,bg='#d3e0ea',textvariable=var_lname)
    lastname.grid(row=1,column=1,sticky='w',padx=10,pady=5)
    newuser = Entry(frm_register,width=20,bg='#d3e0ea',textvariable=var_newuser)
    newuser.grid(row=8,column=1,sticky='w',padx=10,pady=5)
    newpwd = Entry(frm_register,width=20,bg='#a1cae2',textvariable=var_newpwd,show='*')
    newpwd.grid(row=9,column=1,sticky='w',padx=10,pady=5)
    cfpwd = Entry(frm_register,width=20,bg='#a1cae2',textvariable=var_cfpwd,show='*')
    cfpwd.grid(row=10,column=1,sticky='w',padx=10,pady=5)
    

    var_gen.set("")
    Label(frm_register,text="Gender : ",bg='white').grid(row=5,column=0,sticky='e',padx=10,pady=5)
    Radiobutton(frm_register,text='Male',variable=var_gen,value='male',bg='white').grid(row=5,column=1,sticky='w',padx=10,pady=5)
    Radiobutton(frm_register,text='Female',variable=var_gen,value='female',bg='white').grid(row=6,column=1,sticky='w',padx=10,pady=5)
    Radiobutton(frm_register,text='Other',variable=var_gen,value='other',bg='white').grid(row=7,column=1,sticky='w',padx=10,pady=5)
    
    dd = Spinbox(frm_register,from_=1,to=31, justify=LEFT, width=10)
    dd.grid(row=2,column=1,sticky='w',padx=10,pady=5)
    mm = Spinbox(frm_register,from_=1,to=12, justify=LEFT, width=10)
    mm.grid(row=3,column=1,sticky='w',padx=10,pady=5)
    yy = Spinbox(frm_register,from_=1900,to=2021,justify=LEFT, width=10)
    yy.grid(row=4,column=1,sticky='w',padx=10,pady=5)

    Button(frm_register,text='Back',bg='black',height=50,fg='white',font="Time 15 bold",command=start).grid(row=11,column=0,padx=50,pady=20,sticky='e')
    Button(frm_register,text='Registration now',bg='black',height=50,fg='white',font="Time 15 bold",command=lambda:checkregistration(dd.get(),mm.get(),yy.get())).grid(row=11,column=1,padx=50,pady=20,sticky='w')
    
    
def checkregistration(dd,mm,yy) :
    if var_fname.get() == "" :
        messagebox.showwarning("Admin:","Please enter firstname")
    elif var_lname.get() == "" :
        messagebox.showwarning("Admin:","Please enter lastname")
    elif var_gen.get() == "" :
        messagebox.showwarning("Admin:","Please enter gender")
    elif var_newuser.get() == "" :  
        messagebox.showwarning("Admin:","Please enter new username")
    elif var_newpwd.get() == "" :   
        messagebox.showwarning("Admin:","Please enter new password")
    elif var_cfpwd.get() == "" :
        messagebox.showwarning("Admin:","Please enter confirm password")
    else:
        sql = "SELECT * FROM  member WHERE user = ?"
        cursor.execute(sql,[var_newuser.get()])
        result = cursor.fetchall()
        if result :
            messagebox.showwarning("Admin:","Username is already exists\nPlease try again")
        else :
                if var_newpwd.get() == var_cfpwd.get() :
                    
                    birthday = str(dd) + "-" + str(mm) + "-" + str(yy)
                    sql = "insert into member(fname,lname,birthday,gender,user,pwd) values (?,?,?,?,?,?)"
                    cursor.execute(sql,[var_fname.get(),var_lname.get(),birthday,var_gen.get(),var_newuser.get(),var_newpwd.get()])
                    conn.commit()
                    messagebox.showinfo("Admin:","Register Successfully")
                    var_fname.set("")
                    var_lname.set("")
                    var_gen.set("")
                    var_newuser.set("")
                    var_newpwd.set("")
                    var_cfpwd.set("")
                else :
                    messagebox.showwarning("Admin:","The confirm password not match")



def choosemenu():
    global main
    global logo
    logo = PhotoImage(file='logo/logo.png')
    logo = logo.subsample(30)

    frm = Frame(main,bg="White")
    frm.grid(row=0,column=0,sticky='news')
    frm.rowconfigure((0),weight=1)
    frm.rowconfigure((1),weight=7)
    frm.columnconfigure((0,1,2,3,4),weight=1)
    user = Button(frm,image=logo,text="  " + var_user.get(),bg='white',font="Time 20 bold",bd=0,compound=LEFT,command=showinfouser)
    user.grid(row=0,column=0,columnspan=4,sticky='nw')
    Button(frm,text='LogOut',height=60,font="Time 18 bold",command=start).grid(row=0,column=4,padx=5,sticky='e')

    Button(frm,image=menu01,bg='white',bd=0,cursor='hand1',command=plan).grid(row=1,column=0,padx=2,pady=5,sticky='news')
    Button(frm,image=menu02,bg='white',bd=0,cursor='hand2',command=review).grid(row=1,column=1,padx=2,pady=5,sticky='news')
    Button(frm,image=menu03,bg='white',bd=0,cursor='hand1',command=booking).grid(row=1,column=2,padx=2,pady=5,sticky='news')
    Button(frm,image=menu04,bg='white',bd=0,cursor='hand2',command=nanshop).grid(row=1,column=3,padx=2,pady=5,sticky='news')
    Button(frm,image=menu05,bg='white',bd=0,cursor='hand1',command=guide).grid(row=1,column=4,padx=2,pady=5,sticky='news')

def showinfouser():
    global main
    frm = Frame(main,bg="black")
    frm.grid(row=0,column=0,sticky='news')
    frm.rowconfigure((0),weight=1)
    frm.columnconfigure((0),weight=1)

    frm_bg = Frame(frm,bg="lightgrey")
    frm_bg.grid(row=0,column=0,padx=50,pady=50,sticky='news')
    frm_bg.rowconfigure((0),weight=1)
    frm_bg.rowconfigure((1),weight=10)
    frm_bg.columnconfigure((0),weight=1)

    frm_top = Frame(frm_bg,bg='white')
    frm_top.grid(row=0,column=0,pady=5,padx=5,sticky='news')
    frm_top.rowconfigure((0,1),weight=1)
    frm_top.columnconfigure((0),weight=1)
    global logo
    logo = PhotoImage(file='logo/logo.png')
    logo = logo.subsample(20)
    Label(frm_top,image=logo,bg='white',bd=0).pack(pady=10)
    Label(frm_top,text="Imformation",bg='white').pack()

    frm_user = Frame(frm_bg,bg='white')
    frm_user.grid(row=1,column=0,padx=5,pady=5,sticky='news')
    frm_user.rowconfigure((0,1,2,3,4),weight=1)
    frm_user.columnconfigure((0,1),weight=1)

    Label(frm_user,text='Username : ',bg='white').grid(row=0,column=0,sticky='se',padx=10,pady=10)
    Label(frm_user,text='Name : ',bg='white').grid(row=1,column=0,sticky='e',padx=10,pady=5)
    Label(frm_user,text="Birth Day : ",bg='white').grid(row=2,column=0,sticky='e',padx=10,pady=5)
    Label(frm_user,text="Gender : ",bg='white').grid(row=3,column=0,sticky='e',padx=10,pady=5)

    Label(frm_user,textvariable=var_user,bg='white').grid(row=0,column=1,sticky='sw',padx=10,pady=10)
    Label(frm_user,textvariable=name,bg='white').grid(row=1,column=1,sticky='w',padx=10,pady=5)
    Label(frm_user,textvariable=date,bg='white').grid(row=2,column=1,sticky='w',padx=10,pady=5)
    Label(frm_user,textvariable=gen,bg='white').grid(row=3,column=1,sticky='w',padx=10,pady=5)
 
    Button(frm_user,text='Back',bg='black',height=50,fg='white',font="Time 15 bold",command=choosemenu).grid(row=4,column=0,columnspan=2,padx=50,pady=20,sticky='e')


######### Plan #########
def plan():
    global main
    frm = Frame(main,bg="black")
    frm.grid(row=0,column=0,sticky='news')
    frm.rowconfigure((0),weight=1)
    frm.columnconfigure((0),weight=1)

    frm_bg = Frame(frm,bg="lightgrey")
    frm_bg.grid(row=0,column=0,padx=50,pady=50,sticky='news')
    frm_bg.rowconfigure((0,1,3),weight=1)
    frm_bg.rowconfigure((2),weight=10)
    frm_bg.columnconfigure((0),weight=1)

    frm_top = Frame(frm_bg,bg='white')
    frm_top.grid(row=0,column=0,pady=5,padx=5,sticky='news')
    frm_top.rowconfigure((0,1),weight=1)
    frm_top.columnconfigure((0),weight=1)
    global logo
    logo = PhotoImage(file='logo/logo.png')
    logo = logo.subsample(20)
    Label(frm_top,image=logo,bg='white',bd=0).pack(pady=10)
    Label(frm_top,text="PLAN",bg='white').pack()

    frm_plan = Frame(frm_bg,bg='white')
    frm_plan.grid(row=2,column=0,padx=5,sticky='news')


    def showfrm_plan():
        if ch_plan.current() == 1 :
            #editplan()
            set = find_plan('s1')
            set1 = set[0]
            frm_plan = Frame(frm_bg,bg='white')
            frm_plan.grid(row=2,column=0,padx=5,sticky='news')
            frm_plan.rowconfigure((0),weight=10)
            frm_plan.columnconfigure((0),weight=1)
            p1 = LabelFrame(frm_plan,text=' Day 1 : ',bg='lightyellow',fg='black',width=300,height=300)
            p1.grid(row=0,column=0)
            Label(p1,text=set1[1],bg='lightyellow',fg='black',font="Time 15 bold").pack(padx=20,pady=10)
            Label(p1,text=set1[2],bg='lightyellow',fg='black',font="Time 15 bold").pack(padx=20,pady=10)
            Label(p1,text=set1[3],bg='lightyellow',fg='black',font="Time 15 bold").pack(padx=20,pady=10)
            Label(p1,text=set1[4],bg='lightyellow',fg='black',font="Time 15 bold").pack(padx=20,pady=10)
    
            
            
        elif ch_plan.current() == 2 :
            #editplan()
            set = find_plan('s2')
            set1 = set[0]
            set2 = set[1]
            frm_plan = Frame(frm_bg,bg='white')
            frm_plan.grid(row=2,column=0,padx=5,sticky='news')
            frm_plan.rowconfigure((0),weight=10)
            frm_plan.columnconfigure((0,1),weight=1)
            p1 = LabelFrame(frm_plan,text=' Day 1 : ',bg='lightyellow',fg='black',width=300,height=300)
            p1.grid(row=0,column=0)
            Label(p1,text=set1[1],bg='lightyellow',fg='black',font="Time 15 bold").pack(padx=20,pady=10)
            Label(p1,text=set1[2],bg='lightyellow',fg='black',font="Time 15 bold").pack(padx=20,pady=10)
            Label(p1,text=set1[3],bg='lightyellow',fg='black',font="Time 15 bold").pack(padx=20,pady=10)
            Label(p1,text=set1[4],bg='lightyellow',fg='black',font="Time 15 bold").pack(padx=20,pady=10)
            p2 = LabelFrame(frm_plan,text=' Day 2 : ',bg='lightyellow',fg='black',width=300,height=300)
            p2.grid(row=0,column=1)
            Label(p2,text=set2[1],bg='lightyellow',fg='black',font="Time 15 bold").pack(padx=20,pady=10)
            Label(p2,text=set2[2],bg='lightyellow',fg='black',font="Time 15 bold").pack(padx=20,pady=10)
            Label(p2,text=set2[3],bg='lightyellow',fg='black',font="Time 15 bold").pack(padx=20,pady=10)
            Label(p2,text=set2[4],bg='lightyellow',fg='black',font="Time 15 bold").pack(padx=20,pady=10)
            
            
        elif ch_plan.current() == 3 :
            #editplan()
            set = find_plan('s3')
            set1 = set[0]
            set2 = set[1]
            set3 = set[2]
            frm_plan = Frame(frm_bg,bg='white')
            frm_plan.grid(row=2,column=0,padx=5,sticky='news')
            frm_plan.rowconfigure((0),weight=10)
            frm_plan.columnconfigure((0,1,2),weight=1)
            p1 = LabelFrame(frm_plan,text=' Day 1 : ',bg='lightyellow',fg='black',width=300,height=300)
            p1.grid(row=0,column=0)
            Label(p1,text=set1[1],bg='lightyellow',fg='black',font="Time 15 bold").pack(padx=20,pady=10)
            Label(p1,text=set1[2],bg='lightyellow',fg='black',font="Time 15 bold").pack(padx=20,pady=10)
            Label(p1,text=set1[3],bg='lightyellow',fg='black',font="Time 15 bold").pack(padx=20,pady=10)
            Label(p1,text=set1[4],bg='lightyellow',fg='black',font="Time 15 bold").pack(padx=20,pady=10)
            p2 = LabelFrame(frm_plan,text=' Day 2 : ',bg='lightyellow',fg='black',width=300,height=300)
            p2.grid(row=0,column=1)
            Label(p2,text=set2[1],bg='lightyellow',fg='black',font="Time 15 bold").pack(padx=20,pady=10)
            Label(p2,text=set2[2],bg='lightyellow',fg='black',font="Time 15 bold").pack(padx=20,pady=10)
            Label(p2,text=set2[3],bg='lightyellow',fg='black',font="Time 15 bold").pack(padx=20,pady=10)
            Label(p2,text=set2[4],bg='lightyellow',fg='black',font="Time 15 bold").pack(padx=20,pady=10)
            p3 = LabelFrame(frm_plan,text=' Day 3 : ',bg='lightyellow',fg='black',width=300,height=300)
            p3.grid(row=0,column=2)
            Label(p3,text=set3[1],bg='lightyellow',fg='black',font="Time 15 bold").pack(padx=20,pady=10)
            Label(p3,text=set3[2],bg='lightyellow',fg='black',font="Time 15 bold").pack(padx=20,pady=10)
            Label(p3,text=set3[3],bg='lightyellow',fg='black',font="Time 15 bold").pack(padx=20,pady=10)
            Label(p3,text=set3[4],bg='lightyellow',fg='black',font="Time 15 bold").pack(padx=20,pady=10)
            
            
        elif ch_plan.current() == 4 :
            #editplan()
            set = find_plan('s4')
            set1 = set[0]
            set2 = set[1]
            set3 = set[2]
            set4 = set[3]
            frm_plan = Frame(frm_bg,bg='white')
            frm_plan.grid(row=2,column=0,padx=5,sticky='news')
            frm_plan.rowconfigure((0),weight=10)
            frm_plan.rowconfigure((1),weight=1)
            frm_plan.columnconfigure((0,1,2,3),weight=1)
            p1 = LabelFrame(frm_plan,text=' Day 1 : ',bg='lightyellow',fg='black',width=300,height=300)
            p1.grid(row=0,column=0)
            Label(p1,text=set1[1],bg='lightyellow',fg='black',font="Time 15 bold").pack(padx=20,pady=10)
            Label(p1,text=set1[2],bg='lightyellow',fg='black',font="Time 15 bold").pack(padx=20,pady=10)
            Label(p1,text=set1[3],bg='lightyellow',fg='black',font="Time 15 bold").pack(padx=20,pady=10)
            Label(p1,text=set1[4],bg='lightyellow',fg='black',font="Time 15 bold").pack(padx=20,pady=10)
            p2 = LabelFrame(frm_plan,text=' Day 2 : ',bg='lightyellow',fg='black',width=300,height=300)
            p2.grid(row=0,column=1)
            Label(p2,text=set2[1],bg='lightyellow',fg='black',font="Time 15 bold").pack(padx=20,pady=10)
            Label(p2,text=set2[2],bg='lightyellow',fg='black',font="Time 15 bold").pack(padx=20,pady=10)
            Label(p2,text=set2[3],bg='lightyellow',fg='black',font="Time 15 bold").pack(padx=20,pady=10)
            Label(p2,text=set2[4],bg='lightyellow',fg='black',font="Time 15 bold").pack(padx=20,pady=10)
            p3 = LabelFrame(frm_plan,text=' Day 3 : ',bg='lightyellow',fg='black',width=300,height=300)
            p3.grid(row=0,column=2)
            Label(p3,text=set3[1],bg='lightyellow',fg='black',font="Time 15 bold").pack(padx=20,pady=10)
            Label(p3,text=set3[2],bg='lightyellow',fg='black',font="Time 15 bold").pack(padx=20,pady=10)
            Label(p3,text=set3[3],bg='lightyellow',fg='black',font="Time 15 bold").pack(padx=20,pady=10)
            Label(p3,text=set3[4],bg='lightyellow',fg='black',font="Time 15 bold").pack(padx=20,pady=10)
            p4 = LabelFrame(frm_plan,text=' Day 4 : ',bg='lightyellow',fg='black',width=250,height=250)
            p4.grid(row=0,column=3)
            Label(p4,text=set4[1],bg='lightyellow',fg='black',font="Time 15 bold").pack(padx=20,pady=10)
            Label(p4,text=set4[2],bg='lightyellow',fg='black',font="Time 15 bold").pack(padx=20,pady=10)
            Label(p4,text=set4[3],bg='lightyellow',fg='black',font="Time 15 bold").pack(padx=20,pady=10)
            Label(p4,text=set4[4],bg='lightyellow',fg='black',font="Time 15 bold").pack(padx=20,pady=10)
            
                    

    frm_choose = Frame(frm_bg,bg='white')
    frm_choose.grid(row=1,column=0,padx=5,sticky='news')
    lst_plan = ['How many day ?',1,2,3,4]
    ch_plan = ttk.Combobox(frm_choose,values=lst_plan,justify=LEFT)
    ch_plan.pack(pady=10)
    ch_plan.current(0)
    Button(frm_choose,text='Done',command=showfrm_plan).pack()


    frm_menu = Frame(frm_bg,bg='white')
    frm_menu.grid(row=3,column=0,padx=5,pady=5,sticky='news')
    frm_menu.rowconfigure((0),weight=1)
    frm_menu.columnconfigure((0,1,2,3,4,5),weight=1)
    
    Button(frm_menu,image=home,bg='black',command=choosemenu).grid(row=0,column=0,padx=2,sticky='news')
    Button(frm_menu,text="PLAN",bg='black',fg='white',font="Time 18 bold",command=plan).grid(row=0,column=1,padx=2,sticky='news')
    Button(frm_menu,text="REVIEW",bg='black',fg='white',font="Time 18 bold",command=review).grid(row=0,column=2,padx=2,sticky='news')
    Button(frm_menu,text="BOOKING",bg='black',fg='white',font="Time 18 bold",command=booking).grid(row=0,column=3,padx=2,sticky='news')
    Button(frm_menu,text="NAN SHOP",bg='black',fg='white',font="Time 18 bold",command=nanshop).grid(row=0,column=4,padx=2,sticky='news')
    Button(frm_menu,text="GUIDE",bg='black',fg='white',font="Time 18 bold",command=guide).grid(row=0,column=5,padx=2,sticky='news')

def find_plan(num):
    sql = "SELECT * FROM  Default_plan WHERE code = ?"
    cursor.execute(sql,[num])
    result = cursor.fetchall()
    return result


######### Review #########
def review():
    global main
    frm = Frame(main,bg="black")
    frm.grid(row=0,column=0,sticky='news')
    frm.rowconfigure((0),weight=1)
    frm.columnconfigure((0),weight=1)

    frm_bg = Frame(frm,bg="lightgrey")
    frm_bg.grid(row=0,column=0,padx=50,pady=50,sticky='news')
    frm_bg.rowconfigure((0,1,3),weight=1)
    frm_bg.rowconfigure((2),weight=10)
    frm_bg.columnconfigure((0),weight=1)

    frm_top = Frame(frm_bg,bg='white')
    frm_top.grid(row=0,column=0,pady=5,padx=5,sticky='news')
    frm_top.rowconfigure((0,1),weight=1)
    frm_top.columnconfigure((0),weight=1)
    global logo
    logo = PhotoImage(file='logo/logo.png')
    logo = logo.subsample(20)
    Label(frm_top,image=logo,bg='white',bd=0).pack(pady=10)
    Label(frm_top,text="REVIEW",bg='white').pack()

    frm_review = Frame(frm_bg,bg='white')
    frm_review.grid(row=2,column=0,padx=5,sticky='news')
    frm_review.rowconfigure((0,1),weight=3)
    frm_review.rowconfigure((2),weight=1)
    frm_review.columnconfigure((0,1,2,3,4),weight=1)
    
    Button(frm_review,image=t1,bg='white',command=lambda:show_inforeview('t1',rt1)).grid(row=0,column=0,pady=5)
    Button(frm_review,image=t2,bg='white',command=lambda:show_inforeview('t2',rt2)).grid(row=0,column=1,pady=5)
    Button(frm_review,image=t3,bg='white',command=lambda:show_inforeview('t3',rt3)).grid(row=0,column=2,pady=5)
    Button(frm_review,image=t4,bg='white',command=lambda:show_inforeview('t4',rt4)).grid(row=0,column=3,pady=5)
    Button(frm_review,image=t5,bg='white',command=lambda:show_inforeview('t5',rt5)).grid(row=0,column=4,pady=5)
    Button(frm_review,image=t6,bg='white',command=lambda:show_inforeview('t6',rt6)).grid(row=1,column=0,pady=5)
    Button(frm_review,image=t7,bg='white',command=lambda:show_inforeview('t7',rt7)).grid(row=1,column=1,pady=5)
    Button(frm_review,image=t8,bg='white',command=lambda:show_inforeview('t8',rt8)).grid(row=1,column=2,pady=5)
    Button(frm_review,image=t9,bg='white',command=lambda:show_inforeview('t9',rt9)).grid(row=1,column=3,pady=5)
    Button(frm_review,image=s1,bg='white',command=lambda:show_inforeview('s1',rs1)).grid(row=1,column=4,pady=5)

    def showreview(kind,index):
        #print(kind)
        if kind == 0 :
            #All
            frm_review = Frame(frm_bg,bg='white')
            frm_review.grid(row=2,column=0,padx=5,sticky='news')
            frm_review.rowconfigure((0,1),weight=1)
            frm_review.columnconfigure((0,1,2,3,4),weight=1)

            Button(frm_review,image=t1,bg='white',command=lambda:show_inforeview('t1',rt1)).grid(row=0,column=0,pady=5)
            Button(frm_review,image=t2,bg='white',command=lambda:show_inforeview('t2',rt2)).grid(row=0,column=1,pady=5)
            Button(frm_review,image=t3,bg='white',command=lambda:show_inforeview('t3',rt3)).grid(row=0,column=2,pady=5)
            Button(frm_review,image=t4,bg='white',command=lambda:show_inforeview('t4',rt4)).grid(row=0,column=3,pady=5)
            Button(frm_review,image=t5,bg='white',command=lambda:show_inforeview('t5',rt5)).grid(row=0,column=4,pady=5)
            Button(frm_review,image=t6,bg='white',command=lambda:show_inforeview('t6',rt6)).grid(row=1,column=0,pady=5)
            Button(frm_review,image=t7,bg='white',command=lambda:show_inforeview('t7',rt7)).grid(row=1,column=1,pady=5)
            Button(frm_review,image=t8,bg='white',command=lambda:show_inforeview('t8',rt8)).grid(row=1,column=2,pady=5)
            Button(frm_review,image=t9,bg='white',command=lambda:show_inforeview('t9',rt9)).grid(row=1,column=3,pady=5)
            Button(frm_review,image=s1,bg='white',command=lambda:show_inforeview('s1',rs1)).grid(row=1,column=4,pady=5)

            if index == 1 :
                Button(frm_review,image=t1,bg='white',command=lambda:show_inforeview('t1',rt1)).grid(row=0,column=0,pady=5)
                Button(frm_review,image=t2,bg='white',command=lambda:show_inforeview('t2',rt2)).grid(row=0,column=1,pady=5)
                Button(frm_review,image=t3,bg='white',command=lambda:show_inforeview('t3',rt3)).grid(row=0,column=2,pady=5)
                Button(frm_review,image=t4,bg='white',command=lambda:show_inforeview('t4',rt4)).grid(row=0,column=3,pady=5)
                Button(frm_review,image=t5,bg='white',command=lambda:show_inforeview('t5',rt5)).grid(row=0,column=4,pady=5)
                Button(frm_review,image=t6,bg='white',command=lambda:show_inforeview('t6',rt6)).grid(row=1,column=0,pady=5)
                Button(frm_review,image=t7,bg='white',command=lambda:show_inforeview('t7',rt7)).grid(row=1,column=1,pady=5)
                Button(frm_review,image=t8,bg='white',command=lambda:show_inforeview('t8',rt8)).grid(row=1,column=2,pady=5)
                Button(frm_review,image=t9,bg='white',command=lambda:show_inforeview('t9',rt9)).grid(row=1,column=3,pady=5)
                Button(frm_review,image=s1,bg='white',command=lambda:show_inforeview('s1',rs1)).grid(row=1,column=4,pady=5)
            elif index == 2 :
                Button(frm_review,image=c1,bg='white',command=lambda:show_inforeview('c1',rc1)).grid(row=0,column=0,pady=5)
                Button(frm_review,image=c2,bg='white',command=lambda:show_inforeview('c2',rc2)).grid(row=0,column=1,pady=5)
                Button(frm_review,image=c3,bg='white',command=lambda:show_inforeview('c3',rc3)).grid(row=0,column=2,pady=5)
                Button(frm_review,image=c4,bg='white',command=lambda:show_inforeview('c4',rc4)).grid(row=0,column=3,pady=5)
                Button(frm_review,image=c5,bg='white',command=lambda:show_inforeview('c5',rc5)).grid(row=0,column=4,pady=5)
                Button(frm_review,image=c6,bg='white',command=lambda:show_inforeview('c6',rc6)).grid(row=1,column=0,pady=5)
                Button(frm_review,image=c7,bg='white',command=lambda:show_inforeview('c7',rc7)).grid(row=1,column=1,pady=5)
                Button(frm_review,image=c8,bg='white',command=lambda:show_inforeview('c8',rc8)).grid(row=1,column=2,pady=5)
                Button(frm_review,image=c9,bg='white',command=lambda:show_inforeview('c9',rc9)).grid(row=1,column=3,pady=5)
                Button(frm_review,image=c10,bg='white',command=lambda:show_inforeview('c10',rc10)).grid(row=1,column=4,pady=5)
            elif index == 3 :
                Button(frm_review,image=n1,bg='white',command=lambda:show_inforeview('n1',rn1)).grid(row=0,column=0,pady=5)
                Button(frm_review,image=n2,bg='white',command=lambda:show_inforeview('n2',rn2)).grid(row=0,column=1,pady=5)
                Button(frm_review,image=n3,bg='white',command=lambda:show_inforeview('n3',rn3)).grid(row=0,column=2,pady=5)
                Button(frm_review,image=n4,bg='white',command=lambda:show_inforeview('n4',rn4)).grid(row=0,column=3,pady=5)
                Button(frm_review,image=n5,bg='white',command=lambda:show_inforeview('n5',rn5)).grid(row=0,column=4,pady=5)
                Button(frm_review,image=n6,bg='white',command=lambda:show_inforeview('n6',rn6)).grid(row=1,column=0,pady=5)
                Button(frm_review,image=n7,bg='white',command=lambda:show_inforeview('n7',rn7)).grid(row=1,column=1,pady=5)
                Button(frm_review,image=n8,bg='white',command=lambda:show_inforeview('n8',rn8)).grid(row=1,column=2,pady=5)
                Button(frm_review,image=n9,bg='white',command=lambda:show_inforeview('n9',rn9)).grid(row=1,column=3,pady=5)
                Button(frm_review,image=n10,bg='white',command=lambda:show_inforeview('n10',rn10)).grid(row=1,column=4,pady=5)

            frm_reviewbottom = Frame(frm_review,bg='white')
            frm_reviewbottom.grid(row=2,column=0,columnspan=5,sticky='news')
            Button(frm_reviewbottom,text='3',command=lambda:showreview(0,3)).pack(padx=2,side=RIGHT)
            Button(frm_reviewbottom,text='2',command=lambda:showreview(0,2)).pack(padx=2,side=RIGHT)
            Button(frm_reviewbottom,text='1',command=lambda:showreview(0,1)).pack(padx=2,side=RIGHT)

        elif kind == 1 :
            #Temple
            frm_review = Frame(frm_bg,bg='white')
            frm_review.grid(row=2,column=0,padx=5,sticky='news')
            frm_review.rowconfigure((0,1),weight=1)
            frm_review.columnconfigure((0,1,2,3,4),weight=1)
            
            Button(frm_review,image=t1,bg='white',command=lambda:show_inforeview('t1',rt1)).grid(row=0,column=0,pady=5)
            Button(frm_review,image=t2,bg='white',command=lambda:show_inforeview('t2',rt2)).grid(row=0,column=1,pady=5)
            Button(frm_review,image=t3,bg='white',command=lambda:show_inforeview('t3',rt3)).grid(row=0,column=2,pady=5)
            Button(frm_review,image=t4,bg='white',command=lambda:show_inforeview('t4',rt4)).grid(row=0,column=3,pady=5)
            Button(frm_review,image=t5,bg='white',command=lambda:show_inforeview('t5',rt5)).grid(row=0,column=4,pady=5)
            Button(frm_review,image=t6,bg='white',command=lambda:show_inforeview('t6',rt6)).grid(row=1,column=0,pady=5)
            Button(frm_review,image=t7,bg='white',command=lambda:show_inforeview('t7',rt7)).grid(row=1,column=1,pady=5)
            Button(frm_review,image=t8,bg='white',command=lambda:show_inforeview('t8',rt8)).grid(row=1,column=2,pady=5)
            Button(frm_review,image=t9,bg='white',command=lambda:show_inforeview('t9',rt9)).grid(row=1,column=3,pady=5)
            
            frm_reviewbottom = Frame(frm_review,bg='white')
            frm_reviewbottom.grid(row=2,column=0,columnspan=5,sticky='news')

        elif kind == 2 :
            #Cafe
            frm_review = Frame(frm_bg,bg='white')
            frm_review.grid(row=2,column=0,padx=5,sticky='news')
            frm_review.rowconfigure((0,1),weight=1)
            frm_review.columnconfigure((0,1,2,3,4),weight=1)
            
            Button(frm_review,image=c1,bg='white',command=lambda:show_inforeview('c1',rc1)).grid(row=0,column=0,pady=5)
            Button(frm_review,image=c2,bg='white',command=lambda:show_inforeview('c2',rc2)).grid(row=0,column=1,pady=5)
            Button(frm_review,image=c3,bg='white',command=lambda:show_inforeview('c3',rc3)).grid(row=0,column=2,pady=5)
            Button(frm_review,image=c4,bg='white',command=lambda:show_inforeview('c4',rc4)).grid(row=0,column=3,pady=5)
            Button(frm_review,image=c5,bg='white',command=lambda:show_inforeview('c5',rc5)).grid(row=0,column=4,pady=5)
            Button(frm_review,image=c6,bg='white',command=lambda:show_inforeview('c6',rc6)).grid(row=1,column=0,pady=5)
            Button(frm_review,image=c7,bg='white',command=lambda:show_inforeview('c7',rc7)).grid(row=1,column=1,pady=5)
            Button(frm_review,image=c8,bg='white',command=lambda:show_inforeview('c8',rc8)).grid(row=1,column=2,pady=5)
            Button(frm_review,image=c9,bg='white',command=lambda:show_inforeview('c9',rc9)).grid(row=1,column=3,pady=5)
            Button(frm_review,image=c10,bg='white',command=lambda:show_inforeview('c10',rc10)).grid(row=1,column=4,pady=5)

            frm_reviewbottom = Frame(frm_review,bg='white')
            frm_reviewbottom.grid(row=2,column=0,columnspan=5,sticky='news')

        elif kind == 3 :
            #Nature
            frm_review = Frame(frm_bg,bg='white')
            frm_review.grid(row=2,column=0,padx=5,sticky='news')
            frm_review.rowconfigure((0,1),weight=1)
            frm_review.columnconfigure((0,1,2,3,4),weight=1)
            
            Button(frm_review,image=n1,bg='white',command=lambda:show_inforeview('n1',rn1)).grid(row=0,column=0,pady=5)
            Button(frm_review,image=n2,bg='white',command=lambda:show_inforeview('n2',rn2)).grid(row=0,column=1,pady=5)
            Button(frm_review,image=n3,bg='white',command=lambda:show_inforeview('n3',rn3)).grid(row=0,column=2,pady=5)
            Button(frm_review,image=n4,bg='white',command=lambda:show_inforeview('n4',rn4)).grid(row=0,column=3,pady=5)
            Button(frm_review,image=n5,bg='white',command=lambda:show_inforeview('n5',rn5)).grid(row=0,column=4,pady=5)
            Button(frm_review,image=n6,bg='white',command=lambda:show_inforeview('n6',rn6)).grid(row=1,column=0,pady=5)
            Button(frm_review,image=n7,bg='white',command=lambda:show_inforeview('n7',rn7)).grid(row=1,column=1,pady=5)
            Button(frm_review,image=n8,bg='white',command=lambda:show_inforeview('n8',rn8)).grid(row=1,column=2,pady=5)
            Button(frm_review,image=n9,bg='white',command=lambda:show_inforeview('n9',rn9)).grid(row=1,column=3,pady=5)
            Button(frm_review,image=n10,bg='white',command=lambda:show_inforeview('n10',rn10)).grid(row=1,column=4,pady=5)

            frm_reviewbottom = Frame(frm_review,bg='white')
            frm_reviewbottom.grid(row=2,column=0,columnspan=5,sticky='news')

        elif kind == 4 :
            #Walking Street
            frm_review = Frame(frm_bg,bg='white')
            frm_review.grid(row=2,column=0,padx=5,sticky='news')
            
            a = Button(frm_review,image=s1,bg='white',command=lambda:show_inforeview('s1',rs1))
            a.grid(row=0,column=0,padx=10,pady=5)

            frm_reviewbottom = Frame(frm_review,bg='white')
            frm_reviewbottom.grid(row=2,column=0,columnspan=5,sticky='news')

    frm_reviewbottom = Frame(frm_review,bg='white')
    frm_reviewbottom.grid(row=2,column=0,columnspan=5,sticky='news')
    Button(frm_reviewbottom,text='3',command=lambda:showreview(0,3)).pack(padx=2,side=RIGHT)
    Button(frm_reviewbottom,text='2',command=lambda:showreview(0,2)).pack(padx=2,side=RIGHT)
    Button(frm_reviewbottom,text='1',command=lambda:showreview(0,1)).pack(padx=2,side=RIGHT)

    frm_choose = Frame(frm_bg,bg='white')
    frm_choose.grid(row=1,column=0,padx=5,sticky='news')
    lst_kind = ['All','Temple','Cafe','Nature','Walking Street']
    ch_plan = ttk.Combobox(frm_choose,values=lst_kind,justify=LEFT)
    ch_plan.pack(padx=10,pady=5,side=LEFT)
    ch_plan.current(0)
    Button(frm_choose,text='Done',command=lambda:showreview(ch_plan.current(),0)).pack(side=LEFT)

    frm_menu = Frame(frm_bg,bg='white')
    frm_menu.grid(row=3,column=0,padx=5,pady=5,sticky='news')
    frm_menu.rowconfigure((0),weight=1)
    frm_menu.columnconfigure((0,1,2,3,4,5),weight=1)
 
    Button(frm_menu,image=home,bg='black',command=choosemenu).grid(row=0,column=0,padx=2,sticky='news')
    Button(frm_menu,text="PLAN",bg='black',fg='white',font="Time 18 bold",command=plan).grid(row=0,column=1,padx=2,sticky='news')
    Button(frm_menu,text="REVIEW",bg='black',fg='white',font="Time 18 bold",command=review).grid(row=0,column=2,padx=2,sticky='news')
    Button(frm_menu,text="BOOKING",bg='black',fg='white',font="Time 18 bold",command=booking).grid(row=0,column=3,padx=2,sticky='news')
    Button(frm_menu,text="NAN SHOP",bg='black',fg='white',font="Time 18 bold",command=nanshop).grid(row=0,column=4,padx=2,sticky='news')
    Button(frm_menu,text="GUIDE",bg='black',fg='white',font="Time 18 bold",command=guide).grid(row=0,column=5,padx=2,sticky='news')


def show_inforeview(code,img):
    global main
    frm = Frame(main,bg="black")
    frm.grid(row=0,column=0,sticky='news')
    frm.rowconfigure((0),weight=1)
    frm.columnconfigure((0),weight=1)

    frm_bg = Frame(frm,bg="lightblue")
    frm_bg.grid(row=0,column=0,padx=50,pady=50,sticky='news')
    
    Label(frm_bg,image=img,bg='white').pack(pady=30)

    sql = "SELECT * FROM  review WHERE codeplace = ?"
    cursor.execute(sql,[code])
    result = cursor.fetchone()
    score = "Review(%d) : %.2f / 5 "%(result[1],result[3])
    Label(frm_bg,text=score,bg='lightblue').pack()
    if result[3] > 4.85 :
        Label(frm_bg,image=star50,bg='lightblue').pack()
    elif result[3] > 3.85 and result[3] < 4.2 :
        Label(frm_bg,image=star40,bg='lightblue').pack()
    elif result[3] > 2.85 and result[3] < 3.2 :
        Label(frm_bg,image=star30,bg='lightblue').pack()
    elif result[3] > 1.85 and result[3] < 2.2 :
        Label(frm_bg,image=star40,bg='lightblue').pack()
    elif result[3] > 0.85 and result[3] < 1.2 :
        Label(frm_bg,image=star10,bg='lightblue').pack()
    elif result[3] > 0 and result[3] < 0.2 :
        Label(frm_bg,image=star00,bg='lightblue').pack()
    elif result[3] >= 0.2 and result[3] <= 0.85 :
        Label(frm_bg,image=star05,bg='lightblue').pack()
    elif result[3] >= 1.2 and result[3] <= 1.85 :
        Label(frm_bg,image=star15,bg='lightblue').pack()
    elif result[3] >= 2.2 and result[3] <= 2.85 :
        Label(frm_bg,image=star25,bg='lightblue').pack()
    elif result[3] >= 3.2 and result[3] <= 3.85 :
        Label(frm_bg,image=star35,bg='lightblue').pack()
    elif result[3] >= 4.2 and result[3] <= 4.85 :
        Label(frm_bg,image=star45,bg='lightblue').pack()

    Button(frm_bg,text='BACK',bg='black',height=50,fg='white',font="Time 20 bold",command=review).pack(side=LEFT,padx=300)
    Button(frm_bg,text='REVIEW',bg='black',height=50,fg='white',font="Time 20 bold",command=lambda:clickreview(code,img)).pack(side=LEFT)

def clickreview(code,img):
    global popupreview
    if popupreview != None :
        return None
    
    popupreview = Toplevel(main)
    popupreview.geometry("300x300")
    popupreview.config(bg="white")
    popupreview.title("CLICK REVIEW")

    Label(popupreview,text='RATE HERE \n0 - 5',bg="white",font="Time 20 bold").pack(pady=20)
    rate = [0,1,2,3,4,5]
    combo = ttk.Combobox(popupreview,values=rate,state='readonly',justify=LEFT)
    combo.current(5)
    combo.pack(padx=30)

    Button(popupreview,text='Done',height=40, bg="black",fg='white',font="Time 20 bold",command=lambda:setNewrate(code,img,combo.current())).pack(pady=15)
    Button(popupreview,text='Cancle',height=40, bg="red",fg='white',font="Time 20 bold",command=cancle).pack(pady=15)

def setNewrate(code,img,rate) :
    global popupreview
    sql = "SELECT * FROM  review WHERE codeplace = ?"
    cursor.execute(sql,[code])
    result = cursor.fetchone()
    amt = result[1] + 1
    sum = result[2] + rate
    avg = sum/amt

    sql = "UPDATE review SET amt=?,sum=?,calculate=? WHERE codeplace = ?"
    cursor.execute(sql,[amt,sum,avg,code])
    conn.commit()

    popupreview.destroy()
    messagebox.showinfo("Admin","Thank you for your review.")
    popupreview = None
    show_inforeview(code,img)
    
def cancle():
    global popupreview
    popupreview.destroy()
    popupreview = None



######### Booking #########
def booking():
    global main
    frm = Frame(main,bg="black")
    frm.grid(row=0,column=0,sticky='news')
    frm.rowconfigure((0),weight=1)
    frm.columnconfigure((0),weight=1)

    frm_bg = Frame(frm,bg="lightgrey")
    frm_bg.grid(row=0,column=0,padx=50,pady=50,sticky='news')
    frm_bg.rowconfigure((0,1,3),weight=1)
    frm_bg.rowconfigure((2),weight=10)
    frm_bg.columnconfigure((0),weight=1)

    frm_top = Frame(frm_bg,bg='white')
    frm_top.grid(row=0,column=0,pady=5,padx=5,sticky='news')
    frm_top.rowconfigure((0,1),weight=1)
    frm_top.columnconfigure((0),weight=1)
    global logo
    logo = PhotoImage(file='logo/logo.png')
    logo = logo.subsample(20)
    Label(frm_top,image=logo,bg='white',bd=0).pack(pady=10)
    Label(frm_top,text="BOOKING",bg='white').pack()

    frm_bill = Frame(frm_bg,bg='white')
    frm_bill.grid(row=1,column=0,padx=5,sticky='news')
    Button(frm_bill,text=' Bill ',bg='black',fg='white',font="Time 15 bold",command=checkbill_booking).pack(padx=20,pady=10,side=RIGHT)
    
    frm_bk = Frame(frm_bg,bg='white')
    frm_bk.grid(row=2,column=0,padx=5,sticky='news')
    frm_bk.rowconfigure((0,1),weight=1)
    frm_bk.columnconfigure((0,1,2,3),weight=1)
    def create_hotel(index) :
        if index == 1 :
            #h1
            frm01 = Frame(frm_bk,bg='white')
            frm01.grid(row=0,column=0,pady=20,padx=20,sticky='news')
            Label(frm01,image=h1,bg='white').grid(row=0,rowspan=3,column=0)
            Label(frm01,text='Price',bg='white').grid(row=0,column=1,sticky='news')
            Label(frm01,text='1200 BAHT',bg='white').grid(row=1,column=1,sticky='news')
            Button(frm01,text='Booking',bg='black',fg='white',font="Time 15 bold",command=lambda:select_hotel('โรงแรมเทวราช',1200)).grid(row=2,column=1,sticky='news')
            #h2
            frm02 = Frame(frm_bk,bg='white')
            frm02.grid(row=1,column=0,pady=20,padx=20,sticky='news')
            Label(frm02,image=h2,bg='white').grid(row=0,rowspan=3,column=0)
            Label(frm02,text='Price',bg='white').grid(row=0,column=1,sticky='news')
            Label(frm02,text='2600 BAHT',bg='white').grid(row=1,column=1,sticky='news')
            Button(frm02,text='Booking',bg='black',fg='white',font="Time 15 bold",command=lambda:select_hotel('โรงแรมพูคาน่านฟ้า',2600)).grid(row=2,column=1,sticky='news')
            #h3
            frm03 = Frame(frm_bk,bg='white')
            frm03.grid(row=0,column=1,pady=20,padx=20,sticky='news')
            Label(frm03,image=h3,bg='white').grid(row=0,rowspan=3,column=0)
            Label(frm03,text='Price',bg='white').grid(row=0,column=1,sticky='news')
            Label(frm03,text='810 BAHT',bg='white').grid(row=1,column=1,sticky='news')
            Button(frm03,text='Booking',bg='black',fg='white',font="Time 15 bold",command=lambda:select_hotel('Khun Ying Hotel',810)).grid(row=2,column=1,sticky='news')
            #h4
            frm04 = Frame(frm_bk,bg='white')
            frm04.grid(row=1,column=1,pady=20,padx=20,sticky='news')
            Label(frm04,image=h4,bg='white').grid(row=0,rowspan=3,column=0)
            Label(frm04,text='Price',bg='white').grid(row=0,column=1,sticky='news')
            Label(frm04,text='756 BAHT',bg='white').grid(row=1,column=1,sticky='news')
            Button(frm04,text='Booking',bg='black',fg='white',font="Time 15 bold",command=lambda:select_hotel('Namthong Nan Hotel',756)).grid(row=2,column=1,sticky='news')
            #h5
            frm05 = Frame(frm_bk,bg='white')
            frm05.grid(row=0,column=2,pady=20,padx=20,sticky='news')
            Label(frm05,image=h5,bg='white').grid(row=0,rowspan=3,column=0)
            Label(frm05,text='Price',bg='white').grid(row=0,column=1,sticky='news')
            Label(frm05,text='700 BAHT',bg='white').grid(row=1,column=1,sticky='news')
            Button(frm05,text='Booking',bg='black',fg='white',font="Time 15 bold",command=lambda:select_hotel('ช้างเผือกเกสต์เฮ้าส์',700)).grid(row=2,column=1,sticky='news')
            #h6
            frm06 = Frame(frm_bk,bg='white')
            frm06.grid(row=1,column=2,pady=20,padx=20,sticky='news')
            Label(frm06,image=h6,bg='white').grid(row=0,rowspan=3,column=0)
            Label(frm06,text='Price',bg='white').grid(row=0,column=1,sticky='news')
            Label(frm06,text='780 BAHT',bg='white').grid(row=1,column=1,sticky='news')
            Button(frm06,text='Booking',bg='black',fg='white',font="Time 15 bold",command=lambda:select_hotel('ปัว พาโนราม่า รีสอร์ท',780)).grid(row=2,column=1,sticky='news')
            #h7
            frm07 = Frame(frm_bk,bg='white')
            frm07.grid(row=0,column=3,pady=20,padx=20,sticky='news')
            Label(frm07,image=h7,bg='white').grid(row=0,rowspan=3,column=0)
            Label(frm07,text='Price',bg='white').grid(row=0,column=1,sticky='news')
            Label(frm07,text='1000 BAHT',bg='white').grid(row=1,column=1,sticky='news')
            Button(frm07,text='Booking',bg='black',fg='white',font="Time 15 bold",command=lambda:select_hotel('บ้านสวนลีลาวดี รีสอร์ทน่าน',1000)).grid(row=2,column=1,sticky='news')
            #h8
            frm08 = Frame(frm_bk,bg='white')
            frm08.grid(row=1,column=3,pady=20,padx=20,sticky='news')
            Label(frm08,image=h8,bg='white').grid(row=0,rowspan=3,column=0)
            Label(frm08,text='Price',bg='white').grid(row=0,column=1,sticky='news')
            Label(frm08,text='1269 BAHT',bg='white').grid(row=1,column=1,sticky='news')
            Button(frm08,text='Booking',bg='black',fg='white',font="Time 15 bold",command=lambda:select_hotel('น่านตรึงใจ บูทีค โฮเต็ล',1269)).grid(row=2,column=1,sticky='news')
        if index == 2 :
            #h9
            frm01 = Frame(frm_bk,bg='white')
            frm01.grid(row=0,column=0,pady=20,padx=20,sticky='news')
            Label(frm01,image=h9,bg='white').grid(row=0,rowspan=3,column=0)
            Label(frm01,text='Price',bg='white').grid(row=0,column=1,sticky='news')
            Label(frm01,text='990 BAHT',bg='white').grid(row=1,column=1,sticky='news')
            Button(frm01,text='Booking',bg='black',fg='white',font="Time 15 bold",command=lambda:select_hotel('Casa Foresta Nan',990)).grid(row=2,column=1,sticky='news')
            #h10
            frm02 = Frame(frm_bk,bg='white')
            frm02.grid(row=1,column=0,pady=20,padx=20,sticky='news')
            Label(frm02,image=h10,bg='white').grid(row=0,rowspan=3,column=0)
            Label(frm02,text='Price',bg='white').grid(row=0,column=1,sticky='news')
            Label(frm02,text='1080 BAHT',bg='white').grid(row=1,column=1,sticky='news')
            Button(frm02,text='Booking',bg='black',fg='white',font="Time 15 bold",command=lambda:select_hotel('Richmond Nan Hotel',1080)).grid(row=2,column=1,sticky='news')
            #h11
            frm03 = Frame(frm_bk,bg='white')
            frm03.grid(row=0,column=1,pady=20,padx=20,sticky='news')
            Label(frm03,image=h11,bg='white').grid(row=0,rowspan=3,column=0)
            Label(frm03,text='Price',bg='white').grid(row=0,column=1,sticky='news')
            Label(frm03,text='890 BAHT',bg='white').grid(row=1,column=1,sticky='news')
            Button(frm03,text='Booking',bg='black',fg='white',font="Time 15 bold",command=lambda:select_hotel('Sinnlodge',890)).grid(row=2,column=1,sticky='news')
            #h12
            frm04 = Frame(frm_bk,bg='white')
            frm04.grid(row=1,column=1,pady=20,padx=20,sticky='news')
            Label(frm04,image=h12,bg='white').grid(row=0,rowspan=3,column=0)
            Label(frm04,text='Price',bg='white').grid(row=0,column=1,sticky='news')
            Label(frm04,text='2000 BAHT',bg='white').grid(row=1,column=1,sticky='news')
            Button(frm04,text='Booking',bg='black',fg='white',font="Time 15 bold",command=lambda:select_hotel('Nan Rim Nam Resort',2000)).grid(row=2,column=1,sticky='news')
            #h13
            frm05 = Frame(frm_bk,bg='white')
            frm05.grid(row=0,column=2,pady=20,padx=20,sticky='news')
            Label(frm05,image=h13,bg='white').grid(row=0,rowspan=3,column=0)
            Label(frm05,text='Price',bg='white').grid(row=0,column=1,sticky='news')
            Label(frm05,text='700 BAHT',bg='white').grid(row=1,column=1,sticky='news')
            Button(frm05,text='Booking',bg='black',fg='white',font="Time 15 bold",command=lambda:select_hotel('Bee Bee Home',700)).grid(row=2,column=1,sticky='news')
            #h14
            frm06 = Frame(frm_bk,bg='white')
            frm06.grid(row=1,column=2,pady=20,padx=20,sticky='news')
            Label(frm06,image=h14,bg='white').grid(row=0,rowspan=3,column=0)
            Label(frm06,text='Price',bg='white').grid(row=0,column=1,sticky='news')
            Label(frm06,text='1000 BAHT',bg='white').grid(row=1,column=1,sticky='news')
            Button(frm06,text='Booking',bg='black',fg='white',font="Time 15 bold",command=lambda:select_hotel('บ้านสวนฟ้าเคียงดาว',1000)).grid(row=2,column=1,sticky='news')
            #h15
            frm07 = Frame(frm_bk,bg='white')
            frm07.grid(row=0,column=3,pady=20,padx=20,sticky='news')
            Label(frm07,image=h15,bg='white').grid(row=0,rowspan=3,column=0)
            Label(frm07,text='Price',bg='white').grid(row=0,column=1,sticky='news')
            Label(frm07,text='720 BAHT',bg='white').grid(row=1,column=1,sticky='news')
            Button(frm07,text='Booking',bg='black',fg='white',font="Time 15 bold",command=lambda:select_hotel('เรือนวรา เกสต์เฮาส์',720)).grid(row=2,column=1,sticky='news')
            #h16
            frm08 = Frame(frm_bk,bg='white')
            frm08.grid(row=1,column=3,pady=20,padx=20,sticky='news')
            Label(frm08,image=h16,bg='white').grid(row=0,rowspan=3,column=0)
            Label(frm08,text='Price',bg='white').grid(row=0,column=1,sticky='news')
            Label(frm08,text='990 BAHT',bg='white').grid(row=1,column=1,sticky='news')
            Button(frm08,text='Booking',bg='black',fg='white',font="Time 15 bold",command=lambda:select_hotel('Sawaddeelanna Hotel',990)).grid(row=2,column=1,sticky='news')
        if index == 3 :
            #h17
            frm01 = Frame(frm_bk,bg='white')
            frm01.grid(row=0,column=0,pady=20,padx=20,sticky='news')
            Label(frm01,image=h17,bg='white').grid(row=0,rowspan=3,column=0)
            Label(frm01,text='Price',bg='white').grid(row=0,column=1,sticky='news')
            Label(frm01,text='2888 BAHT',bg='white').grid(row=1,column=1,sticky='news')
            Button(frm01,text='Booking',bg='black',fg='white',font="Time 15 bold",command=lambda:select_hotel('น่าน ซีซั่น บูติก รีสอร์ท',2888)).grid(row=2,column=1,sticky='news')
            #h18
            frm02 = Frame(frm_bk,bg='white')
            frm02.grid(row=0,column=1,pady=20,padx=20,sticky='news')
            Label(frm02,image=h18,bg='white').grid(row=0,rowspan=3,column=0)
            Label(frm02,text='Price',bg='white').grid(row=0,column=1,sticky='news')
            Label(frm02,text='1100 BAHT',bg='white').grid(row=1,column=1,sticky='news')
            Button(frm02,text='Booking',bg='black',fg='white',font="Time 15 bold",command=lambda:select_hotel('Pang Chompu',1100)).grid(row=2,column=1,sticky='news')
            #h19
            frm03 = Frame(frm_bk,bg='white')
            frm03.grid(row=0,column=2,pady=20,padx=20,sticky='news')
            Label(frm03,image=h19,bg='white').grid(row=0,rowspan=3,column=0)
            Label(frm03,text='Price',bg='white').grid(row=0,column=1,sticky='news')
            Label(frm03,text='1500 BAHT',bg='white').grid(row=1,column=1,sticky='news')
            Button(frm03,text='Booking',bg='black',fg='white',font="Time 15 bold",command=lambda:select_hotel('สวนหมากริมนา',1500)).grid(row=2,column=1,sticky='news')
            #h20
            frm04 = Frame(frm_bk,bg='white')
            frm04.grid(row=0,column=3,pady=20,padx=20,sticky='news')
            Label(frm04,image=h20,bg='white').grid(row=0,rowspan=3,column=0)
            Label(frm04,text='Price',bg='white').grid(row=0,column=1,sticky='news')
            Label(frm04,text='1600 BAHT',bg='white').grid(row=1,column=1,sticky='news')
            Button(frm04,text='Booking',bg='black',fg='white',font="Time 15 bold",command=lambda:select_hotel('Baan Yang Na Relax Zone Nan',1600)).grid(row=2,column=1,sticky='news')

            frm05 = Frame(frm_bk,bg='white')
            frm05.grid(row=1,column=0,pady=20,padx=20,sticky='news')
            frm06 = Frame(frm_bk,bg='white')
            frm06.grid(row=1,column=1,pady=20,padx=20,sticky='news')
            frm07 = Frame(frm_bk,bg='white')
            frm07.grid(row=1,column=2,pady=20,padx=20,sticky='news')
            frm08 = Frame(frm_bk,bg='white')
            frm08.grid(row=1,column=3,pady=20,padx=20,sticky='news')
            

    create_hotel(1)
    frm_bkbottom = Frame(frm_bk,bg='white')
    frm_bkbottom.grid(row=2,column=0,columnspan=5,sticky='news')
    Button(frm_bkbottom,text='3',command=lambda:create_hotel(3)).pack(padx=2,side=RIGHT)
    Button(frm_bkbottom,text='2',command=lambda:create_hotel(2)).pack(padx=2,side=RIGHT)
    Button(frm_bkbottom,text='1',command=lambda:create_hotel(1)).pack(padx=2,side=RIGHT)

    frm_menu = Frame(frm_bg,bg='white')
    frm_menu.grid(row=3,column=0,padx=5,pady=5,sticky='news')
    frm_menu.rowconfigure((0),weight=1)
    frm_menu.columnconfigure((0,1,2,3,4,5),weight=1)
    Button(frm_menu,image=home,bg='black',command=choosemenu).grid(row=0,column=0,padx=2,sticky='news')
    Button(frm_menu,text="PLAN",bg='black',fg='white',font="Time 18 bold",command=plan).grid(row=0,column=1,padx=2,sticky='news')
    Button(frm_menu,text="REVIEW",bg='black',fg='white',font="Time 18 bold",command=review).grid(row=0,column=2,padx=2,sticky='news')
    Button(frm_menu,text="BOOKING",bg='black',fg='white',font="Time 18 bold",command=booking).grid(row=0,column=3,padx=2,sticky='news')
    Button(frm_menu,text="NAN SHOP",bg='black',fg='white',font="Time 18 bold",command=nanshop).grid(row=0,column=4,padx=2,sticky='news')
    Button(frm_menu,text="GUIDE",bg='black',fg='white',font="Time 18 bold",command=guide).grid(row=0,column=5,padx=2,sticky='news')

def select_hotel(name,price):
    global main
    frm = Frame(main,bg="black")
    frm.grid(row=0,column=0,sticky='news')
    frm.rowconfigure((0),weight=1)
    frm.columnconfigure((0),weight=1)
    
    frm_bg = Frame(frm,bg="white")
    frm_bg.grid(row=0,column=0,padx=50,pady=50,sticky='news')
    frm_bg.rowconfigure((0,6,7),weight=1)
    frm_bg.columnconfigure((0,1),weight=1)

    Label(frm_bg,text=name,bg='white',font="Time 40 bold").grid(row=0,column=0,columnspan=2,pady=10)
    Label(frm_bg,text='Date : ',bg='white',font="Time 25 bold").grid(row=1,column=0,sticky='e',padx=20,pady=5)
    Label(frm_bg,text="Rooms : ",bg='white',font="Time 25 bold").grid(row=4,column=0,sticky='e',padx=20,pady=5)
    Label(frm_bg,text="Persons : ",bg='white',font="Time 25 bold").grid(row=5,column=0,sticky='e',padx=20,pady=5)
    Label(frm_bg,text="* หมายเหตุ : 1 ห้อง / 2 คน หากเกินจะต้องจ่ายเพิ่มกับทางโรงแรม",bg='white',font="Time 15 bold").grid(row=6,column=0,columnspan=2,pady=5)

    dd = Spinbox(frm_bg,from_=1,to=31, justify=LEFT, width=10)
    dd.grid(row=1,column=1,sticky='w',padx=10,pady=5)
    mm = Spinbox(frm_bg,from_=1,to=12, justify=LEFT, width=10)
    mm.grid(row=2,column=1,sticky='w',padx=10,pady=5)
    yy = Spinbox(frm_bg,from_=2021,to=2022,justify=LEFT, width=10)
    yy.grid(row=3,column=1,sticky='w',padx=10,pady=5)

    nr = Spinbox(frm_bg,from_=1,to=10,justify=LEFT, width=10)
    nr.grid(row=4,column=1,sticky='w',padx=10,pady=5)

    np = Spinbox(frm_bg,from_=1,to=10,justify=LEFT, width=10)
    np.grid(row=5,column=1,sticky='w',padx=10,pady=5)

    Button(frm_bg,text='Cancle',bg='black',height=50,fg='white',font="Time 15 bold",command=booking).grid(row=7,column=0,padx=50,pady=20,sticky='e')
    Button(frm_bg,text='Comfirm',bg='black',height=50,fg='white',font="Time 15 bold",command=lambda:booking_pay(name,price,dd.get(),mm.get(),yy.get(),nr.get(),np.get())).grid(row=7,column=1,padx=50,pady=20,sticky='w')

def booking_pay(name,price,dd,mm,yy,nr,np):
    date = str(dd) + "-" + str(mm) + "-" + str(yy)
    price = int(price)
    nr = int(nr)
    np = int(np)
    total = price * nr

    global main
    frm = Frame(main,bg="black")
    frm.grid(row=0,column=0,sticky='news')
    frm.rowconfigure((0),weight=1)
    frm.columnconfigure((0),weight=1)
    
    frm_bg = Frame(frm,bg="white")
    frm_bg.grid(row=0,column=0,padx=50,pady=50,sticky='news')
    frm_bg.rowconfigure((0,1,2,3,4,5),weight=1)
    frm_bg.columnconfigure((0,1),weight=1)

    Label(frm_bg,text='PAY',bg='white',font="Time 50 bold").grid(row=0,column=0,columnspan=2,padx=10,pady=5)
    Label(frm_bg,text=name,bg='white',font="Time 30 bold").grid(row=1,column=0,columnspan=2,pady=10)
    Label(frm_bg,text="Price : %.2f BAHT"%total,bg='white',font="Time 25 bold").grid(row=2,column=0,columnspan=2,padx=10,pady=5)
    Label(frm_bg,image=qrcode,bg='white').grid(row=3,column=0,columnspan=2,pady=15)
    Label(frm_bg,text="* If you already scan this QR code \nPlease click Confirm",bg='white',font="Time 15 bold").grid(row=4,column=0,columnspan=2)

    Button(frm_bg,text='Cancle',bg='black',height=50,fg='white',font="Time 15 bold",command=lambda:select_hotel(name,price)).grid(row=5,column=0,padx=50,pady=20,sticky='e')
    Button(frm_bg,text='Comfirm',bg='black',height=50,fg='white',font="Time 15 bold",command=lambda:showbill_booking(name,price,date,nr,np)).grid(row=5,column=1,padx=50,pady=20,sticky='w')

def showbill_booking(name,price,date,nr,np):
    #SQL
    sql = "SELECT * FROM  Bill_Booking WHERE user = ?"
    cursor.execute(sql,[var_user.get()])
    result = cursor.fetchone()
    if result :
        sql = "UPDATE Bill_Booking SET hotel=?,date=?,rooms=?,persons=?,price=? WHERE user = ?"
        cursor.execute(sql,[name,date,nr,np,price,var_user.get()])
        conn.commit()
    else :
        sql = "insert into Bill_Booking values (?,?,?,?,?,?)"
        cursor.execute(sql,[var_user.get(),name,date,nr,np,price])
        conn.commit()
    #Layout
    global main
    frm = Frame(main,bg="black")
    frm.grid(row=0,column=0,sticky='news')
    frm.rowconfigure((0),weight=1)
    frm.columnconfigure((0),weight=1)
    
    frm_bg = Frame(frm,bg="white")
    frm_bg.grid(row=0,column=0,padx=50,pady=50,sticky='news')
    frm_bg.rowconfigure((0,9),weight=1)
    frm_bg.columnconfigure((0,1),weight=1)

    Label(frm_bg,text='Bill',bg='white',font="Time 50 bold").grid(row=0,column=0,columnspan=2,pady=5)
    Label(frm_bg,text='Username : ',bg='white',font="Time 25 bold").grid(row=1,column=0,sticky='e',padx=20,pady=10)
    Label(frm_bg,text='Hotel : ',bg='white',font="Time 25 bold").grid(row=2,column=0,sticky='e',padx=20,pady=5)
    Label(frm_bg,text="Date : ",bg='white',font="Time 25 bold").grid(row=3,column=0,sticky='e',padx=20,pady=5)
    Label(frm_bg,text="Rooms : ",bg='white',font="Time 25 bold").grid(row=4,column=0,sticky='e',padx=20,pady=5)
    Label(frm_bg,text="Persons : ",bg='white',font="Time 25 bold").grid(row=5,column=0,sticky='e',padx=20,pady=5)
    Label(frm_bg,text="Price : ",bg='white',font="Time 25 bold").grid(row=6,column=0,sticky='e',padx=20,pady=5)
    Label(frm_bg,text="(Paid)",bg='white',fg='green',font="Time 30 ").grid(row=7,column=0,columnspan=2,pady=5)
    Label(frm_bg,text="** หากจำนวนคนมากกว่า 2 คน / ห้อง \nทางโรงแรมจะเก็บค่าส่วนเกินในวันที่เข้าพัก",bg='white',font="Time 15").grid(row=8,column=0,columnspan=2,pady=5)
    
    Label(frm_bg,text=var_user.get(),bg='white',font="Time 25 ").grid(row=1,column=1,sticky='w',padx=20,pady=10)
    Label(frm_bg,text=name,bg='white',font="Time 25 ").grid(row=2,column=1,sticky='w',padx=20,pady=5)
    Label(frm_bg,text=str(date),bg='white',font="Time 25 ").grid(row=3,column=1,sticky='w',padx=20,pady=5)
    Label(frm_bg,text=str(nr),bg='white',font="Time 25 ").grid(row=4,column=1,sticky='w',padx=20,pady=5)
    Label(frm_bg,text=str(np),bg='white',font="Time 25 ").grid(row=5,column=1,sticky='w',padx=20,pady=5)
    Label(frm_bg,text="%.2f BAHT"%price,bg='white',font="Time 25 ").grid(row=6,column=1,sticky='w',padx=20,pady=5)

    Button(frm_bg,text="Done",height=50,bg='black',fg='white',font="Time 15 bold",command=booking).grid(row=9,column=0,columnspan=2,pady=5)

def checkbill_booking():
    sql = "SELECT * FROM  Bill_Booking WHERE user = ?"
    cursor.execute(sql,[var_user.get()])
    result = cursor.fetchone()
    if result :
        global main
        frm = Frame(main,bg="black")
        frm.grid(row=0,column=0,sticky='news')
        frm.rowconfigure((0),weight=1)
        frm.columnconfigure((0),weight=1)
    
        frm_bg = Frame(frm,bg="white")
        frm_bg.grid(row=0,column=0,padx=50,pady=50,sticky='news')
        frm_bg.rowconfigure((0,9),weight=1)
        frm_bg.columnconfigure((0,1),weight=1)

        Label(frm_bg,text='Bill',bg='white',font="Time 50 bold").grid(row=0,column=0,columnspan=2,pady=5)
        Label(frm_bg,text='Username : ',bg='white',font="Time 25 bold").grid(row=1,column=0,sticky='e',padx=20,pady=10)
        Label(frm_bg,text='Hotel : ',bg='white',font="Time 25 bold").grid(row=2,column=0,sticky='e',padx=20,pady=5)
        Label(frm_bg,text="Date : ",bg='white',font="Time 25 bold").grid(row=3,column=0,sticky='e',padx=20,pady=5)
        Label(frm_bg,text="Rooms : ",bg='white',font="Time 25 bold").grid(row=4,column=0,sticky='e',padx=20,pady=5)
        Label(frm_bg,text="Persons : ",bg='white',font="Time 25 bold").grid(row=5,column=0,sticky='e',padx=20,pady=5)
        Label(frm_bg,text="Price : ",bg='white',font="Time 25 bold").grid(row=6,column=0,sticky='e',padx=20,pady=5)
        Label(frm_bg,text="(Paid)",bg='white',fg='green',font="Time 30 ").grid(row=7,column=0,columnspan=2,pady=5)
        Label(frm_bg,text="** หากจำนวนคนมากกว่า 2 คน / ห้อง \nทางโรงแรมจะเก็บค่าส่วนเกินในวันที่เข้าพัก",bg='white',font="Time 15").grid(row=8,column=0,columnspan=2,pady=5)
    
        Label(frm_bg,text=result[0],bg='white',font="Time 25 ").grid(row=1,column=1,sticky='w',padx=20,pady=10)
        Label(frm_bg,text=result[1],bg='white',font="Time 25 ").grid(row=2,column=1,sticky='w',padx=20,pady=5)
        Label(frm_bg,text=result[2],bg='white',font="Time 25 ").grid(row=3,column=1,sticky='w',padx=20,pady=5)
        Label(frm_bg,text=str(result[3]),bg='white',font="Time 25 ").grid(row=4,column=1,sticky='w',padx=20,pady=5)
        Label(frm_bg,text=str(result[4]),bg='white',font="Time 25 ").grid(row=5,column=1,sticky='w',padx=20,pady=5)
        Label(frm_bg,text="%.2f BAHT"%result[5],bg='white',font="Time 25 ").grid(row=6,column=1,sticky='w',padx=20,pady=5)

        Button(frm_bg,text="Done",height=50,bg='black',fg='white',font="Time 15 bold",command=booking).grid(row=9,column=0,columnspan=2,pady=5)
    else :
        messagebox.showwarning('Admin','Not found your Bill \nPls Booking first.')


######### Nan Shop #########
def nanshop():
    global main
    
    frm = Frame(main,bg="black")
    frm.grid(row=0,column=0,sticky='news')
    frm.rowconfigure((0),weight=1)
    frm.columnconfigure((0),weight=1)

    frm_bg = Frame(frm,bg="lightgrey")
    frm_bg.grid(row=0,column=0,padx=50,pady=50,sticky='news')
    frm_bg.rowconfigure((0,1,3),weight=1)
    frm_bg.rowconfigure((2),weight=10)
    frm_bg.columnconfigure((0),weight=1)

    frm_top = Frame(frm_bg,bg='white')
    frm_top.grid(row=0,column=0,pady=5,padx=5,sticky='news')
    frm_top.rowconfigure((0,1),weight=1)
    frm_top.columnconfigure((0),weight=1)
    global logo
    logo = PhotoImage(file='logo/logo.png')
    logo = logo.subsample(20)
    Label(frm_top,image=logo,bg='white',bd=0).pack(pady=10)
    Label(frm_top,text="NAN SHOP",bg='white').pack()

    frm_bill = Frame(frm_bg,bg='white')
    frm_bill.grid(row=1,column=0,padx=5,sticky='news')
    Button(frm_bill,text=' Pay ',bg='black',fg='white',font="Time 15 bold",command=basket).pack(padx=20,pady=10,side=RIGHT)
    
    frm_shop = Frame(frm_bg,bg='white')
    frm_shop.grid(row=2,column=0,padx=5,sticky='news')
    frm_shop.rowconfigure((0,1),weight=1)
    frm_shop.columnconfigure((0,1,2,3),weight=1)
    #p1
    frm01 = Frame(frm_shop,bg='white')
    frm01.grid(row=0,column=0,pady=20,padx=20,sticky='news')
    Label(frm01,image=p1,bg='white').grid(row=0,rowspan=3,column=0)
    Label(frm01,text='Price',bg='white').grid(row=0,column=1,sticky='news')
    Label(frm01,text='1500 BAHT',bg='white').grid(row=1,column=1,sticky='news')
    Button(frm01,text='Select',bg='black',fg='white',font="Time 15 bold",command=lambda:selectproduct('p1')).grid(row=2,column=1,sticky='news')
    #p2
    frm02 = Frame(frm_shop,bg='white')
    frm02.grid(row=1,column=0,pady=20,padx=20,sticky='news')
    Label(frm02,image=p2,bg='white').grid(row=0,rowspan=3,column=0)
    Label(frm02,text='Price',bg='white').grid(row=0,column=1,sticky='news')
    Label(frm02,text='150 BAHT',bg='white').grid(row=1,column=1,sticky='news')
    Button(frm02,text='Select',bg='black',fg='white',font="Time 15 bold",command=lambda:selectproduct('p2')).grid(row=2,column=1,sticky='news')
    #p3
    frm03 = Frame(frm_shop,bg='white')
    frm03.grid(row=0,column=1,pady=20,padx=20,sticky='news')
    Label(frm03,image=p3,bg='white').grid(row=0,rowspan=3,column=0)
    Label(frm03,text='Price',bg='white').grid(row=0,column=1,sticky='news')
    Label(frm03,text='120 BAHT',bg='white').grid(row=1,column=1,sticky='news')
    Button(frm03,text='Select',bg='black',fg='white',font="Time 15 bold",command=lambda:selectproduct('p3')).grid(row=2,column=1,sticky='news')
    #p4
    frm04 = Frame(frm_shop,bg='white')
    frm04.grid(row=1,column=1,pady=20,padx=20,sticky='news')
    Label(frm04,image=p4,bg='white').grid(row=0,rowspan=3,column=0)
    Label(frm04,text='Price',bg='white').grid(row=0,column=1,sticky='news')
    Label(frm04,text='39 BAHT',bg='white').grid(row=1,column=1,sticky='news')
    Button(frm04,text='Select',bg='black',fg='white',font="Time 15 bold",command=lambda:selectproduct('p4')).grid(row=2,column=1,sticky='news')
    #p5
    frm05 = Frame(frm_shop,bg='white')
    frm05.grid(row=0,column=2,pady=20,padx=20,sticky='news')
    Label(frm05,image=p5,bg='white').grid(row=0,rowspan=3,column=0)
    Label(frm05,text='Price',bg='white').grid(row=0,column=1,sticky='news')
    Label(frm05,text='39 BAHT',bg='white').grid(row=1,column=1,sticky='news')
    Button(frm05,text='Select',bg='black',fg='white',font="Time 15 bold",command=lambda:selectproduct('p5')).grid(row=2,column=1,sticky='news')
    #p6
    frm06 = Frame(frm_shop,bg='white')
    frm06.grid(row=1,column=2,pady=20,padx=20,sticky='news')
    Label(frm06,image=p6,bg='white').grid(row=0,rowspan=3,column=0)
    Label(frm06,text='Price',bg='white').grid(row=0,column=1,sticky='news')
    Label(frm06,text='35 BAHT',bg='white').grid(row=1,column=1,sticky='news')
    Button(frm06,text='Select',bg='black',fg='white',font="Time 15 bold",command=lambda:selectproduct('p6')).grid(row=2,column=1,sticky='news')
    #p7
    frm07 = Frame(frm_shop,bg='white')
    frm07.grid(row=0,column=3,pady=20,padx=20,sticky='news')
    Label(frm07,image=p7,bg='white').grid(row=0,rowspan=3,column=0)
    Label(frm07,text='Price',bg='white').grid(row=0,column=1,sticky='news')
    Label(frm07,text='39 BAHT',bg='white').grid(row=1,column=1,sticky='news')
    Button(frm07,text='Select',bg='black',fg='white',font="Time 15 bold",command=lambda:selectproduct('p7')).grid(row=2,column=1,sticky='news')
    #p8
    frm08 = Frame(frm_shop,bg='white')
    frm08.grid(row=1,column=3,pady=20,padx=20,sticky='news')
    Label(frm08,image=p8,bg='white').grid(row=0,rowspan=3,column=0)
    Label(frm08,text='Price',bg='white').grid(row=0,column=1,sticky='news')
    Label(frm08,text='100 BAHT',bg='white').grid(row=1,column=1,sticky='news')
    Button(frm08,text='Select',bg='black',fg='white',font="Time 15 bold",command=lambda:selectproduct('p8')).grid(row=2,column=1,sticky='news')


    frm_menu = Frame(frm_bg,bg='white')
    frm_menu.grid(row=3,column=0,padx=5,pady=5,sticky='news')
    frm_menu.rowconfigure((0),weight=1)
    frm_menu.columnconfigure((0,1,2,3,4,5),weight=1)
    Button(frm_menu,image=home,bg='black',command=choosemenu).grid(row=0,column=0,padx=2,sticky='news')
    Button(frm_menu,text="PLAN",bg='black',fg='white',font="Time 18 bold",command=plan).grid(row=0,column=1,padx=2,sticky='news')
    Button(frm_menu,text="REVIEW",bg='black',fg='white',font="Time 18 bold",command=review).grid(row=0,column=2,padx=2,sticky='news')
    Button(frm_menu,text="BOOKING",bg='black',fg='white',font="Time 18 bold",command=booking).grid(row=0,column=3,padx=2,sticky='news')
    Button(frm_menu,text="NAN SHOP",bg='black',fg='white',font="Time 18 bold",command=nanshop).grid(row=0,column=4,padx=2,sticky='news')
    Button(frm_menu,text="GUIDE",bg='black',fg='white',font="Time 18 bold",command=guide).grid(row=0,column=5,padx=2,sticky='news')

def selectproduct(code):
    global np1,np2,np3,np4,np5,np6,np7,np8

    if code == 'p1' :
        np1 = np1 + 1
        messagebox.showinfo("Admin","เพิ่มผ้าทอมือไทลื้อในตะกร้า 1 ชิ้น \nมีผ้าทอมือไทลื้อในตะกร้า %d ชิ้น"%np1)
    elif code == 'p2' :
        np2 = np2 + 1
        messagebox.showinfo("Admin","เพิ่มข้าวน่านในตะกร้า 1 ชิ้น \nมีข้าวน่านในตะกร้า %d ชิ้น"%np2)
    elif code == 'p3' :
        np3 = np3 + 1
        messagebox.showinfo("Admin","เพิ่มขนมเปี๊ยะฮ่องกงในตะกร้า 1 ชิ้น \nมีขนมเปี๊ยะฮ่องกงในตะกร้า %d ชิ้น"%np3)
    elif code == 'p4' :
        np4 = np4 + 1
        messagebox.showinfo("Admin","เพิ่มเพียงตะวันมะไฟจีนในตะกร้า 1 ชิ้น \nมีเพียงตะวันมะไฟจีนในตะกร้า %d ชิ้น"%np4)
    elif code == 'p5' :
        np5 = np5 + 1
        messagebox.showinfo("Admin","เพิ่มสาหร่ายไกเริศรสในตะกร้า 1 ชิ้น \nมีสาหร่ายไกเริศรสในตะกร้า %d ชิ้น"%np5)
    elif code == 'p6' :
        np6 = np6 + 1
        messagebox.showinfo("Admin","เพิ่มข้าวแต๋นน้ำแตงโมในตะกร้า 1 ชิ้น \nมีข้าวแต๋นน้ำแตงโมในตะกร้า %d ชิ้น"%np6)
    elif code == 'p7' :
        np7 = np7 + 1
        messagebox.showinfo("Admin","เพิ่มทองม้วนหมูหยองในตะกร้า 1 ชิ้น \nมีทองม้วนหมูหยองในตะกร้า %d ชิ้น"%np7)
    elif code == 'p8' :
        np8 = np8 + 1
        messagebox.showinfo("Admin","เพิ่มมันอะลูทอดกรอบในตะกร้า 1 ชิ้น \nมีมันอะลูทอดกรอบในตะกร้า %d ชิ้น"%np8)
    #print(np1,np2,np3,np4,np5,np6,np7,np8)

def clear(page):
    global np1,np2,np3,np4,np5,np6,np7,np8
    global pp1,pp2,pp3,pp4,pp5,pp6,pp7,pp8
    np1,np2,np3,np4,np5,np6,np7,np8 = 0,0,0,0,0,0,0,0
    pp1,pp2,pp3,pp4,pp5,pp6,pp7,pp8 = 0,0,0,0,0,0,0,0
    if page == 1 :
        basket()
    elif page == 2 :
        nanshop()
def basket():
    global np1,np2,np3,np4,np5,np6,np7,np8
    global pp1,pp2,pp3,pp4,pp5,pp6,pp7,pp8
    lst_np = [np1,np2,np3,np4,np5,np6,np7,np8]
    lst_pp = [pp1,pp2,pp3,pp4,pp5,pp6,pp7,pp8]
    price_pd = [1500,150,120,39,39,35,39,100]
    product = ["ผ้าทอมือไทลื้อ","ข้าวน่าน","ขนมเปี๊ยะฮ่องกง","เพียงตะวันมะไฟจีน","สาหร่ายไกเริศรส","ข้าวแต๋นน้ำแตงโม","ทองม้วนหมูหยอง","มันอะลูทอดกรอบ"]
    global main
    frm = Frame(main,bg="black")
    frm.grid(row=0,column=0,sticky='news')
    frm.rowconfigure((0),weight=1)
    frm.columnconfigure((0),weight=1)
    
    frm_bg = Frame(frm,bg="white")
    frm_bg.grid(row=0,column=0,padx=50,pady=50,sticky='news')
    frm_bg.rowconfigure((0,11),weight=1)
    frm_bg.columnconfigure((0,1),weight=1)

    Label(frm_bg,text='Basket',bg='white',font="Time 50 bold").grid(row=0,column=0,columnspan=2,pady=5)
    cnt_t = 0
    cnt_f = 0
    sum = 0
    for i,np in enumerate(lst_np) :
        if np > 0 :
            cnt_t = cnt_t +1
            lst_pp[i] = lst_np[i] * price_pd[i]
            sum = sum + lst_pp[i]
            Label(frm_bg,text="%d. %s "%(cnt_t,product[i]),bg='white',font="Time 25 bold").grid(row=cnt_t,column=0,padx=150,pady=10,sticky='w')
            Label(frm_bg,text='%d'%np,width=20,bg='lightblue',font="Time 25 bold").grid(row=cnt_t,column=1,padx=10,pady=10,sticky='w')
        else :
            cnt_f = cnt_f + 1
    if cnt_f == 8 :
        Label(frm_bg,text='ไม่มีรายการซื้อของในตะกร้า',bg='white',font="Time 30 bold").grid(row=5,column=0,columnspan=2,pady=5)
    Label(frm_bg,text='Total Price : %.2f BAHT'%sum,bg='white',font="Time 25 bold").grid(row=9,column=0,columnspan=2,pady=20)
    Button(frm_bg,text="BACK",height=50,bg='black',fg='white',font="Time 20 bold",command=nanshop).grid(row=10,column=0,pady=5)
    Button(frm_bg,text="Confirm",height=50,bg='black',fg='white',font="Time 20 bold",command=enterhotel).grid(row=10,column=1,pady=5)
    Button(frm_bg,text='Clear All',height=50,bg='red',fg='white',font="Time 25 bold",command=lambda:clear(1)).grid(row=11,column=0,columnspan=2,pady=15,sticky='n')

def enterhotel():
    global main
    global np1,np2,np3,np4,np5,np6,np7,np8
    global pp1,pp2,pp3,pp4,pp5,pp6,pp7,pp8
    lst_np = [np1,np2,np3,np4,np5,np6,np7,np8]
    lst_pp = [pp1,pp2,pp3,pp4,pp5,pp6,pp7,pp8]
    price_pd = [1500,150,120,39,39,35,39,100]
    product = ["ผ้าทอมือไทลื้อ","ข้าวน่าน","ขนมเปี๊ยะฮ่องกง","เพียงตะวันมะไฟจีน","สาหร่ายไกเริศรส","ข้าวแต๋นน้ำแตงโม","ทองม้วนหมูหยอง","มันอะลูทอดกรอบ"]
    frm = Frame(main,bg="black")
    frm.grid(row=0,column=0,sticky='news')
    frm.rowconfigure((0),weight=1)
    frm.columnconfigure((0),weight=1)
    
    frm_bg = Frame(frm,bg="white")
    frm_bg.grid(row=0,column=0,padx=50,pady=50,sticky='news')
    frm_bg.rowconfigure((0,10),weight=1)
    frm_bg.columnconfigure((0,1),weight=1)

    Label(frm_bg,text='เลือกโรงแรมที่จะจัดส่ง',bg='white',font="Time 50 bold").grid(row=0,column=0,columnspan=2,pady=5)
    lst_hotel = ["โรงแรมเทวราช","โรงแรมพูคาน่านฟ้า","Khun Yong Hotel","Namthong Nan Hotel","ช้างเผือกเกสต์เฮ้าส์","ปัว พาโนราม่า รีสอร์ท",
    "บ้านสวนลีลาวดี รีสอร์ท น่าน","น่านตรึงใจ บูทีค โฮเต็ล","Casa Foresta Nan","Richmond Nan Hotel","Sinnlodge","Nan Rim Nam Resort",
    "Bee Bee Home","บ้านสวนฟ้าเคียงดาว","เรือนวรา เกสต์เฮ้าส์","Sawadeelanna Hotel",
    "น่าน ซีซั่นส์ บูติก รีสอร์ท","Pang Chompu","สวนหมากริมนา","Baan Yang Na Relax Zone Nan"]
    combo_hotel = ttk.Combobox(frm_bg,values=lst_hotel)
    combo_hotel.grid(row=1,column=0,columnspan=2,pady=5)
    combo_hotel.current(0)
    cnt_t = 1
    cnt = 0
    sum = 0
    for i,np in enumerate(lst_np) :
        if np > 0 :
            cnt_t = cnt_t +1
            cnt = cnt +1
            lst_pp[i] = lst_np[i] * price_pd[i]
            sum = sum + lst_pp[i]
            Label(frm_bg,text="%d. %s "%(cnt,product[i]),bg='white',font="Time 25 bold").grid(row=cnt_t,column=0,padx=150,pady=10,sticky='w')
            Label(frm_bg,text='%d BATH'%lst_pp[i],width=20,bg='lightblue',font="Time 25 bold",justify=RIGHT).grid(row=cnt_t,column=1,padx=10,pady=10,sticky='w')
           

    Label(frm_bg,text='Total Price : %.2f BAHT'%sum,bg='white',font="Time 25 bold").grid(row=9,column=0,columnspan=2,pady=20)
    Button(frm_bg,text="BACK",height=50,bg='black',fg='white',font="Time 20 bold",command=basket).grid(row=10,column=0,pady=5,sticky='n')
    Button(frm_bg,text="Confirm",height=50,bg='black',fg='white',font="Time 20 bold",command=lambda:pay_nanshop(sum,lst_hotel[combo_hotel.current()])).grid(row=10,column=1,pady=5,sticky='n')
    Label(frm_bg,text='** หมายเหตุ : สินค้าจะถูกจัดส่งไปยังโรงแรมที่ลูกค้าพักภายใน 1 ชม.',bg='white',font="Time 15 bold").grid(row=11,column=0,columnspan=2,pady=20)

def pay_nanshop(total,hotel):
    global main
    frm = Frame(main,bg="black")
    frm.grid(row=0,column=0,sticky='news')
    frm.rowconfigure((0),weight=1)
    frm.columnconfigure((0),weight=1)
    
    frm_bg = Frame(frm,bg="white")
    frm_bg.grid(row=0,column=0,padx=50,pady=50,sticky='news')
    frm_bg.rowconfigure((0,3,4,5),weight=1)
    frm_bg.columnconfigure((0,1),weight=1)

    Label(frm_bg,text='PAY',bg='white',font="Time 50 bold").grid(row=0,column=0,columnspan=2,padx=10,pady=5)
    Label(frm_bg,text='Nan Shop',bg='white',font="Time 30 bold").grid(row=1,column=0,columnspan=2,pady=10)
    Label(frm_bg,text="Price : %.2f BAHT"%total,bg='white',font="Time 25 bold").grid(row=2,column=0,columnspan=2,padx=10,pady=5)
    Label(frm_bg,image=qrcode,bg='white').grid(row=3,column=0,columnspan=2,pady=15)
    Label(frm_bg,text="* If you already scan this QR code \nPlease click Confirm",bg='white',font="Time 15 bold").grid(row=4,column=0,columnspan=2)

    Button(frm_bg,text='Cancle',bg='black',height=50,fg='white',font="Time 15 bold",command=enterhotel).grid(row=5,column=0,padx=50,pady=20,sticky='e')
    Button(frm_bg,text='Comfirm',bg='black',height=50,fg='white',font="Time 15 bold",command=lambda:bill_nanshop(hotel)).grid(row=5,column=1,padx=50,pady=20,sticky='w')

def bill_nanshop(hotel):
    global main
    global np1,np2,np3,np4,np5,np6,np7,np8
    global pp1,pp2,pp3,pp4,pp5,pp6,pp7,pp8
    lst_np = [np1,np2,np3,np4,np5,np6,np7,np8]
    lst_pp = [pp1,pp2,pp3,pp4,pp5,pp6,pp7,pp8]
    price_pd = [1500,150,120,39,39,35,39,100]
    product = ["ผ้าทอมือไทลื้อ","ข้าวน่าน","ขนมเปี๊ยะฮ่องกง","เพียงตะวันมะไฟจีน","สาหร่ายไกเริศรส","ข้าวแต๋นน้ำแตงโม","ทองม้วนหมูหยอง","มันอะลูทอดกรอบ"]
    
    frm = Frame(main,bg="black")
    frm.grid(row=0,column=0,sticky='news')
    frm.rowconfigure((0),weight=1)
    frm.columnconfigure((0),weight=1)
    
    frm_bg = Frame(frm,bg="white")
    frm_bg.grid(row=0,column=0,padx=50,pady=50,sticky='news')
    frm_bg.rowconfigure((0,13),weight=1)
    frm_bg.columnconfigure((0,1),weight=1)

    Label(frm_bg,text='Bill Nan Shop',bg='white',font="Time 50 bold").grid(row=0,column=0,columnspan=2,pady=5)
    cnt_t = 0
    sum = 0
    for i,np in enumerate(lst_np) :
        if np > 0 :
            cnt_t = cnt_t +1
            lst_pp[i] = lst_np[i] * price_pd[i]
            sum = sum + lst_pp[i]
            Label(frm_bg,text="%d. %s "%(cnt_t,product[i]),bg='white',font="Time 25 bold").grid(row=cnt_t,column=0,padx=150,pady=10,sticky='w')
            Label(frm_bg,text='%d BATH'%lst_pp[i],width=20,bg='white',font="Time 25 bold",justify=RIGHT).grid(row=cnt_t,column=1,padx=10,pady=10,sticky='w')
    
    Label(frm_bg,text='Total Price : ',bg='white',font="Time 30 bold").grid(row=9,column=0,padx=30,pady=10,sticky='e')
    Label(frm_bg,text='%.2f BAHT'%sum,bg='white',font="Time 25 bold").grid(row=9,column=1,padx=15,pady=10,sticky='w')
    Label(frm_bg,text="สถานที่จัดส่ง : ",bg='white',font="Time 30 bold").grid(row=10,column=0,padx=30,pady=10,sticky='e')
    Label(frm_bg,text=hotel,bg='white',font="Time 25 bold").grid(row=10,column=1,padx=15,pady=15,sticky='w')
    Label(frm_bg,text="(Paid)",bg='white',fg='Green',font="Time 30 ").grid(row=11,column=0,columnspan=2,pady=15)
    Label(frm_bg,text='** หมายเหตุ : สินค้าจะถูกจัดส่งไปยังโรงแรมที่ลูกค้าพักภายใน 1 ชม.',bg='white',font="Time 15 bold").grid(row=12,column=0,columnspan=2,pady=10)
    Button(frm_bg,text="Done",height=50,bg='black',fg='white',font="Time 20 bold",command=lambda:clear(2)).grid(row=13,column=0,columnspan=2,pady=5,sticky='n')
    


    
######### Guide #########
def guide():
    global main
    frm = Frame(main,bg="black")
    frm.grid(row=0,column=0,sticky='news')
    frm.rowconfigure((0),weight=1)
    frm.columnconfigure((0),weight=1)

    frm_bg = Frame(frm,bg="lightgrey")
    frm_bg.grid(row=0,column=0,padx=50,pady=50,sticky='news')
    frm_bg.rowconfigure((0,1,3),weight=1)
    frm_bg.rowconfigure((2),weight=10)
    frm_bg.columnconfigure((0),weight=1)

    frm_top = Frame(frm_bg,bg='white')
    frm_top.grid(row=0,column=0,pady=5,padx=5,sticky='news')
    frm_top.rowconfigure((0,1),weight=1)
    frm_top.columnconfigure((0),weight=1)
    global logo
    logo = PhotoImage(file='logo/logo.png')
    logo = logo.subsample(20)
    Label(frm_top,image=logo,bg='white',bd=0).pack(pady=10)
    Label(frm_top,text="GUIDE",bg='white').pack()

    frm_bill = Frame(frm_bg,bg='white')
    frm_bill.grid(row=1,column=0,padx=5,sticky='news')
    Button(frm_bill,text=' Bill ',bg='black',fg='white',font="Time 15 bold",command=checkbill_bookingguide).pack(padx=20,pady=10,side=RIGHT)
    
    frm_guide = Frame(frm_bg,bg='white')
    frm_guide.grid(row=2,column=0,padx=5,sticky='news')
    frm_guide.rowconfigure((0,1),weight=1)
    frm_guide.columnconfigure((0,1),weight=1)

    #g1
    frm01 = Frame(frm_guide,bg='white')
    frm01.grid(row=0,column=0,pady=10,padx=30)
    Label(frm01,image=g01,bg='white').grid(row=0,rowspan=4,column=0)
    Label(frm01,text='ชื่อ : กนกอร พรชัย',bg='white',font="Time 15 bold",justify=LEFT).grid(row=0,column=1,sticky='news')
    Label(frm01,text='อายุ : 37 ปี',bg='white',font="Time 15 bold",justify=LEFT).grid(row=1,column=1,sticky='news')
    Label(frm01,text='เพศ : หญิง',bg='white',font="Time 15 bold",justify=LEFT).grid(row=2,column=1,sticky='news')
    Label(frm01,text='ภาษา : พื้นเมือง , อังกฤษ , จีน',bg='white',font="Time 15 bold",justify=LEFT).grid(row=3,column=1,sticky='news')
    Button(frm01,text='Booking',bg='black',fg='white',font="Time 15 bold",command=lambda:select_guide("G01")).grid(row=4,column=0,columnspan=2,sticky='news')
    #g2
    frm02 = Frame(frm_guide,bg='white')
    frm02.grid(row=1,column=0,pady=10,padx=30)
    Label(frm02,image=g02,bg='white').grid(row=0,rowspan=4,column=0)
    Label(frm02,text='ชื่อ : มนัสนันท์  ไชยนุสถาน',bg='white',font="Time 15 bold",justify=LEFT).grid(row=0,column=1,sticky='news')
    Label(frm02,text='อายุ : 21 ปี',bg='white',font="Time 15 bold",justify=LEFT).grid(row=1,column=1,sticky='news')
    Label(frm02,text='เพศ : หญิง',bg='white',font="Time 15 bold",justify=LEFT).grid(row=2,column=1,sticky='news')
    Label(frm02,text='ภาษา : พื้นเมือง , อังกฤษ , เกาหลี',bg='white',font="Time 15 bold",justify=LEFT).grid(row=3,column=1,sticky='news')
    Button(frm02,text='Booking',bg='black',fg='white',font="Time 15 bold",command=lambda:select_guide("G02")).grid(row=4,column=0,columnspan=2,sticky='news')
    #g3
    frm03 = Frame(frm_guide,bg='white')
    frm03.grid(row=0,column=1,pady=10,padx=20)
    Label(frm03,image=g03,bg='white').grid(row=0,rowspan=4,column=0)
    Label(frm03,text='ชื่อ : ทินกร ยอดดอย',bg='white',font="Time 15 bold",justify=LEFT).grid(row=0,column=1,sticky='news')
    Label(frm03,text='อายุ : 33 ปี',bg='white',font="Time 15 bold",justify=LEFT).grid(row=1,column=1,sticky='news')
    Label(frm03,text='เพศ : ชาย',bg='white',font="Time 15 bold",justify=LEFT).grid(row=2,column=1,sticky='news')
    Label(frm03,text='ภาษา : พื้นเมือง , อังกฤษ , สเปน',bg='white',font="Time 15 bold",justify=LEFT).grid(row=3,column=1,sticky='news')
    Button(frm03,text='Booking',bg='black',fg='white',font="Time 15 bold",command=lambda:select_guide("G03")).grid(row=4,column=0,columnspan=2,sticky='news')
    #g4
    frm04 = Frame(frm_guide,bg='white')
    frm04.grid(row=1,column=1,pady=10,padx=20)
    Label(frm04,image=g04,bg='white').grid(row=0,rowspan=4,column=0)
    Label(frm04,text='ชื่อ : รามิล  องอาจ',bg='white',font="Time 15 bold",justify=LEFT).grid(row=0,column=1,sticky='news')
    Label(frm04,text='อายุ : 24 ปี',bg='white',font="Time 15 bold",justify=LEFT).grid(row=1,column=1,sticky='news')
    Label(frm04,text='เพศ : ชาย',bg='white',font="Time 15 bold",justify=LEFT).grid(row=2,column=1,sticky='news')
    Label(frm04,text='ภาษา : พื้นเมือง , อังกฤษ , จีน',bg='white',font="Time 15 bold",justify=LEFT).grid(row=3,column=1,sticky='news')
    Button(frm04,text='Booking',bg='black',fg='white',font="Time 15 bold",command=lambda:select_guide("G04")).grid(row=4,column=0,columnspan=2,sticky='news')

    frm_menu = Frame(frm_bg,bg='white')
    frm_menu.grid(row=3,column=0,padx=5,pady=5,sticky='news')
    frm_menu.rowconfigure((0),weight=1)
    frm_menu.columnconfigure((0,1,2,3,4,5),weight=1)
    
    Button(frm_menu,image=home,bg='black',command=choosemenu).grid(row=0,column=0,padx=2,sticky='news')
    Button(frm_menu,text="PLAN",bg='black',fg='white',font="Time 18 bold",command=plan).grid(row=0,column=1,padx=2,sticky='news')
    Button(frm_menu,text="REVIEW",bg='black',fg='white',font="Time 18 bold",command=review).grid(row=0,column=2,padx=2,sticky='news')
    Button(frm_menu,text="BOOKING",bg='black',fg='white',font="Time 18 bold",command=booking).grid(row=0,column=3,padx=2,sticky='news')
    Button(frm_menu,text="NAN SHOP",bg='black',fg='white',font="Time 18 bold",command=nanshop).grid(row=0,column=4,padx=2,sticky='news')
    Button(frm_menu,text="GUIDE",bg='black',fg='white',font="Time 18 bold",command=guide).grid(row=0,column=5,padx=2,sticky='news')

def select_guide(id_g):
    global main
    frm = Frame(main,bg="black")
    frm.grid(row=0,column=0,sticky='news')
    frm.rowconfigure((0),weight=1)
    frm.columnconfigure((0),weight=1)
    
    frm_bg = Frame(frm,bg="white")
    frm_bg.grid(row=0,column=0,padx=50,pady=50,sticky='news')
    frm_bg.rowconfigure((0,6,7),weight=1)
    frm_bg.columnconfigure((0,1),weight=1)

    Label(frm_bg,text='Booking Guide',bg='white',font="Time 40 bold").grid(row=0,column=0,columnspan=2,pady=10)
    Label(frm_bg,text='Date : ',bg='white',font="Time 25 bold").grid(row=1,column=0,sticky='e',padx=20,pady=5)
    Label(frm_bg,text="Price : 700.00 BAHT",bg='white',font="Time 25 bold").grid(row=4,column=0,columnspan=2,padx=20,pady=5)

    Label(frm_bg,text="* หมายเหตุ : เวลาทำงานของไกด์ คือ ตั้งแต่เวลา 07.00 - 18.00น. เท่านั้น",bg='white',font="Time 15 bold").grid(row=5,column=0,columnspan=2,pady=10)

    dd = Spinbox(frm_bg,from_=1,to=31, justify=LEFT, width=10)
    dd.grid(row=1,column=1,sticky='w',padx=10,pady=5)
    mm = Spinbox(frm_bg,from_=1,to=12, justify=LEFT, width=10)
    mm.grid(row=2,column=1,sticky='w',padx=10,pady=5)
    yy = Spinbox(frm_bg,from_=2021,to=2022,justify=LEFT, width=10)
    yy.grid(row=3,column=1,sticky='w',padx=10,pady=5)

    Button(frm_bg,text='Cancle',bg='black',height=50,fg='white',font="Time 15 bold",command=guide).grid(row=6,column=0,padx=50,pady=20,sticky='e')
    Button(frm_bg,text='Comfirm',bg='black',height=50,fg='white',font="Time 15 bold",command=lambda:pay_billguide(id_g,dd.get(),yy.get(),mm.get())).grid(row=6,column=1,padx=50,pady=20,sticky='w')

def pay_billguide(id_g,dd,yy,mm) :
    date = str(dd) + "-" + str(mm) + "-" + str(yy)
    global main
    frm = Frame(main,bg="black")
    frm.grid(row=0,column=0,sticky='news')
    frm.rowconfigure((0),weight=1)
    frm.columnconfigure((0),weight=1)
    
    frm_bg = Frame(frm,bg="white")
    frm_bg.grid(row=0,column=0,padx=50,pady=50,sticky='news')
    frm_bg.rowconfigure((0,3,4,5),weight=1)
    frm_bg.columnconfigure((0,1),weight=1)

    Label(frm_bg,text='PAY',bg='white',font="Time 50 bold").grid(row=0,column=0,columnspan=2,padx=10,pady=5)
    Label(frm_bg,text='Booking Guide',bg='white',font="Time 30 bold").grid(row=1,column=0,columnspan=2,pady=10)
    Label(frm_bg,text="Price : 700.00 BAHT",bg='white',font="Time 25 bold").grid(row=2,column=0,columnspan=2,padx=10,pady=5)
    Label(frm_bg,image=qrcode,bg='white').grid(row=3,column=0,columnspan=2,pady=15)
    Label(frm_bg,text="* If you already scan this QR code \nPlease click Confirm",bg='white',font="Time 15 bold").grid(row=4,column=0,columnspan=2)

    Button(frm_bg,text='Cancle',bg='black',height=50,fg='white',font="Time 15 bold",command=select_guide).grid(row=5,column=0,padx=50,pady=20,sticky='e')
    Button(frm_bg,text='Comfirm',bg='black',height=50,fg='white',font="Time 15 bold",command=lambda:showbill_bookingguide(id_g,date)).grid(row=5,column=1,padx=50,pady=20,sticky='w')

def showbill_bookingguide(id_g,date):
    #SQL
    sql = "SELECT * FROM  Bill_guide WHERE user = ?"
    cursor.execute(sql,[var_user.get()])
    result = cursor.fetchone()
    if result :
        sql = "UPDATE Bill_guide SET id_guide=?,date=? WHERE user = ?"
        cursor.execute(sql,[id_g,date,var_user.get()])
        conn.commit()
    else :
        sql = "insert into Bill_guide values (?,?,?)"
        cursor.execute(sql,[var_user.get(),id_g,date])
        conn.commit()
    #Layout
    #find info guide
    sql = "SELECT * FROM  guide WHERE  id_guide = ?"
    cursor.execute(sql,[id_g])
    guide_info = cursor.fetchone()

    global main
    frm = Frame(main,bg="black")
    frm.grid(row=0,column=0,sticky='news')
    frm.rowconfigure((0),weight=1)
    frm.columnconfigure((0),weight=1)
    
    frm_bg = Frame(frm,bg="white")
    frm_bg.grid(row=0,column=0,padx=50,pady=50,sticky='news')
    frm_bg.rowconfigure((0,12),weight=1)
    frm_bg.columnconfigure((0,1),weight=1)

    Label(frm_bg,text='Bill',bg='white',font="Time 50 bold").grid(row=0,column=0,columnspan=2,pady=5)
    Label(frm_bg,text='Username : ',bg='white',font="Time 25 bold").grid(row=1,column=0,sticky='e',padx=20,pady=10)
    Label(frm_bg,text='Guide Information',bg='white',fg='blue',font="Time 30 bold").grid(row=2,column=0,columnspan=2,padx=20,pady=5)
    Label(frm_bg,text="ชื่อ : ",bg='white',font="Time 25 bold").grid(row=3,column=0,sticky='e',padx=20,pady=5)
    Label(frm_bg,text="อายุ : ",bg='white',font="Time 25 bold").grid(row=4,column=0,sticky='e',padx=20,pady=5)
    Label(frm_bg,text="เพศ : ",bg='white',font="Time 25 bold").grid(row=5,column=0,sticky='e',padx=20,pady=5)
    Label(frm_bg,text="ภาษา : ",bg='white',font="Time 25 bold").grid(row=6,column=0,sticky='e',padx=20,pady=5)
    Label(frm_bg,text="Contact ",bg='white',fg='blue',font="Time 30 bold").grid(row=7,column=0,columnspan=2,padx=20,pady=5)
    Label(frm_bg,text="Email : ",bg='white',font="Time 25 bold").grid(row=8,column=0,sticky='e',padx=20,pady=5)
    Label(frm_bg,text="Phone No. : ",bg='white',font="Time 25 bold").grid(row=9,column=0,sticky='e',padx=20,pady=5)
    Label(frm_bg,text="Price : 700.00 BAHT",bg='white',font="Time 30 bold").grid(row=10,column=0,columnspan=2,pady=5)
    Label(frm_bg,text="(Paid)",bg='white',fg='green',font="Time 30 ").grid(row=11,column=0,columnspan=2,pady=5)

    Label(frm_bg,text=var_user.get(),bg='white',font="Time 25 bold").grid(row=1,column=1,sticky='w',padx=20,pady=10)
    Label(frm_bg,text=guide_info[1],bg='white',font="Time 25 bold").grid(row=3,column=1,sticky='w',padx=20,pady=5)
    Label(frm_bg,text=guide_info[2],bg='white',font="Time 25 bold").grid(row=4,column=1,sticky='w',padx=20,pady=5)
    Label(frm_bg,text=guide_info[3],bg='white',font="Time 25 bold").grid(row=5,column=1,sticky='w',padx=20,pady=5)
    Label(frm_bg,text=guide_info[4],bg='white',font="Time 25 bold").grid(row=6,column=1,sticky='w',padx=20,pady=5)
   
    Label(frm_bg,text=guide_info[5],bg='white',font="Time 25 bold").grid(row=8,column=1,sticky='w',padx=20,pady=5)
    Label(frm_bg,text=guide_info[6],bg='white',font="Time 25 bold").grid(row=9,column=1,sticky='w',padx=20,pady=5)

    Button(frm_bg,text="Done",height=50,bg='black',fg='white',font="Time 15 bold",command=guide).grid(row=12,column=0,columnspan=2,pady=5)

def checkbill_bookingguide():
    sql = "SELECT * FROM  Bill_guide WHERE user = ?"
    cursor.execute(sql,[var_user.get()])
    result = cursor.fetchone()
    print(result)
    if result :
        #find info guide
        sql = "SELECT * FROM  guide WHERE  id_guide = ?"
        cursor.execute(sql,[result[1]])
        guide_info = cursor.fetchone()
        global main
        frm = Frame(main,bg="black")
        frm.grid(row=0,column=0,sticky='news')
        frm.rowconfigure((0),weight=1)
        frm.columnconfigure((0),weight=1)
    
        frm_bg = Frame(frm,bg="white")
        frm_bg.grid(row=0,column=0,padx=50,pady=50,sticky='news')
        frm_bg.rowconfigure((0,12),weight=1)
        frm_bg.columnconfigure((0,1),weight=1)

        Label(frm_bg,text='Bill',bg='white',font="Time 50 bold").grid(row=0,column=0,columnspan=2,pady=5)
        Label(frm_bg,text='Username : ',bg='white',font="Time 25 bold").grid(row=1,column=0,sticky='e',padx=20,pady=10)
        Label(frm_bg,text='Guide Information',bg='white',fg='blue',font="Time 30 bold").grid(row=2,column=0,columnspan=2,padx=20,pady=5)
        Label(frm_bg,text="ชื่อ : ",bg='white',font="Time 25 bold").grid(row=3,column=0,sticky='e',padx=20,pady=5)
        Label(frm_bg,text="อายุ : ",bg='white',font="Time 25 bold").grid(row=4,column=0,sticky='e',padx=20,pady=5)
        Label(frm_bg,text="เพศ : ",bg='white',font="Time 25 bold").grid(row=5,column=0,sticky='e',padx=20,pady=5)
        Label(frm_bg,text="ภาษา : ",bg='white',font="Time 25 bold").grid(row=6,column=0,sticky='e',padx=20,pady=5)
        Label(frm_bg,text="Contact ",bg='white',fg='blue',font="Time 30 bold").grid(row=7,column=0,columnspan=2,padx=20,pady=5)
        Label(frm_bg,text="Email : ",bg='white',font="Time 25 bold").grid(row=8,column=0,sticky='e',padx=20,pady=5)
        Label(frm_bg,text="Phone No. : ",bg='white',font="Time 25 bold").grid(row=9,column=0,sticky='e',padx=20,pady=5)
        Label(frm_bg,text="Price : 700.00 BAHT",bg='white',font="Time 30 bold").grid(row=10,column=0,columnspan=2,pady=5)
        Label(frm_bg,text="(Paid)",bg='white',fg='green',font="Time 30 ").grid(row=11,column=0,columnspan=2,pady=5)

        Label(frm_bg,text=var_user.get(),bg='white',font="Time 25 bold").grid(row=1,column=1,sticky='w',padx=20,pady=10)
        Label(frm_bg,text=guide_info[1],bg='white',font="Time 25 bold").grid(row=3,column=1,sticky='w',padx=20,pady=5)
        Label(frm_bg,text=guide_info[2],bg='white',font="Time 25 bold").grid(row=4,column=1,sticky='w',padx=20,pady=5)
        Label(frm_bg,text=guide_info[3],bg='white',font="Time 25 bold").grid(row=5,column=1,sticky='w',padx=20,pady=5)
        Label(frm_bg,text=guide_info[4],bg='white',font="Time 25 bold").grid(row=6,column=1,sticky='w',padx=20,pady=5)
   
        Label(frm_bg,text=guide_info[5],bg='white',font="Time 25 bold").grid(row=8,column=1,sticky='w',padx=20,pady=5)
        Label(frm_bg,text=guide_info[6],bg='white',font="Time 25 bold").grid(row=9,column=1,sticky='w',padx=20,pady=5)

        Button(frm_bg,text="Done",height=50,bg='black',fg='white',font="Time 15 bold",command=guide).grid(row=12,column=0,columnspan=2,pady=5)
    else :
        messagebox.showwarning('Admin','Not found your Bill \nPls Booking first.')


main = mainwindow()
createconnection()
popupeditplan = None
popupreview = None
np1,np2,np3,np4,np5,np6,np7,np8 = 0,0,0,0,0,0,0,0
pp1,pp2,pp3,pp4,pp5,pp6,pp7,pp8 = 0,0,0,0,0,0,0,0
logo = PhotoImage(file='logo/logo.png')
home = PhotoImage(file='logo/home.png').subsample(7)
qrcode = PhotoImage(file='logo/QR.png').subsample(5)
g01 = PhotoImage(file='logo/g01.png').subsample(5)
g02 = PhotoImage(file='logo/g02.png').subsample(5)
g03 = PhotoImage(file='logo/g03.png').subsample(5)
g04 = PhotoImage(file='logo/g04.png').subsample(5)
menu01 = PhotoImage(file='menu/01.png').subsample(6)
menu02 = PhotoImage(file='menu/02.png').subsample(6)
menu03 = PhotoImage(file='menu/03.png').subsample(6)
menu04 = PhotoImage(file='menu/04.png').subsample(6)
menu05 = PhotoImage(file='menu/05.png').subsample(6)
s1 = PhotoImage(file='img_travel/s1.png').subsample(3)
t1 = PhotoImage(file='img_travel/t1.png').subsample(3)
t2 = PhotoImage(file='img_travel/t2.png').subsample(3)
t3 = PhotoImage(file='img_travel/t3.png').subsample(3)
t4 = PhotoImage(file='img_travel/t4.png').subsample(3)
t5 = PhotoImage(file='img_travel/t5.png').subsample(3)
t6 = PhotoImage(file='img_travel/t6.png').subsample(3)
t7 = PhotoImage(file='img_travel/t7.png').subsample(3)
t8 = PhotoImage(file='img_travel/t8.png').subsample(3)
t9 = PhotoImage(file='img_travel/t9.png').subsample(3)
c1 = PhotoImage(file='img_travel/c1.png').subsample(3)
c2 = PhotoImage(file='img_travel/c2.png').subsample(3)
c3 = PhotoImage(file='img_travel/c3.png').subsample(3)
c4 = PhotoImage(file='img_travel/c4.png').subsample(3)
c5 = PhotoImage(file='img_travel/c5.png').subsample(3)
c6 = PhotoImage(file='img_travel/c6.png').subsample(3)
c7 = PhotoImage(file='img_travel/c7.png').subsample(3)
c8 = PhotoImage(file='img_travel/c8.png').subsample(3)
c9 = PhotoImage(file='img_travel/c9.png').subsample(3)
c10 = PhotoImage(file='img_travel/c10.png').subsample(3)
n1 = PhotoImage(file='img_travel/n1.png').subsample(3)
n2 = PhotoImage(file='img_travel/n2.png').subsample(3)
n3 = PhotoImage(file='img_travel/n3.png').subsample(3)
n4 = PhotoImage(file='img_travel/n4.png').subsample(3)
n5 = PhotoImage(file='img_travel/n5.png').subsample(3)
n6 = PhotoImage(file='img_travel/n6.png').subsample(3)
n7 = PhotoImage(file='img_travel/n7.png').subsample(3)
n8 = PhotoImage(file='img_travel/n8.png').subsample(3)
n9 = PhotoImage(file='img_travel/n9.png').subsample(3)
n10 = PhotoImage(file='img_travel/n10.png').subsample(3)
h1 = PhotoImage(file='img_travel/h1.png').subsample(4)
h2 = PhotoImage(file='img_travel/h2.png').subsample(4)
h3 = PhotoImage(file='img_travel/h3.png').subsample(4)
h4 = PhotoImage(file='img_travel/h4.png').subsample(4)
h5 = PhotoImage(file='img_travel/h5.png').subsample(4)
h6 = PhotoImage(file='img_travel/h6.png').subsample(4)
h7 = PhotoImage(file='img_travel/h7.png').subsample(4)
h8 = PhotoImage(file='img_travel/h8.png').subsample(4)
h9 = PhotoImage(file='img_travel/h9.png').subsample(4)
h10 = PhotoImage(file='img_travel/h10.png').subsample(4)
h11 = PhotoImage(file='img_travel/h11.png').subsample(4)
h12 = PhotoImage(file='img_travel/h12.png').subsample(4)
h13 = PhotoImage(file='img_travel/h13.png').subsample(4)
h14 = PhotoImage(file='img_travel/h14.png').subsample(4)
h15 = PhotoImage(file='img_travel/h15.png').subsample(4)
h16 = PhotoImage(file='img_travel/h16.png').subsample(4)
h17 = PhotoImage(file='img_travel/h17.png').subsample(4)
h18 = PhotoImage(file='img_travel/h18.png').subsample(4)
h19 = PhotoImage(file='img_travel/h19.png').subsample(4)
h20 = PhotoImage(file='img_travel/h20.png').subsample(4)
p1 = PhotoImage(file='img_travel/p1.png').subsample(4)
p2 = PhotoImage(file='img_travel/p2.png').subsample(4)
p3 = PhotoImage(file='img_travel/p3.png').subsample(4)
p4 = PhotoImage(file='img_travel/p4.png').subsample(4)
p5 = PhotoImage(file='img_travel/p5.png').subsample(4)
p6 = PhotoImage(file='img_travel/p6.png').subsample(4)
p7 = PhotoImage(file='img_travel/p7.png').subsample(4)
p8 = PhotoImage(file='img_travel/p8.png').subsample(4)
rt1 = PhotoImage(file='review/rt1.png').subsample(4)
rt2 = PhotoImage(file='review/rt2.png').subsample(4)
rt3 = PhotoImage(file='review/rt3.png').subsample(4)
rt4 = PhotoImage(file='review/rt4.png').subsample(4)
rt5 = PhotoImage(file='review/rt5.png').subsample(4)
rt6 = PhotoImage(file='review/rt6.png').subsample(4)
rt7 = PhotoImage(file='review/rt7.png').subsample(4)
rt8 = PhotoImage(file='review/rt8.png').subsample(4)
rt9 = PhotoImage(file='review/rt9.png').subsample(4)
rs1 = PhotoImage(file='review/rs1.png').subsample(4)
rc1 = PhotoImage(file='review/rc1.png').subsample(4)
rc2 = PhotoImage(file='review/rc2.png').subsample(4)
rc3 = PhotoImage(file='review/rc3.png').subsample(4)
rc4 = PhotoImage(file='review/rc4.png').subsample(4)
rc5 = PhotoImage(file='review/rc5.png').subsample(4)
rc6 = PhotoImage(file='review/rc6.png').subsample(4)
rc7 = PhotoImage(file='review/rc7.png').subsample(4)
rc8 = PhotoImage(file='review/rc8.png').subsample(4)
rc9 = PhotoImage(file='review/rc9.png').subsample(4)
rc10 = PhotoImage(file='review/rc10.png').subsample(4)
rn1 = PhotoImage(file='review/rn1.png').subsample(4)
rn2 = PhotoImage(file='review/rn2.png').subsample(4)
rn3 = PhotoImage(file='review/rn3.png').subsample(4)
rn4 = PhotoImage(file='review/rn4.png').subsample(4)
rn5 = PhotoImage(file='review/rn5.png').subsample(4)
rn6 = PhotoImage(file='review/rn6.png').subsample(4)
rn7 = PhotoImage(file='review/rn7.png').subsample(4)
rn8 = PhotoImage(file='review/rn8.png').subsample(4)
rn9 = PhotoImage(file='review/rn9.png').subsample(4)
rn10 = PhotoImage(file='review/rn10.png').subsample(4)
star10 = PhotoImage(file='star/star10.png')
star20 = PhotoImage(file='star/star20.png')
star30 = PhotoImage(file='star/star30.png')
star40 = PhotoImage(file='star/star40.png')
star50 = PhotoImage(file='star/star50.png')
star00 = PhotoImage(file='star/star00.png')
star05 = PhotoImage(file='star/star05.png')
star15 = PhotoImage(file='star/star15.png')
star25 = PhotoImage(file='star/star25.png')
star35 = PhotoImage(file='star/star35.png')
star45 = PhotoImage(file='star/star45.png')

var_user = StringVar()
var_pwd = StringVar()
var_fname = StringVar()
var_lname = StringVar()
var_gen = StringVar()
var_newuser = StringVar()
var_newpwd = StringVar()
var_cfpwd = StringVar()
name = StringVar()
date = StringVar()
gen = StringVar()

wellcome()
main.mainloop()
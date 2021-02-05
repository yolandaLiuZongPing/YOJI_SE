from tkinter import *
import sqlite3, sys
from tkinter import StringVar

from tkinter import *
from tkinter import messagebox
import os

def connection():
    try:
        conn = sqlite3.connect("RVL.db")
    except:
        print("cannot connect to the database")
    return conn


def verifier():
    a = b = c = d = e = f = 0
    if not Variable_name.get():
        t1.insert(END, "<>Variable name is required<>\n")
        a = 1
    if not Modbus_no.get():
        t1.insert(END, "<>Modbus Index is required<>\n")
        b = 1
    if not BacNet.get():
        t1.insert(END, "<>BacNet is required<>\n")
        c = 1
    if not MIB.get():
        t1.insert(END, "<>MIB is requrired<>\n")
        d = 1
    if not Alm.get():
        t1.insert(END, "<>ALARM is required<>\n")
        e = 1
    if not Touch.get():
        t1.insert(END, "<>TOUCH is Required<>\n")
        f = 1
    if a == 1 or b == 1 or c == 1 or d == 1 or e == 1 or f == 1:
        return 1
    else:
        return 0


def add_Variable():
    ret = verifier()
    if ret == 0:
        conn = connection()
        cur = conn.cursor()
        cur.execute(
            "CREATE TABLE IF NOT EXISTS VARIABLES(NAME TEXT,Modbus_no INTEGER,BacNet TEXT,PHONE_NO INTEGER,Alm TEXT,Touch TEXT)")
        cur.execute("insert into VARIABLE values(?,?,?,?,?,?)", (
        Variable_name.get(), int(Modbus_no.get()), BacNet.get(), int(MIB.get()), Alm.get(), Touch.get()))
        conn.commit()
        conn.close()
        t1.insert(END, "ADDED SUCCESSFULLY\n")


def view_Variable():
    conn = connection()
    cur = conn.cursor()
    cur.execute("select * from VARIABLES")
    data = cur.fetchall()
    conn.close()
    for i in data:
        t1.insert(END, str(i) + "\n")


def delete_Variable():
    ret = verifier()
    if ret == 0:
        conn = connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM VARIABLES WHERE Modbus_no=?", (int(Modbus_no.get()),))
        conn.commit()
        conn.close()
        t1.insert(END, "SUCCESSFULLY DELETED THE VARIABLE\n")


def update_Info():
    ret = verifier()
    if ret == 0:
        conn = connection()
        cur = conn.cursor()
        cur.execute("UPDATE VARIABLE SET NAME=?,Modbus_no=?,BacNet=?,PHONE_NO=?,Alm=?,Touch=? where Modbus_no=?", (
        Variable_name.get(), int(Modbus_no.get()), BacNet.get(), int(MIB.get()), Alm.get(), Touch.get(),
        int(Modbus_no.get())))
        conn.commit()
        conn.close()
        t1.insert(END, "UPDATED SUCCESSFULLY\n")


def clse():
    sys.exit()

def YOJIScreen():
    root = Tk()
    root.title("YOJI RVL Management System")

    Variable_name = StringVar()
    Modbus_no = StringVar()
    BacNet = StringVar()
    MIB = StringVar()
    Alm: StringVar = StringVar()
    Touch = StringVar()

    label1 = Label(root, text="Variable name:")
    label1.place(x=0, y=0)

    label2 = Label(root, text="Modbus Index:")
    label2.place(x=0, y=30)

    label3 = Label(root, text="BacNet:")
    label3.place(x=0, y=60)

    label4 = Label(root, text="MIB:")
    label4.place(x=0, y=90)

    label5 = Label(root, text="ALARM:")
    label5.place(x=0, y=120)

    label6 = Label(root, text="TOUCH:")
    label6.place(x=0, y=150)

    e1 = Entry(root, textvariable=Variable_name)
    e1.place(x=100, y=0)

    e2 = Entry(root, textvariable=Modbus_no)
    e2.place(x=100, y=30)

    e3 = Entry(root, textvariable=BacNet)
    e3.place(x=100, y=60)

    e4 = Entry(root, textvariable=MIB)
    e4.place(x=100, y=90)

    e5 = Entry(root, textvariable=Alm)
    e5.place(x=100, y=120)

    e6 = Entry(root, textvariable=Touch)
    e6.place(x=100, y=150)

    t1 = Text(root, width=80, height=20)
    t1.grid(row=10, column=1)

    b1 = Button(root, text="ADD VARIABLE", command=add_Variable, width=40)
    b1.grid(row=11, column=0)

    b2 = Button(root, text="VIEW ALL VARIABLES", command=view_Variable, width=40)
    b2.grid(row=12, column=0)

    b3 = Button(root, text="DELETE VARIABLE", command=delete_Variable, width=40)
    b3.grid(row=13, column=0)

    b4 = Button(root, text="UPDATE INFO", command=update_Info, width=40)
    b4.grid(row=14, column=0)

    b5 = Button(root, text="CLOSE", command=clse, width=40)
    b5.grid(row=15, column=0)

    root.mainloop()
##################################################################################################
def register_user():
    username_info = username.get()
    password_info = password.get()
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()
    u_entry.delete(0, END)
    p_entry.delete(0, END)
    messagebox.showinfo("info", "Registration Successful")


def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    u_entry1.delete(0, END)
    p_entry1.delete(0, END)
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            YOJIScreen()
        else:
            messagebox.showinfo("info", "Password has not been recognised")
    else:
        messagebox.showinfo("info", "User not found")


def register():
    global username, password
    global u_entry, p_entry, root1
    root1 = Toplevel(root)
    username = StringVar()
    password = StringVar()
    root1.title("Register")
    root1.configure(bg="#F1C40F")
    w1 = 350
    h1 = 310
    root1.geometry("%dx%d+%d+%d" % (w1, h1, x, y))
    Label(root1, text="Please enter the details below\nin the given empty fields", font=("Georgia", 15),
          bg="#F1C40F").pack()
    Label(root1, text="", bg="#F1C40F").pack()
    Label(root1, text="Username *", font=("Georgia", 15), bg="#F1C40F").pack()
    Label(root1, text="", bg="#F1C40F").pack()
    u_entry = Entry(root1, textvariable=username, width="15", borderwidth=3)
    u_entry.pack()
    Label(root1, text="", bg="#F1C40F").pack()
    Label(root1, text="Password *", font=("Georgia", 15), bg="#F1C40F").pack()
    Label(root1, text="", bg="#F1C40F").pack()
    p_entry = Entry(root1, textvariable=password, width="15", borderwidth=3)
    p_entry.pack()
    Label(root1, text="", bg="#F1C40F").pack()
    button = Button(root1, text="Register", width=10, command=lambda: register_user(), bg="#F9E79F",
                    font=("Georgia", 12)).pack()
    root1.mainloop()


def login():
    global root2, u_entry1, p_entry1
    global username_verify, password_verify
    username_verify = StringVar()
    password_verify = StringVar()
    root2 = Toplevel(root)
    w2 = 350
    h2 = 250
    root2.geometry("%dx%d+%d+%d" % (w2, h2, x, y))
    root2.configure(bg="#AF7AC5")
    root2.title("Login")
    Label(root2, text="Username", bg="#AF7AC5", font=("Georgia", 17)).pack()
    Label(root2, text="", bg="#AF7AC5").pack()
    u_entry1 = Entry(root2, textvariable=username_verify, width=15, borderwidth=3)
    u_entry1.pack()
    Label(root2, text="", bg="#AF7AC5").pack()
    Label(root2, text="Password", bg="#AF7AC5", font=("Georgia", 17)).pack()
    Label(root2, text="", bg="#AF7AC5").pack()
    p_entry1 = Entry(root2, textvariable=password_verify, width=15, borderwidth=3)
    p_entry1.pack()
    Label(root2, text="", bg="#AF7AC5").pack()
    button1 = Button(root2, text="Login", width=10, command=lambda: login_verify(), bg="#D7BDE2",
                     font=("Georgia", 13)).pack()
    root2.mainloop()


def mainscreen():
    global root, screen_w, screen_h, x, y
    root = Tk()
    screen_w = root.winfo_screenwidth()
    screen_h = root.winfo_screenheight()
    w = 350
    h = 200
    x = screen_w / 2.7
    y = screen_h / 2.7
    root.geometry("%dx%d+%d+%d" % (w, h, x, y))
    root.title("Register-Login")
    root.configure(bg="#1ABC9C")
    heading = Label(root, text="Register/Login Form", font=("Georgia", 18), bg="#1ABC9C").pack()
    Label(root, text="", bg="#1ABC9C").pack()
    login_button = Button(root, text="Login", width="300", font=("Georgia", 15), bg="#A3E4D7",
                          command=lambda: login()).pack()
    Label(root, text="", bg="#1ABC9C").pack()
    register_button = Button(root, text="Register", width="300", font=("Georgia", 15), bg="#A3E4D7",
                             command=lambda: register()).pack()
    Label(root, text="", bg="#1ABC9C").pack()
    root.mainloop()


# mainscreen()



if __name__ == "__main__":
    mainscreen()


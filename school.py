#!/usr/bin/env python
# coding: utf-8

from tkinter import *
from tkinter import ttk
import pymysql.cursors
import pymysql
from tkinter import messagebox


class Student:
    def __init__(self,root, username, user_password):
        self.root = root
        self.root.title("STUDENT MANAGEMENT System")
        self.username = username
        self.user_password = user_password
        self.root.geometry("1350x700+0+0")

        title = Label(self.root,text="Student Management System",
                      bd=10,relief=GROOVE,
                    font=("times new roman",40,
                      "bold"),bg="yellow")
        title.pack(side=TOP,fill=X)

        #============================All variables in the program=====================
        self.roll_no = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.gender_var = StringVar()


        self.searchby = StringVar()
        self.search_txt = StringVar()
        #>>>>>>>>>>>>>>>>>>>Manage frame>>>>>>>>>
        manage_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        manage_Frame.place(x=20,y=100,width=470,height=600)

        ################Labels and Entries for the db ########################

        lbl_roll= Label(manage_Frame,text="ADM No.",bg="crimson",fg="white",
                      font=("times new roman",20,
                      "bold"))
        lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky="w")

        txt_Roll= Entry(manage_Frame,textvariable=self.roll_no,
                      font=("times new roman",15,
                      "bold"),bd=5,relief=GROOVE)
        txt_Roll.grid(row=1,column=1,pady=10,padx=20,sticky="w")


        lbl_name= Label(manage_Frame,text="Name ",bg="crimson",fg="white",
                      font=("times new roman",20,
                      "bold"))
        lbl_name.grid(row=2,column=0,pady=10,padx=20,sticky="w")

        txt_Name= Entry(manage_Frame,textvariable=self.name_var,font=("times new roman",15,
                      "bold"),bd=5,relief=GROOVE)
        txt_Name.grid(row=2,column=1,pady=10,padx=20,sticky="w")

        lbl_Email= Label(manage_Frame,text="Email ",bg="crimson",fg="white",
                      font=("times new roman",20,
                      "bold"))
        lbl_Email.grid(row=3,column=0,pady=10,padx=20,sticky="w")

        txt_Email= Entry(manage_Frame,textvariable=self.email_var,font=("times new roman",15,
                      "bold"),bd=5,relief=GROOVE)
        txt_Email.grid(row=3,column=1,pady=10,padx=20,sticky="w")


        lbl_Gender= Label(manage_Frame,text="Gender ",bg="crimson",fg="white",
                      font=("times new roman",20,
                      "bold"))
        lbl_Gender.grid(row=4,column=0,pady=10,padx=20,sticky="w")

        combo_gender=ttk.Combobox(manage_Frame,textvariable=self.gender_var,font=("times new roman",20,"bold"))
        combo_gender['values']=("Male","Female","Other")
        combo_gender.grid(row=4,column=1,padx=20,pady=10)



         ###BUTTON FRAME#################

        btn_Frame = Frame(manage_Frame,bd=4,relief=RIDGE,bg="crimson")
        btn_Frame.place(x=0,y=500,width=470)

        Add_btn = Button(btn_Frame,text ="Add",width=10).grid(row=0,column=0,padx=10,pady=10)
        update_btn = Button(btn_Frame,text ="Update",width=10).grid(row=0,column=1,padx=10,pady=10)
        delete_btn = Button(btn_Frame,text ="Delete",width=10).grid(row=0,column=2,padx=10,pady=10)
        clear_btn = Button(btn_Frame,text ="Clear",width=9,command=self.clear_all).grid(row=0,column=3,padx=10,pady=10)

        #>>>>>>>>>>>Details Frame>>>>>>>>>>>>>>>>>>>
        Detail_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        Detail_Frame.place(x=500,y=100,width=800,height=600)

        m_title =Label(manage_Frame,text="Manage Students",
                       bg="crimson",fg="white",
                      font=("times new roman",30,
                      "bold"))
        m_title.grid(row=0,columnspan=2,pady=20)



        lbl_search= Label(Detail_Frame,text="Search By  ",bg="crimson",fg="white",
                      font=("times new roman",20,
                      "bold"))
        lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

        combo_search=ttk.Combobox(Detail_Frame,textvariable=self.searchby,width=10,font=("times new roman",20,"bold"),
                                 state='readonly')
        combo_search['values']=("Roll_No","Name","Gender")
        combo_search.grid(row=0,column=1,padx=20,pady=10)

        txt_search = Entry(Detail_Frame,textvariable=self.search_txt,width=15,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
        txt_search.grid(row=0,column=2,padx=20,pady=10,sticky="w")


        searchbtn = Button(Detail_Frame,text ="Search",width=10,pady=5).grid(row=0,column=3,padx=10,pady=10)
        showallbtn = Button(Detail_Frame,text ="Show All",width=10,pady=5).grid(row=0,column=4,padx=10,pady=10)

        #>>>>>>>>>>>Table Frame>>>>>>>>>>>>>>>>>>>
        Table_Frame = Frame(Detail_Frame,bd=4,relief=RIDGE,bg="crimson")
        Table_Frame.place(x=10,y=70,width=760,height=500)


        scroll_x = Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame,orient=VERTICAL)
        self.Student_table=ttk.Treeview(Table_Frame,columns=("roll","name","email","gender"),
                                  xscrollcommand= scroll_x.set,yscrollcommand= scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)

        self.Student_table.heading("roll",text="Roll No")
        self.Student_table.heading("name",text="Name")
        self.Student_table.heading("email",text="Email")
        self.Student_table.heading("gender",text="Gender")

        self.Student_table['show']='headings'

        # self.Student_table.column("roll",width=100)
        # self.Student_table.column("name",width=100)
        # self.Student_table.column("email",width=150)
        # self.Student_table.column("gender",width=100)

        self.Student_table.pack(fill=BOTH,expand=1)
        self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)
        # self.fetch_data()



    def add_students(self):

        if self.roll_no.get()=="" or self.name_var.get()=="":
            messagebox.showerror("ERRoR","All fields are required !!")
        else:


            con=pymysql.connect(host="localhost",user=self.username,password= self.user_password,database="stm",charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
            cur=con.cursor()
            cur.execute("insert into students values(%s,%s,%s,%s)",(self.roll_no.get(),
                        self.name_var.get(),
                        self.email_var.get(),self.gender_var.get()))
            con.commit()
            # self.fetch_data()
            self.clear_all()
            con.close()
            messagebox.showinfo("Success","recod added")


    def fetch_data(self):
        con=pymysql.connect(host="localhost",user=self.username, password= self.user_password, database="stm")
        cur=con.cursor()
        cur.execute("SELECT * FROM students")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)

            con.commit()
        con.close()

    def clear_all(self):
        self.roll_no.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.gender_var.set("")


    def get_cursor(self,ev):
        curosor_row=self.Student_table.focus()
        contents=self.Student_table.item(curosor_row)
        row=contents['values']


        self.roll_no.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])

    def update_data(self):
        con=pymysql.connect(host="localhost",user=self.username, password= self.user_password, database="stm")
        cur=con.cursor()
        cur.execute("update students set name=%s,email=%s,gender=%s WHERE roll_no=%s",(self.name_var.get(),
                    self.email_var.get(),self.gender_var.get(),self.roll_no.get(),
                    ))

        con.commit()
        # self.fetch_data()
        self.clear_all()
        con.close()

    def delete_data(self):
        con=pymysql.connect(host="localhost", user=self.username, password=self.user_password, database="stm")
        cur=con.cursor()
        cur.execute("delete  FROM students WHERE roll_no=%s",self.roll_no.get())
        con.commit()
        con.close()

        # self.fetch_data()
        self.clear()

    def search_data(self):
        con=pymysql.connect(host="localhost", user=self.username, password=self.user_password, database="stm")
        cur=con.cursor()
        cur.execute("SELECT * FROM students WHERE "+str(self.searchby.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)

            con.commit()
        con.close()



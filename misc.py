from tkinter import *
from tkinter import ttk, messagebox
from tkinter.messagebox import askquestion

import pymysql
import tkinter as tk

class MiscClass:
    def __init__(self, myframe):
        self.mytop = Toplevel(myframe)

        self.mytop.geometry("1130x560+213+128")
        self.mytop.title("Miscellaneous")
        self.mytop.configure(background="#ffe5b4")
        self.mytop.configure(highlightbackground="#d9d9d9")
        self.mytop.configure(highlightcolor="black")

        self.Frame1 = tk.Frame(self.mytop)
        self.Frame1.place(relx=0.009, rely=0.018, relheight=0.973
                , relwidth=0.982)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#ffe5b4")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")
        self.Frame1.configure(width=1110)


        self.TNotebook1 = ttk.Notebook(self.Frame1)
        self.TNotebook1.place(relx=0.009, rely=0.018, relheight=0.965
                , relwidth=0.977)
        self.TNotebook1.configure(width=1084)
        self.TNotebook1.configure(takefocus="")


        #initiating with the next frame
        self.TNotebook1_t1 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t1, padding=3)
        self.TNotebook1.tab(0, text="Staff Data", compound="left", underline="-1"
                ,)
        self.TNotebook1_t1.configure(background="#ffe5b4")
        self.TNotebook1_t1.configure(highlightbackground="#d9d9d9")
        self.TNotebook1_t1.configure(highlightcolor="black")

        self.Label8 = tk.Label(self.TNotebook1_t1)
        self.Label8.place(relx=0.034, rely=0.063, height=21, width=92)
        self.Label8.configure(background="#ffe5b4")
        self.Label8.configure(disabledforeground="#a3a3a3")
        self.Label8.configure(foreground="#000000")
        self.Label8.configure(text='''Search By Name''')

        self.Entry6 = tk.Entry(self.TNotebook1_t1)
        self.Entry6.place(relx=0.193, rely=0.063, height=20, relwidth=0.186)
        self.Entry6.configure(background="white")
        self.Entry6.configure(disabledforeground="#a3a3a3")
        self.Entry6.configure(font="TkFixedFont")
        self.Entry6.configure(foreground="#000000")
        self.Entry6.configure(insertbackground="black")

        self.Button4 = tk.Button(self.TNotebook1_t1)
        self.Button4.place(relx=0.42, rely=0.063, height=20, width=46)
        self.Button4.configure(activebackground="#ececec")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#d9d9d9")
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''Search''',command=self.searchinfo)

        self.TSeparator1 = ttk.Separator(self.TNotebook1_t1)
        self.TSeparator1.place(relx=0.034, rely=0.146, relwidth=0.955)

        mytablearea1 = Frame(self.TNotebook1_t1)
        scrollbarx1 = Scrollbar(mytablearea1, orient=HORIZONTAL)
        scrollbary1 = Scrollbar(mytablearea1, orient=VERTICAL)

        self.mytable1 = ttk.Treeview(mytablearea1, columns=("fname","qualf","salary","phone","email"),
                                    xscrollcommand=scrollbarx1.set, yscrollcommand=scrollbary1.set)
        self.mytable1['show'] = 'headings'
        scrollbarx1.config(command=self.mytable1.xview)
        scrollbary1.config(command=self.mytable1.yview)

        scrollbarx1.pack(side=BOTTOM, fill=X)
        scrollbary1.pack(side=RIGHT, fill=Y)

        self.mytable1.heading("fname", text="Name")
        self.mytable1.heading("qualf", text="Qualification")
        self.mytable1.heading("salary", text="Salary")
        self.mytable1.heading("phone", text="Phone Number")
        self.mytable1.heading("email", text="Email Address")

        self.mytable1.column('#0', stretch=NO)
        self.mytable1.column('#1', stretch=NO)
        self.mytable1.column('#2', stretch=NO)
        self.mytable1.column('#3', stretch=NO)
        self.mytable1.column('#4', stretch=NO)
        self.mytable1.column('#5', stretch=NO)

        self.mytable1.pack()
        mytablearea1.place(relx=0.04, rely=0.188, height=371, width=1000)


        self.TNotebook1_t0 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t0, padding=3)
        self.TNotebook1.tab(1, text="Product Data", compound="left"
                            , underline="-1", )
        self.TNotebook1_t0.configure(background="#ffe5b4")
        self.TNotebook1_t0.configure(highlightbackground="#d9d9d9")
        self.TNotebook1_t0.configure(highlightcolor="black")

        self.Label81 = tk.Label(self.TNotebook1_t0)
        self.Label81.place(relx=0.034, rely=0.063, height=21, width=92)
        self.Label81.configure(background="#ffe5b4")
        self.Label81.configure(disabledforeground="#a3a3a3")
        self.Label81.configure(foreground="#000000")
        self.Label81.configure(text='''Search By Name''')

        self.Entry61 = tk.Entry(self.TNotebook1_t0)
        self.Entry61.place(relx=0.193, rely=0.063, height=20, relwidth=0.186)
        self.Entry61.configure(background="white")
        self.Entry61.configure(disabledforeground="#a3a3a3")
        self.Entry61.configure(font="TkFixedFont")
        self.Entry61.configure(foreground="#000000")
        self.Entry61.configure(insertbackground="black")

        self.Button41 = tk.Button(self.TNotebook1_t0)
        self.Button41.place(relx=0.42, rely=0.063, height=20, width=46)
        self.Button41.configure(activebackground="#ececec")
        self.Button41.configure(activeforeground="#000000")
        self.Button41.configure(background="#d9d9d9")
        self.Button41.configure(disabledforeground="#a3a3a3")
        self.Button41.configure(foreground="#000000")
        self.Button41.configure(highlightbackground="#d9d9d9")
        self.Button41.configure(highlightcolor="black")
        self.Button41.configure(pady="0")
        self.Button41.configure(text='''Search''', command=self.searchprod)


        self.TSeparator11 = ttk.Separator(self.TNotebook1_t0)
        self.TSeparator11.place(relx=0.034, rely=0.146, relwidth=0.955)

        mytablearea = Frame(self.TNotebook1_t0)
        scrollbarx = Scrollbar(mytablearea, orient=HORIZONTAL)
        scrollbary = Scrollbar(mytablearea, orient=VERTICAL)

        self.mytable = ttk.Treeview(mytablearea, columns=("name", "price", "cat", "esttime"),
                                    xscrollcommand=scrollbarx.set, yscrollcommand=scrollbary.set)
        self.mytable['show'] = 'headings'
        scrollbarx.config(command=self.mytable.xview)
        scrollbary.config(command=self.mytable.yview)

        scrollbarx.pack(side=BOTTOM, fill=X)
        scrollbary.pack(side=RIGHT, fill=Y)

        self.mytable.heading("name", text="Product Name")
        self.mytable.heading("price", text="Price")
        self.mytable.heading("cat", text="Category")
        self.mytable.heading("esttime", text=" Waiting  ")

        self.mytable.column('#0', stretch=NO)
        self.mytable.column('#1', stretch=NO)
        self.mytable.column('#2', stretch=NO)
        self.mytable.column('#3', stretch=NO)
        self.mytable.column('#4', stretch=NO)

        self.mytable.pack()
        mytablearea.place(relx=0.04, rely=0.188, height=371, width=1000)
        ####


        self.TNotebook1_t2 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t2, padding=3)
        self.TNotebook1.tab(2, text="Phonebook Data", compound="none", underline="-1"
                ,)
        self.TNotebook1_t2.configure(background="#ffe5b4")
        self.TNotebook1_t2.configure(highlightbackground="#d9d9d9")
        self.TNotebook1_t2.configure(highlightcolor="black")


        self.Label82 = tk.Label(self.TNotebook1_t2)
        self.Label82.place(relx=0.034, rely=0.063, height=21, width=92)
        self.Label82.configure(background="#ffe5b4")
        self.Label82.configure(disabledforeground="#a3a3a3")
        self.Label82.configure(foreground="#000000")
        self.Label82.configure(text='''Search By Name''')

        self.Entry62 = tk.Entry(self.TNotebook1_t2)
        self.Entry62.place(relx=0.193, rely=0.063, height=20, relwidth=0.186)
        self.Entry62.configure(background="white")
        self.Entry62.configure(disabledforeground="#a3a3a3")
        self.Entry62.configure(font="TkFixedFont")
        self.Entry62.configure(foreground="#000000")
        self.Entry62.configure(insertbackground="black")

        self.Button42 = tk.Button(self.TNotebook1_t2)
        self.Button42.place(relx=0.42, rely=0.063, height=20, width=46)
        self.Button42.configure(activebackground="#ececec")
        self.Button42.configure(activeforeground="#000000")
        self.Button42.configure(background="#d9d9d9")
        self.Button42.configure(disabledforeground="#a3a3a3")
        self.Button42.configure(foreground="#000000")
        self.Button42.configure(highlightbackground="#d9d9d9")
        self.Button42.configure(highlightcolor="black")
        self.Button42.configure(pady="0")
        self.Button42.configure(text='''Search''', command=self.searchbook)


        self.TSeparator12 = ttk.Separator(self.TNotebook1_t2)
        self.TSeparator12.place(relx=0.034, rely=0.146, relwidth=0.955)


        mytablearea2 = Frame(self.TNotebook1_t2)
        scrollbarx2 = Scrollbar(mytablearea2, orient=HORIZONTAL)
        scrollbary2 = Scrollbar(mytablearea2, orient=VERTICAL)

        self.mytable2 = ttk.Treeview(mytablearea2, columns=("custname", "occu", "email", "phone"),
                                    xscrollcommand=scrollbarx2.set, yscrollcommand=scrollbary2.set)
        self.mytable2['show'] = 'headings'
        scrollbarx2.config(command=self.mytable2.xview)
        scrollbary2.config(command=self.mytable2.yview)

        scrollbarx2.pack(side=BOTTOM, fill=X)
        scrollbary2.pack(side=RIGHT, fill=Y)

        self.mytable2.heading("custname", text="Customer Name")
        self.mytable2.heading("occu", text="Occupation")
        self.mytable2.heading("email", text="Email")
        self.mytable2.heading("phone", text="Phone")

        self.mytable2.column('#0', stretch=NO)
        self.mytable2.column('#1', stretch=NO)
        self.mytable2.column('#2', stretch=NO)
        self.mytable2.column('#3', stretch=NO)
        self.mytable2.column('#4', stretch=NO)

        self.mytable2.pack()
        mytablearea2.place(relx=0.04, rely=0.188, height=371, width=1000)


    def searchinfo(self):
        try:
            mydatabaseobj = pymysql.connect(host="localhost", user="root", password="",
                                            db="office")
            try:

                with mydatabaseobj.cursor() as myconn:
                    myconn.execute("select fname,qualf,salary,phone,email from stafftable where fname like %s", (self.Entry6.get() + "%"))
                    myresultdata = myconn.fetchall()
                    self.mytable1.delete(*self.mytable1.get_children())
                    for row in myresultdata:
                        self.mytable1.insert('', END, value=(row))

                    if myresultdata == None:
                        messagebox.showerror("No Records Found", "No Staff added yet.")

            except Exception as ex:
                messagebox.showerror("Error Occured", "Error in fetching due to " + str(ex))
            finally:
                mydatabaseobj.close()
        except Exception as ex:
            messagebox.showerror("Error Occured", "Error creating database due to " + str(ex))

    def searchbook(self):
        try:
            mydatabaseobj = pymysql.connect(host="localhost", user="root", password="",
                                            db="office")
            try:

                with mydatabaseobj.cursor() as myconn:
                    myconn.execute("select custname, occu, email,phone from phonebook where custname like %s", (self.Entry62.get() + "%"))
                    myresultdata = myconn.fetchall()
                    self.mytable2.delete(*self.mytable2.get_children())
                    for row in myresultdata:
                        self.mytable2.insert('', END, value=(row))

                    if myresultdata == None:
                        messagebox.showerror("No Records Found", "No customer records added yet.")

            except Exception as ex:
                messagebox.showerror("Error Occured", "Error in fetching due to " + str(ex))
            finally:
                mydatabaseobj.close()
        except Exception as ex:
            messagebox.showerror("Error Occured", "Error creating database due to " + str(ex))


    def searchprod(self):
        try:
            mydatabaseobj = pymysql.connect(host="localhost", user="root", password="",
                                            db="office")
            try:

                with mydatabaseobj.cursor() as myconn:
                    myconn.execute("select name, price, cat,esttime from producttable where name like %s", (self.Entry61.get() + "%"))
                    myresultdata = myconn.fetchall()
                    self.mytable.delete(*self.mytable.get_children())
                    for row in myresultdata:
                        self.mytable.insert('', END, value=(row))

                    if myresultdata == None:
                        messagebox.showerror("No Records Found", "No Products added yet.")

            except Exception as ex:
                messagebox.showerror("Error Occured", "Error in fetching due to " + str(ex))
            finally:
                mydatabaseobj.close()
        except Exception as ex:
            messagebox.showerror("Error Occured", "Error creating database due to " + str(ex))


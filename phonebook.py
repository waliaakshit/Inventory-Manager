import traceback
from tkinter import *
from tkinter import ttk, messagebox
from tkinter.messagebox import askquestion

import pymysql as pymysql
import tkinter as tk


class AddPhone:
    def __init__(self, myframe):
        self.mytop = Toplevel(myframe)
        self.mytop.geometry("1130x560+213+128")
        self.mytop.title("customer records")
        self.mytop.configure(background="#ffe5b4")
        self.mytop.configure(highlightbackground="#d9d9d9")
        self.mytop.configure(highlightcolor="black")

        self.TNotebook1 = ttk.Notebook(self.mytop)
        self.TNotebook1.place(relx=0.013, rely=0.038, relheight=0.953
                              , relwidth=0.979)
        self.TNotebook1.configure(width=754)
        self.TNotebook1.configure(takefocus="")
        self.TNotebook1_t0 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t0, padding=3)
        self.TNotebook1.tab(0, text="Adding Informtion", compound="left", underline="-1", )
        self.TNotebook1_t0.configure(background="#ffe5b4")
        self.TNotebook1_t0.configure(highlightbackground="#d9d9d9")
        self.TNotebook1_t0.configure(highlightcolor="black")
        self.TNotebook1_t1 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t1, padding=3)
        self.TNotebook1.tab(1, text="Updating and Deleting Records", compound="left", underline="-1", )
        self.TNotebook1_t1.configure(background="#ffe5b4")
        self.TNotebook1_t1.configure(highlightbackground="#d9d9d9")
        self.TNotebook1_t1.configure(highlightcolor="black")

        self.Label1 = tk.Label(self.TNotebook1_t0)
        self.Label1.place(relx=0.04, rely=0.063, height=21, width=90)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#ffe5b4")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Customer Name''')
        self.Label1.configure(anchor="e")

        self.Entry1 = tk.Entry(self.TNotebook1_t0)
        self.Entry1.place(relx=0.213, rely=0.063, height=20, relwidth=0.179)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="#c4c4c4")
        self.Entry1.configure(selectforeground="black")

        self.Label2 = tk.Label(self.TNotebook1_t0)
        self.Label2.place(relx=0.04, rely=0.146, height=21, width=109)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#ffe5b4")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Email ID''')


        self.Entry2 = tk.Entry(self.TNotebook1_t0)
        self.Entry2.place(relx=0.213, rely=0.146, height=20, relwidth=0.179)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(highlightbackground="#d9d9d9")
        self.Entry2.configure(highlightcolor="black")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(selectbackground="#c4c4c4")
        self.Entry2.configure(selectforeground="black")

        self.Label3 = tk.Label(self.TNotebook1_t0)
        self.Label3.place(relx=0.04, rely=0.229, height=21, width=90)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#ffe5b4")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''Occupation''')
        self.Label3.configure(anchor="e")

        self.Entry3 = tk.Entry(self.TNotebook1_t0)
        self.Entry3.place(relx=0.213, rely=0.229, height=20, relwidth=0.179)
        self.Entry3.configure(background="white")
        self.Entry3.configure(disabledforeground="#a3a3a3")
        self.Entry3.configure(font="TkFixedFont")
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(highlightbackground="#d9d9d9")
        self.Entry3.configure(highlightcolor="black")
        self.Entry3.configure(insertbackground="black")
        self.Entry3.configure(selectbackground="#c4c4c4")
        self.Entry3.configure(selectforeground="black")


        self.Label4 = tk.Label(self.TNotebook1_t0)
        self.Label4.place(relx=0.04, rely=0.313, height=21, width=68)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="#ffe5b4")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''     Phone''')


        self.Entry4 = tk.Entry(self.TNotebook1_t0)
        self.Entry4.place(relx=0.213, rely=0.313, height=20, relwidth=0.179)
        self.Entry4.configure(background="white")
        self.Entry4.configure(disabledforeground="#a3a3a3")
        self.Entry4.configure(font="TkFixedFont")
        self.Entry4.configure(foreground="#000000")
        self.Entry4.configure(highlightbackground="#d9d9d9")
        self.Entry4.configure(highlightcolor="black")
        self.Entry4.configure(insertbackground="black")
        self.Entry4.configure(selectbackground="#c4c4c4")
        self.Entry4.configure(selectforeground="black")

        self.Button1 = tk.Button(self.TNotebook1_t1)
        self.Button1.place(relx=0.453, rely=0.063, height=20, width=46)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Search''',command=self.searchinfo)

        self.Button2 = tk.Button(self.TNotebook1_t0)
        self.Button2.place(relx=0.213, rely=0.5, height=24, width=35)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Save''',command=self.saveinfo)

        self.Button3 = tk.Button(self.TNotebook1_t1)
        self.Button3.place(relx=0.213, rely=0.583, height=24, width=49)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Update''',command=self.updateinfo)

        self.Button4 = tk.Button(self.TNotebook1_t1)
        self.Button4.place(relx=0.293, rely=0.583, height=24, width=44)
        self.Button4.configure(activebackground="#ececec")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#d9d9d9")
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''Delete''',command=self.deleteinfo)

        mytablearea = Frame(self.TNotebook1_t1)
        scrollbarx = Scrollbar(mytablearea, orient=HORIZONTAL)
        scrollbary = Scrollbar(mytablearea, orient=VERTICAL)

        self.mytable = ttk.Treeview(mytablearea, columns=("custname", "occu", "phone","email"),
                                    xscrollcommand=scrollbarx.set, yscrollcommand=scrollbary.set)
        self.mytable['show'] = 'headings'
        scrollbarx.config(command=self.mytable.xview)
        scrollbary.config(command=self.mytable.yview)

        scrollbarx.pack(side=BOTTOM, fill=X)
        scrollbary.pack(side=RIGHT, fill=Y)

        self.mytable.heading("custname", text="Customer")
        self.mytable.heading("occu", text="occupation")
        self.mytable.heading("phone", text="Phone")

        self.mytable.heading("email", text="Email")

        self.mytable.column('#0', stretch=NO, minwidth=0, width=0)
        self.mytable.column('#1', stretch=NO, minwidth=0, width=50)
        self.mytable.column('#2', stretch=NO, minwidth=0, width=140)
        self.mytable.column('#3', stretch=NO, minwidth=0, width=140)
        self.mytable.column('#4', stretch=NO, minwidth=0, width=150)
        self.mytable.bind("<ButtonRelease-1>", self.fetchbysrno)
        self.mytable.pack()
        mytablearea.place(relx=0.453, rely=0.167, height=200, width=500)

        self.Label11 = tk.Label(self.TNotebook1_t1)
        self.Label11.place(relx=0.04, rely=0.063, height=21, width=90)
        self.Label11.configure(activebackground="#f9f9f9")
        self.Label11.configure(activeforeground="black")
        self.Label11.configure(background="#ffe5b4")
        self.Label11.configure(disabledforeground="#a3a3a3")
        self.Label11.configure(foreground="#000000")
        self.Label11.configure(highlightbackground="#d9d9d9")
        self.Label11.configure(highlightcolor="black")
        self.Label11.configure(text='''Customer Name''')
        self.Label11.configure(anchor="e")

        self.Entry11 = tk.Entry(self.TNotebook1_t1)
        self.Entry11.place(relx=0.213, rely=0.063, height=20, relwidth=0.179)
        self.Entry11.configure(background="white")
        self.Entry11.configure(disabledforeground="#a3a3a3")
        self.Entry11.configure(font="TkFixedFont")
        self.Entry11.configure(foreground="#000000")
        self.Entry11.configure(highlightbackground="#d9d9d9")
        self.Entry11.configure(highlightcolor="black")
        self.Entry11.configure(insertbackground="black")
        self.Entry11.configure(selectbackground="#c4c4c4")
        self.Entry11.configure(selectforeground="black")

        self.Label21 = tk.Label(self.TNotebook1_t1)
        self.Label21.place(relx=0.04, rely=0.146, height=21, width=109)
        self.Label21.configure(activebackground="#f9f9f9")
        self.Label21.configure(activeforeground="black")
        self.Label21.configure(background="#ffe5b4")
        self.Label21.configure(disabledforeground="#a3a3a3")
        self.Label21.configure(foreground="#000000")
        self.Label21.configure(highlightbackground="#d9d9d9")
        self.Label21.configure(highlightcolor="black")
        self.Label21.configure(text='''Email ID''')


        self.Entry21 = tk.Entry(self.TNotebook1_t1)
        self.Entry21.place(relx=0.213, rely=0.146, height=20, relwidth=0.179)
        self.Entry21.configure(background="white")
        self.Entry21.configure(disabledforeground="#a3a3a3")
        self.Entry21.configure(font="TkFixedFont")
        self.Entry21.configure(foreground="#000000")
        self.Entry21.configure(highlightbackground="#d9d9d9")
        self.Entry21.configure(highlightcolor="black")
        self.Entry21.configure(insertbackground="black")
        self.Entry21.configure(selectbackground="#c4c4c4")
        self.Entry21.configure(selectforeground="black")

        self.Label31 = tk.Label(self.TNotebook1_t1)
        self.Label31.place(relx=0.04, rely=0.229, height=21, width=90)
        self.Label31.configure(activebackground="#f9f9f9")
        self.Label31.configure(activeforeground="black")
        self.Label31.configure(background="#ffe5b4")
        self.Label31.configure(disabledforeground="#a3a3a3")
        self.Label31.configure(foreground="#000000")
        self.Label31.configure(highlightbackground="#d9d9d9")
        self.Label31.configure(highlightcolor="black")
        self.Label31.configure(text='''Occupation''')
        self.Label31.configure(anchor="e")

        self.Entry31 = tk.Entry(self.TNotebook1_t1)
        self.Entry31.place(relx=0.213, rely=0.229, height=20, relwidth=0.179)
        self.Entry31.configure(background="white")
        self.Entry31.configure(disabledforeground="#a3a3a3")
        self.Entry31.configure(font="TkFixedFont")
        self.Entry31.configure(foreground="#000000")
        self.Entry31.configure(highlightbackground="#d9d9d9")
        self.Entry31.configure(highlightcolor="black")
        self.Entry31.configure(insertbackground="black")
        self.Entry31.configure(selectbackground="#c4c4c4")
        self.Entry31.configure(selectforeground="black")

        self.Label41 = tk.Label(self.TNotebook1_t1)
        self.Label41.place(relx=0.04, rely=0.313, height=21, width=68)
        self.Label41.configure(activebackground="#f9f9f9")
        self.Label41.configure(activeforeground="black")
        self.Label41.configure(background="#ffe5b4")
        self.Label41.configure(disabledforeground="#a3a3a3")
        self.Label41.configure(foreground="#000000")
        self.Label41.configure(highlightbackground="#d9d9d9")
        self.Label41.configure(highlightcolor="black")
        self.Label41.configure(text='''     Phone''')


        self.Entry41 = tk.Entry(self.TNotebook1_t1)
        self.Entry41.place(relx=0.213, rely=0.313, height=20, relwidth=0.179)
        self.Entry41.configure(background="white")
        self.Entry41.configure(disabledforeground="#a3a3a3")
        self.Entry41.configure(font="TkFixedFont")
        self.Entry41.configure(foreground="#000000")
        self.Entry41.configure(highlightbackground="#d9d9d9")
        self.Entry41.configure(highlightcolor="black")
        self.Entry41.configure(insertbackground="black")
        self.Entry41.configure(selectbackground="#c4c4c4")
        self.Entry41.configure(selectforeground="black")

    def updateinfo(self):
        try:
            mydatabaseobj = pymysql.connect(host="localhost", user="root", password="",
                                            db="office")
            try:

                with mydatabaseobj.cursor() as myconn:
                    myconn.execute(
                        "update phonebook set occu=%s,email=%s,custname=%s,phone=%s where custname=%s",
                        (self.Entry31.get(),self.Entry21.get(),self.Entry11.get(),self.Entry41.get(), self.compdi
                        ))
                    mydatabaseobj.commit()
                    messagebox.showinfo("Success", "Record Updated Successfully",parent=self.TNotebook1_t0)
            except Exception as ex:
                messagebox.showerror("Error Occured", "Error in insert query due to " + str(ex))
            finally:
                mydatabaseobj.close()


            self.Entry11.delete(0, END)

            self.Entry31.delete(0, END)

            self.Entry41.delete(0, END)

            self.Entry21.delete(0, END)

            self.mytable.delete(*self.mytable.get_children())

        except Exception as ex:
            messagebox.showerror("Error Occured", "Error creating database due to " + str(ex))

    def deleteinfo(self):
        answer = askquestion("Confirm", "Do you really want to delete?", icon="warning")

        if answer == "yes":
            try:
                mydatabaseobj = pymysql.connect(host="localhost", user="root", password="",
                                                db="office")
                try:

                    with mydatabaseobj.cursor() as myconn:
                        myconn.execute(
                            "delete from phonebook where custname=%s",
                            (self.compdi))
                        mydatabaseobj.commit()
                        messagebox.showinfo("Success", "Record Deleted Successfully",parent=self.TNotebook1_t0)
                except Exception as ex:
                    messagebox.showerror("Error Occured", "Error in insert query due to " + str(ex),
                                        )

                finally:
                    mydatabaseobj.close()

                self.Entry11.delete(0, END)
                self.Entry31.delete(0, END)

                self.Entry41.delete(0, END)

                self.Entry21.delete(0, END)

                self.mytable.delete(*self.mytable.get_children())

            except Exception as ex:
                messagebox.showerror("Error Occured", "Error creating database due to " + str(ex))


    def saveinfo(self):

        try:
            mydatabaseobj = pymysql.connect(host="localhost", user="root", password="", db="office")
            try:
                with mydatabaseobj.cursor() as myconn:
                    myconn.execute(
                        "insert into phonebook(occu,custname,email,phone) "
                        "values(%s,%s,%s,%s)",
                        (self.Entry3.get(),self.Entry1.get(),self.Entry2.get(), self.Entry4.get()
                         ))
                    mydatabaseobj.commit()
                    messagebox.showinfo("Success", "Record Saved Successfully", parent=self.TNotebook1_t0)

            except Exception as ex:
                messagebox.showerror("Error Occured", "Error in insert query due to " + str(ex))
            finally:
                mydatabaseobj.close()

            self.Entry1.delete(0, END)
            self.Entry3.delete(0, END)

            self.Entry4.delete(0, END)

            self.Entry2.delete(0, END)



        except Exception as ex:
            messagebox.showerror("Error Occured", "Error creating database due to " + str(ex))


    def searchinfo(self):
        try:
            mydatabaseobj = pymysql.connect(host="localhost", user="root", password="",
                                        db="office")
            try:

                with mydatabaseobj.cursor() as myconn:
                    myconn.execute("select custname, occu,phone,email from phonebook"
                               " where custname like %s", (self.Entry1.get() + "%"))
                    myresultdata = myconn.fetchall()
                    self.mytable.delete(*self.mytable.get_children())
                    for row in myresultdata:
                        self.mytable.insert('', END, value=(row))

                    if myresultdata == None:
                        messagebox.showerror("No Records Found", "No records were added yet.")

            except Exception as ex:
                messagebox.showerror("Error Occured", "Error in fetching due to " + str(ex))
            finally:
                mydatabaseobj.close()
        except Exception as ex:
            messagebox.showerror("Error Occured", "Error creating database due to " + str(ex))


    def fetchbysrno(self, e):
        currentItem = self.mytable.focus()
        contents = self.mytable.item(currentItem)
        selectedRow = contents['values']
        self.compdi = selectedRow[0]
        try:
            mydatabaseobj = pymysql.connect(host="localhost", user="root", password="",
                                        db="office")
            try:

                with mydatabaseobj.cursor() as myconn:
                    myconn.execute("select * from phonebook where custname=%s",
                               (self.compdi))
                    myresultdata = myconn.fetchall()

                    for row in myresultdata:
                        self.Entry21.delete(0, END)
                        self.Entry21.insert(0,row[1])
                        self.Entry11.delete(0,END)
                        self.Entry11.insert(0,row[2])
                        self.Entry31.delete(0, END)
                        self.Entry31.insert(0, row[0])
                        self.Entry41.delete(0, END)
                        self.Entry41.insert(0, row[3])

                    if myresultdata == None:
                        messagebox.showerror("No Records Found", "No records added yet.")

            except Exception as ex:
                traceback.print_exc()
                messagebox.showerror("Error Occured", "Error in fetching due to " + str(ex))
            finally:
                mydatabaseobj.close()
        except Exception as ex:
            messagebox.showerror("Error Occured", "Error creating database due to " + str(ex))







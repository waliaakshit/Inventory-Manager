import traceback
from tkinter import *
from tkinter import ttk, messagebox
from tkinter.messagebox import askquestion

import pymysql as pymysql
import tkinter as tk

from tkcalendar import DateEntry



class Att:

    def __init__(self, myframe):
        self.mytop= tk.Toplevel(myframe)
        self.mytop.geometry("1130x560+213+128")
        self.mytop.title("Attendance Records")
        self.mytop.configure(background="#ffe5b4")
        self.mytop.configure(highlightbackground="#d9d9d9")
        self.mytop.configure(highlightcolor="black")

        self.Frame1 = tk.Frame(self.mytop)
        self.Frame1.place(relx=0.009, rely=0.018, relheight=0.965
                          , relwidth=0.978)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#ffe5b4")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")
        self.Frame1.configure(width=1105)



        self.TNotebook1 = ttk.Notebook(self.Frame1)
        self.TNotebook1.place(relx=0.009, rely=0.018, relheight=0.964
                              , relwidth=0.981)
        self.TNotebook1.configure(width=1084)
        self.TNotebook1.configure(takefocus="")
        self.TNotebook1_t0 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t0, padding=3)
        self.TNotebook1.tab(0, text="Staff Attendance Add or Modify", compound="left", underline="-1"
                            , )
        self.TNotebook1_t0.configure(background="#ffe5b4")
        self.TNotebook1_t0.configure(highlightbackground="#d9d9d9")
        self.TNotebook1_t0.configure(highlightcolor="black")

        self.TNotebook1_t2 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t2, padding=3)
        self.TNotebook1.tab(1, text="Attendance Records", compound="left", underline="-1"
                            , )
        self.TNotebook1_t2.configure(background="#ffe5b4")
        self.TNotebook1_t2.configure(highlightbackground="#d9d9d9")
        self.TNotebook1_t2.configure(highlightcolor="black")

        self.Label1111 = tk.Label(self.TNotebook1_t0)
        self.Label1111.place(relx=0.034, rely=0.068, height=21, width=38)
        self.Label1111.configure(text='''Name''')
        self.Label1111.configure(background="#ffe5b4")

        self.name1 = tk.Entry(self.TNotebook1_t0)
        self.name1.place(relx=0.101, rely=0.068, height=20, relwidth=0.183)

        self.Label311 = tk.Label(self.TNotebook1_t0)
        self.Label311.place(relx=0.034, rely=0.159, height=21, width=34)
        self.Label311.configure(text='''From''')
        self.Label311.configure(background="#ffe5b4")

        self.l14 = tk.Label(self.TNotebook1_t0)
        self.l14.place(relx=0.324, rely=0.159, height=21, width=20)
        self.l14.configure(text='''To''')
        self.l14.configure(background="#ffe5b4")

        self.Ll5 = tk.Label(self.TNotebook1_t0)
        self.Ll5.place(relx=0.034, rely=0.251, height=21, width=124)
        self.Ll5.configure(text='''Total Number Of Days''')
        self.Ll5.configure(background="#ffe5b4")

        self.tdays = tk.Label(self.TNotebook1_t0)
        self.tdays.place(relx=0.212, rely=0.251, height=20, relwidth=0.183)

        self.Ll6 = tk.Label(self.TNotebook1_t0)
        self.Ll6.place(relx=0.034, rely=0.342, height=21, width=136)
        self.Ll6.configure(text='''Number Of Days Present''')
        self.Ll6.configure(background="#ffe5b4")

        self.p = tk.Entry(self.TNotebook1_t0)
        self.p.place(relx=0.212, rely=0.342,height=20, relwidth=0.183)

        self.Ll7 = tk.Label(self.TNotebook1_t0)
        self.Ll7.place(relx=0.034, rely=0.433, height=21, width=134)
        self.Ll7.configure(text='''Number Of Days Absent''')
        self.Ll7.configure(background="#ffe5b4")

        self.a = tk.Entry(self.TNotebook1_t0)
        self.a.place(relx=0.212, rely=0.433,height=20, relwidth=0.183)

        self.Label11 = tk.Label(self.TNotebook1_t0)
        self.Label11.place(relx=0.425, rely=0.068, height=21, width=50)
        self.Label11.configure(text='''Number''')
        self.Label11.configure(background="#ffe5b4")

        self.Entry2 = tk.Entry(self.TNotebook1_t0)
        self.Entry2.place(relx=0.514, rely=0.068, height=20, relwidth=0.183)

        self.savebtn = tk.Button(self.TNotebook1_t0)
        self.savebtn.place(relx=0.212, rely=0.524, height=24, width=35)
        self.savebtn.configure(text='''Save''',command=self.saveinfo)

        self.deleteat = tk.Button(self.TNotebook1_t0)
        self.deleteat.place(relx=0.346, rely=0.524, height=24, width=44)
        self.deleteat.configure(text='''Delete''',command=self.deleteinfo)

        self.Button3 = tk.Button(self.TNotebook1_t0)
        self.Button3.place(relx=0.268, rely=0.524, height=24, width=59)
        self.Button3.configure(text='''Update''',command=self.updateinfo)


        self.fr = DateEntry(self.TNotebook1_t0, background='darkblue', foreground='white', borderwidth=2)
        self.fr.place(relx=0.101, rely=0.159, height=21,relwidth=0.183)

        self.to = DateEntry(self.TNotebook1_t0, background='darkblue', foreground='white', borderwidth=2)
        self.to.place(relx=0.469, rely=0.159, height=21,relwidth=0.183)
        self.to.bind("<Return>", self.mouseev)

        self.searchat = tk.Button(self.TNotebook1_t0)
        self.searchat.place(relx=0.313, rely=0.068, height=20, width=46)
        self.searchat.configure(text='''Search''', command=self.searchinfo)

        self.TSeparator1 = ttk.Separator(self.TNotebook1_t2)
        self.TSeparator1.place(relx=0.034, rely=0.146, relwidth=0.955)


        self.search1=tk.Button(self.TNotebook1_t2)
        self.search1.place(relx=0.456, rely=0.063, height=21, width=92)
        self.search1.configure(text='''SHOW''',command=self.searchinfo1)

        mytablearea = Frame(self.TNotebook1_t0)
        scrollbarx = Scrollbar(mytablearea, orient=HORIZONTAL)
        scrollbary = Scrollbar(mytablearea, orient=VERTICAL)

        self.mytable = ttk.Treeview(mytablearea, columns=("sr_no", "fname", "phone"),
                                    xscrollcommand=scrollbarx.set, yscrollcommand=scrollbary.set)
        self.mytable['show'] = 'headings'
        scrollbarx.config(command=self.mytable.xview)
        scrollbary.config(command=self.mytable.yview)

        scrollbarx.pack(side=BOTTOM, fill=X)
        scrollbary.pack(side=RIGHT, fill=Y)

        self.mytable.heading("sr_no", text="ID")
        self.mytable.heading("fname", text="Name")
        self.mytable.heading("phone", text="Mobile")


        self.mytable.column('#0', stretch=NO,minwidth=0, width=0)
        self.mytable.column('#1', stretch=NO,minwidth=0, width=150)
        self.mytable.column('#2', stretch=NO,minwidth=0, width=150)
        self.mytable.column('#3', stretch=NO,minwidth=0, width=150)

        self.mytable.bind("<ButtonRelease-1>", self.fetchbysrno)
        self.mytable.pack()
        mytablearea.place(relx=0.469, rely=0.251, height=141, width=454)

        mytablearea1 = Frame(self.TNotebook1_t2)
        scrollbarx1 = Scrollbar(mytablearea1, orient=HORIZONTAL)
        scrollbary1 = Scrollbar(mytablearea1, orient=VERTICAL)

        self.mytable1 = ttk.Treeview(mytablearea1,
                                     columns=("sr_no", "name","attfrom","attto",	"pdays",	"adays"),
                                     xscrollcommand=scrollbarx1.set, yscrollcommand=scrollbary1.set)
        self.mytable1['show'] = 'headings'
        scrollbarx1.config(command=self.mytable1.xview)
        scrollbary1.config(command=self.mytable1.yview)

        scrollbarx1.pack(side=BOTTOM, fill=X)
        scrollbary1.pack(side=RIGHT, fill=Y)

        self.mytable1.heading("sr_no", text="ID")
        self.mytable1.heading("name", text="NAME")
        self.mytable1.heading("attfrom", text="Attend From")
        self.mytable1.heading("attto", text="Attend To")

        self.mytable1.heading("pdays", text="Present Days")
        self.mytable1.heading("adays", text="Absent Days")


        self.mytable1.column('#0', stretch=NO, minwidth=0, width=0)
        self.mytable1.column('#1', stretch=NO, minwidth=0, width=142)
        self.mytable1.column('#2', stretch=NO, minwidth=0, width=142)
        self.mytable1.column('#3', stretch=NO, minwidth=0, width=142)
        self.mytable1.column('#4', stretch=NO, minwidth=0, width=142)
        self.mytable1.column('#5', stretch=NO, minwidth=0, width=142)

        self.mytable1.column('#6', stretch=NO, minwidth=0, width=142)

        self.mytable1.pack()
        mytablearea1.place(relx=0.04, rely=0.188, height=371, width=1000)


    def updateinfo(self):
        try:
            mydatabaseobj = pymysql.connect(host="localhost", user="root", password="",
                                            db="office")
            try:

                with mydatabaseobj.cursor() as myconn:
                    myconn.execute(
                        "update attendtable set name=%s,attfrom=%s,attto=%s,pdays=%s,adays=%s where sr_no=%s",
                        (self.name1.get(), self.fr.get_date(),
                         self.to.get_date(), self.p.get(), self.a.get(), self.serialno
                         ))
                    mydatabaseobj.commit()
                    messagebox.showinfo("Success", "Records Updated Successfully", parent=self.TNotebook1_t0)
            except Exception as ex:
                messagebox.showerror("Error Occured", "Error in insert query due to " + str(ex))
            finally:
                mydatabaseobj.close()

            self.Entry2.delete(0, END)
            self.name1.delete(0, END)


            self.fr.delete(0, END)
            self.to.delete(0, END)

            self.a.delete(0, END)

            self.p.delete(0, END)
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
                            "delete from attendtable where sr_no=%s",
                            (self.serialno))
                        mydatabaseobj.commit()
                        messagebox.showinfo("Success", "Record Deleted Successfully", parent=self.TNotebook1_t0)
                except Exception as ex:
                    messagebox.showerror("Error Occured", "Error in insert query due to " + str(ex),
                                         )

                finally:
                    mydatabaseobj.close()

                self.Entry2.delete(0, END)
                self.name1.delete(0, END)

                self.fr.delete(0, END)
                self.to.delete(0, END)

                self.a.delete(0, END)

                self.p.delete(0, END)
                self.mytable.delete(*self.mytable.get_children())

            except Exception as ex:
                messagebox.showerror("Error Occured", "Error creating database due to " + str(ex))


    def searchinfo1(self):
        try:
            mydatabaseobj = pymysql.connect(host="localhost", user="root", password="",
                                            db="office")
            try:

                with mydatabaseobj.cursor() as myconn:
                    myconn.execute("select name,sr_no,attfrom,attto,pdays,adays from attendtable")
                    myresultdata = myconn.fetchall()
                    self.mytable1.delete(*self.mytable1.get_children())
                    for row in myresultdata:
                        self.mytable1.insert('', END, value=(row))

                    if myresultdata == None:
                        messagebox.showerror("No Records Found", "No Staff Members added yet.")

            except Exception as ex:
                messagebox.showerror("Error Occured", "Error in fetching due to " + str(ex))
            finally:
                mydatabaseobj.close()
        except Exception as ex:
            messagebox.showerror("Error Occured", "Error creating database due to " + str(ex))

    def mouseev(self,ev):
        self.delta = self.to.get_date() - self.fr.get_date()
        self.day=self.delta.days
        self.tdays.config(text=self.day)

    def saveinfo(self):

        try:
            mydatabaseobj = pymysql.connect(host="localhost", user="root", password="", db="office")
            try:
                with mydatabaseobj.cursor() as myconn:
                    myconn.execute(
                        "insert into attendtable(name,sr_no,attfrom,attto,pdays,adays) "
                        "values(%s,%s,%s,%s,%s,%s)",
                        (self.name1.get(), self.Entry2.get(), self.fr.get_date(),
                         self.to.get_date(), self.p.get(), self.a.get()
                         ))
                    mydatabaseobj.commit()
                    messagebox.showinfo("Success", "Record Saved Successfully", parent=self.TNotebook1_t0)

            except Exception as ex:
                messagebox.showerror("Error Occured", "Error in insert query due to " + str(ex))
            finally:
                mydatabaseobj.close()
            self.Entry2.delete(0, END)
            self.name1.delete(0, END)


            self.fr.delete(0, END)
            self.to.delete(0, END)

            self.a.delete(0, END)

            self.p.delete(0, END)
            self.mytable.delete(*self.mytable.get_children())

        except Exception as ex:
            messagebox.showerror("Error Occured", "Error creating database due to " + str(ex))



    def searchinfo(self):
        try:
            mydatabaseobj = pymysql.connect(host="localhost", user="root", password="",
                                            db="office")
            try:

                with mydatabaseobj.cursor() as myconn:
                    myconn.execute("select sr_no, fname,phone from stafftable"
                                   " where fname like %s", (self.name1.get() + "%"))
                    myresultdata = myconn.fetchall()
                    self.mytable.delete(*self.mytable.get_children())
                    for row in myresultdata:
                        self.mytable.insert('', END, value=(row))

                    if myresultdata == None:
                        messagebox.showerror("No Records Found", "No Staff Members added yet.")

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
        self.serialno = selectedRow[0]
        try:
            mydatabaseobj = pymysql.connect(host="localhost", user="root", password="",
                                            db="office")
            try:

                with mydatabaseobj.cursor() as myconn:
                    myconn.execute("select * from stafftable where sr_no=%s",
                                   (self.serialno))
                    myresultdata = myconn.fetchall()

                    for row in myresultdata:
                        self.Entry2.delete(0, END)
                        self.Entry2.insert(0, self.serialno)
                        self.name1.delete(0, END)
                        self.name1.insert(0, row[1])

                    if myresultdata == None:
                        messagebox.showerror("No Records Found", "No Staff Members added yet.")

            except Exception as ex:
                traceback.print_exc()
                messagebox.showerror("Error Occured", "Error in fetching due to " + str(ex))
            finally:
                mydatabaseobj.close()
        except Exception as ex:
            messagebox.showerror("Error Occured", "Error creating database due to " + str(ex))

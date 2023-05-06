import time
import traceback
from tkinter import *
from tkinter import ttk, messagebox
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import askquestion

import pymysql as pymysql
import tkinter as tk

from PIL import ImageTk
from tkcalendar import DateEntry


class AddProduct:
    def __init__(self, myframe):
        self.mytop = Toplevel(myframe)
        self.mytop.geometry("1130x560+213+128")
        self.mytop.title("Product database")
        self.mytop.configure(background="#ffe5b4")
        self.mytop.configure(highlightbackground="#d9d9d9")
        self.mytop.configure(highlightcolor="black")



        self.TNotebook1 = ttk.Notebook(self.mytop)
        self.TNotebook1.place(relx=0.02, rely=0.033, relheight=0.943
                              , relwidth=0.968)
        self.TNotebook1.configure(width=964)
        self.TNotebook1.configure(takefocus="")
        self.TNotebook1_t0 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t0, padding=3)
        self.TNotebook1.tab(0, text="Product Information", compound="left", underline="-1", )
        self.TNotebook1_t0.configure(background="#ffe5b4")
        self.TNotebook1_t0.configure(highlightbackground="#d9d9d9")
        self.TNotebook1_t0.configure(highlightcolor="black")
        self.TNotebook1_t1 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t1, padding=3)
        self.TNotebook1.tab(1, text="Search and Update information", compound="left", underline="-1", )
        self.TNotebook1_t1.configure(background="#ffe5b4")
        self.TNotebook1_t1.configure(highlightbackground="#d9d9d9")
        self.TNotebook1_t1.configure(highlightcolor="black")

        self.Label1 = tk.Label(self.TNotebook1_t0)
        self.Label1.place(relx=0.031, rely=0.056, height=21, width=87)
        self.Label1.configure(background="#ffe5b4")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Product Name''')

        self.Entry1 = tk.Entry(self.TNotebook1_t0)
        self.Entry1.place(relx=0.135, rely=0.056, height=20, relwidth=0.171)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")



        self.Label3 = tk.Label(self.TNotebook1_t0)
        self.Label3.place(relx=0.031, rely=0.13, height=21, width=87)
        self.Label3.configure(background="#ffe5b4")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''  Waiting Time''')

        self.Entry3 = tk.Entry(self.TNotebook1_t0)
        self.Entry3.place(relx=0.135, rely=0.13, height=20, relwidth=0.171)
        self.Entry3.configure(background="white")
        self.Entry3.configure(disabledforeground="#a3a3a3")
        self.Entry3.configure(font="TkFixedFont")
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(insertbackground="black")


        self.Label5 = tk.Label(self.TNotebook1_t0)
        self.Label5.place(relx=0.031, rely=0.204, height=21, width=87)
        self.Label5.configure(background="#ffe5b4")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(text=''' Prod. Category''')

        self.prodcat=StringVar()
        self.TCombobox1 = ttk.Combobox(self.TNotebook1_t0)
        self.TCombobox1.place(relx=0.135, rely=0.204, relheight=0.039
                              , relwidth=0.17)
        self.TCombobox1.configure(takefocus="", textvariable=self.prodcat, state='readonly', values=('Android','IOS','KaiOS'))
        self.TCombobox1.configure(width=163)
        self.TCombobox1.set("Choose Category")
        self.TCombobox1.configure(takefocus="")

        self.Label10 = tk.Label(self.TNotebook1_t0)
        self.Label10.place(relx=0.031, rely=0.278, height=21, width=90)
        self.Label10.configure(background="#ffe5b4")
        self.Label10.configure(disabledforeground="#a3a3a3")
        self.Label10.configure(foreground="#000000")
        self.Label10.configure(text='''Product Price''')

        self.Entry7 = tk.Entry(self.TNotebook1_t0)
        self.Entry7.place(relx=0.135, rely=0.278, height=20, relwidth=0.171)
        self.Entry7.configure(background="white")
        self.Entry7.configure(disabledforeground="#a3a3a3")
        self.Entry7.configure(font="TkFixedFont")
        self.Entry7.configure(foreground="#000000")
        self.Entry7.configure(insertbackground="black")

        self.Button1 = tk.Button(self.TNotebook1_t0)
        self.Button1.place(relx=0.135, rely=0.426, height=24, width=35)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Save''',command=self.saveinfo)

        self.img = tk.Label(self.TNotebook1_t0)
        self.img.place(x=450,y=20, height=150, width=150)

        self.Button2 = tk.Button(self.TNotebook1_t0)
        self.Button2.place(x=500,y=225, height=24, width=49)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Upload''',command=self.uploadimage)


        #now we will start designing the second page of the notebook itself.
        self.Label1 = tk.Label(self.TNotebook1_t1)
        self.Label1.place(relx=0.031, rely=0.056, height=21, width=87)
        self.Label1.configure(background="#ffe5b4")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Product Name''')

        self.name = tk.Entry(self.TNotebook1_t1)
        self.name.place(relx=0.135, rely=0.056, height=20, relwidth=0.171)
        self.name.configure(background="white")
        self.name.configure(disabledforeground="#a3a3a3")
        self.name.configure(font="TkFixedFont")
        self.name.configure(foreground="#000000")
        self.name.configure(insertbackground="black")



        self.Label3 = tk.Label(self.TNotebook1_t1)
        self.Label3.place(relx=0.031, rely=0.13, height=21, width=87)
        self.Label3.configure(background="#ffe5b4")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''  Waiting Time''')

        self.ttm = tk.Entry(self.TNotebook1_t1)
        self.ttm.place(relx=0.135, rely=0.13, height=20, relwidth=0.171)
        self.ttm.configure(background="white")
        self.ttm.configure(disabledforeground="#a3a3a3")
        self.ttm.configure(font="TkFixedFont")
        self.ttm.configure(foreground="#000000")
        self.ttm.configure(insertbackground="black")



        self.Label5 = tk.Label(self.TNotebook1_t1)
        self.Label5.place(relx=0.031, rely=0.204, height=21, width=87)
        self.Label5.configure(background="#ffe5b4")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(text=''' Prod. Category''')



        self.prodca = StringVar()
        self.TCombobox = ttk.Combobox(self.TNotebook1_t1)
        self.TCombobox.place(relx=0.135, rely=0.204, relheight=0.039
                              , relwidth=0.17)
        self.TCombobox.configure(takefocus="", textvariable=self.prodca, state='readonly', values=('Android','IOS','KaiOS'))
        self.TCombobox.configure(width=163)
        self.TCombobox.set("Choose Category")
        self.TCombobox.configure(takefocus="")



        self.Label10 = tk.Label(self.TNotebook1_t1)
        self.Label10.place(relx=0.031, rely=0.278, height=21, width=90)
        self.Label10.configure(background="#ffe5b4")
        self.Label10.configure(disabledforeground="#a3a3a3")
        self.Label10.configure(foreground="#000000")
        self.Label10.configure(text='''Product Price''')

        self.pr = tk.Entry(self.TNotebook1_t1)
        self.pr.place(relx=0.135, rely=0.278, height=20, relwidth=0.171)
        self.pr.configure(background="white")
        self.pr.configure(disabledforeground="#a3a3a3")
        self.pr.configure(font="TkFixedFont")
        self.pr.configure(foreground="#000000")
        self.pr.configure(insertbackground="black")

        self.img1 = tk.Label(self.TNotebook1_t1)
        self.img1.place(x=450, y=20, height=150, width=150)
        self.filename = ImageTk.PhotoImage(file="images/phone.png" )
        self.img1.config(image=self.filename)
        self.img.config(image=self.filename)

        self.update = tk.Button(self.TNotebook1_t1)
        self.update.place(relx=0.135, rely=0.426, height=24, width=55)
        self.update.configure(text='Update', command=self.updateinfo)

        self.delete = tk.Button(self.TNotebook1_t1)
        self.delete.place(relx=0.195, rely=0.426, height=24, width=55)
        self.delete.configure(text='Delete', command=self.deleteinfo)

        self.search = tk.Button(self.TNotebook1_t1)
        self.search.place(relx=0.255, rely=0.426, height=24, width=55)
        self.search.configure(text='Search', command=self.searchinfo)

        mytablearea = Frame(self.TNotebook1_t1)
        scrollbarx = Scrollbar(mytablearea, orient=HORIZONTAL)
        scrollbary = Scrollbar(mytablearea, orient=VERTICAL)

        self.mytable = ttk.Treeview(mytablearea, columns=("name", "price", "esttime"),
                                    xscrollcommand=scrollbarx.set, yscrollcommand=scrollbary.set)
        self.mytable['show'] = 'headings'
        scrollbarx.config(command=self.mytable.xview)
        scrollbary.config(command=self.mytable.yview)

        scrollbarx.pack(side=BOTTOM, fill=X)
        scrollbary.pack(side=RIGHT, fill=Y)


        self.mytable.heading("name", text="Name")
        self.mytable.heading("price", text="Price")

        self.mytable.heading("esttime", text="TTD")

        self.mytable.column('#0', stretch=NO, minwidth=0, width=0)
        self.mytable.column('#1', stretch=NO, minwidth=0, width=120)
        self.mytable.column('#2', stretch=NO, minwidth=0, width=140)
        self.mytable.column('#3', stretch=NO, minwidth=0, width=140)

        self.mytable.bind("<ButtonRelease-1>", self.fetchbysrno)
        self.mytable.pack()
        mytablearea.place(relx = 0.500, rely = 0.426, height = 101, width = 414)

    def searchinfo(self):
        try:
            mydatabaseobj = pymysql.connect(host="localhost", user="root", password="",
                                        db="office")
            try:

                with mydatabaseobj.cursor() as myconn:
                    myconn.execute("select name, price,esttime from producttable"
                               " where name like %s", (self.name.get() + "%"))
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


    def fetchbysrno(self, e):
        currentItem = self.mytable.focus()
        contents = self.mytable.item(currentItem)
        selectedRow = contents['values']
        self.serialname = selectedRow[0]
        try:
            mydatabaseobj = pymysql.connect(host="localhost", user="root", password="",
                                        db="office")
            try:

                with mydatabaseobj.cursor() as myconn:
                    myconn.execute("select * from producttable where name=%s",
                               (self.serialname))
                    myresultdata = myconn.fetchall()

                    for row in myresultdata:
                        self.pr.delete(0, END)
                        self.pr.insert(0,row[1])

                        self.name.delete(0,END)
                        self.name.insert(0,row[0])


                        self.ttm.delete(0, END)
                        self.ttm.insert(0, row[3])

                        self.filename = ImageTk.PhotoImage(file="images//" + row[4])
                        self.img1.config(image=self.filename)

                        self.prodca.set(row[2])
                        self.TCombobox1.set(row[2])

                    if myresultdata == None:
                        messagebox.showerror("No Records Found", "No Products added yet.")

            except Exception as ex:
                traceback.print_exc()
                messagebox.showerror("Error Occured", "Error in fetching due to " + str(ex))
            finally:
                mydatabaseobj.close()
        except Exception as ex:
            messagebox.showerror("Error Occured", "Error creating database due to " + str(ex))


    def updateinfo(self):
        try:
            mydatabaseobj = pymysql.connect(host="localhost", user="root", password="",
                                            db="office")
            try:

                with mydatabaseobj.cursor() as myconn:
                    myconn.execute(
                        "update producttable set name=%s,price=%s,cat=%s,esttime=%s where name=%s",
                        (self.name.get(),self.pr.get(),self.TCombobox1.get(),self.ttm.get(),self.name.get()
                        ))
                    mydatabaseobj.commit()
                    messagebox.showinfo("Success", "Record Updated Successfully",parent=self.TNotebook1_t1)
            except Exception as ex:
                messagebox.showerror("Error Occured", "Error in insert query due to " + str(ex))
            finally:
                mydatabaseobj.close()
            self.TCombobox.set('Choose Category')
            self.prodca.set('Choose Category')

            self.pr.delete(0, END)

            self.name.delete(0, END)

            self.ttm.delete(0,END)

            self.filename2 = ImageTk.PhotoImage(file="images/default.png")

            self.img1.config(image=self.filename2)

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
                            "delete from producttable where name=%s",
                            (self.serialname))
                        mydatabaseobj.commit()
                        messagebox.showinfo("Success", "Record Deleted Successfully",parent=self.TNotebook1_t1)
                except Exception as ex:
                    messagebox.showerror("Error Occured", "Error in insert query due to " + str(ex),
                                        )

                finally:
                    mydatabaseobj.close()
                self.TCombobox.set('Choose Category')
                self.prodca.set('Choose Category')

                self.pr.delete(0, END)

                self.name.delete(0, END)

                self.ttm.delete(0, END)

                self.filename2 = ImageTk.PhotoImage(file="images/default.png")

                self.img1.config(image=self.filename2)

                self.mytable.delete(*self.mytable.get_children())


            except Exception as ex:
                messagebox.showerror("Error Occured", "Error creating database due to " + str(ex))


    def saveinfo(self):

        try:
            mydatabaseobj = pymysql.connect(host="localhost", user="root", password="", db="office")



            try:
                with mydatabaseobj.cursor() as myconn:
                    myconn.execute(
                        "insert into producttable(name,price,cat,esttime,image) "
                        "values(%s,%s,%s,%s,%s)",
                        (self.Entry1.get(),self.Entry7.get(),self.TCombobox1.get(),self.Entry3.get(),self.myfinalname
                        ))
                    mydatabaseobj.commit()
                    messagebox.showinfo("Success", "Record Saved Successfully", parent=self.TNotebook1_t0)

            except Exception as ex:
                messagebox.showerror("Error Occured","Please Fill All Blocks!", parent=self.TNotebook1_t0)
            finally:
                mydatabaseobj.close()

            self.prodcat.set('Choose Category')
            self.TCombobox1.set("Choose Category")

            self.Entry7.delete(0, END)
            self.Entry1.delete(0, END)
            self.Entry3.delete(0, END)

            self.filename = ImageTk.PhotoImage(file="images/default.png")

            self.img.config(image=self.filename)

        except Exception as ex:
            messagebox.showerror("Error Occured", "Error creating database due to " + str(ex))


    def uploadimage(self):
        filename = askopenfilename(filetypes=[(("Picture Files", "*.jpg;*.png;*.gif"))])

        self.image = ImageTk.PhotoImage(file=filename)
        mydata = filename.split("/")
        self.myfinalname = str(int(time.time())) + mydata[-1]

        infile = open(filename, "rb")
        outfile = open("images//" + self.myfinalname, "wb")
        for line in infile:
            outfile.write(line)
        infile.close()
        outfile.close()
        self.img.configure(image=self.image)








import traceback
from tkinter import *
from tkinter import ttk, messagebox
from tkinter.messagebox import askquestion
import os
import sys
from Facial_Recognition_Part1 import CreateDataset
import Facial_Recognition_Part1
import pymysql as pymysql

import parent


class CreateAdmin:

    def __init__(self):
        self.mywindow = Tk()
        self.mywindow.wm_title("Running First Time, Create Admin Account")
        self.mywindow.configure(background="#ffe5b4")

        self.mywindow.geometry("800x450+260+110")

        namebox = Label(self.mywindow, text="Username")
        namebox.configure(background="#ffe5b4")
        namebox.place(x=100, y=100)

        self.nameentrybox = Entry(self.mywindow)
        self.nameentrybox.place(x=300, y=100)

        passwordbox = Label(self.mywindow, text="Password")
        passwordbox.configure(background="#ffe5b4")
        passwordbox.place(x=100, y=150)

        self.passwordentrybox = Entry(self.mywindow, show="*")
        self.passwordentrybox.place(x=300, y=150)


        savebtn = Button(self.mywindow, text="Create Admin", command=self.createadmininfo, padx=20)
        savebtn.place(x=300, y=200)


        createimagedata = Button(self.mywindow,text="G images",command=self.run, padx=20)
        createimagedata.place(x=300 , y=250)

        self.mywindow.mainloop()


    def run(self):
        CreateDataset()

    def createadmininfo(self):
        try:
                mydatabaseobj = pymysql.connect(host="localhost", user="root", password="",
                                                db="office")
                try:

                    with mydatabaseobj.cursor() as myconn:
                        myconn.execute("insert into usertable values(%s,%s,%s)", (self.nameentrybox.get(), self.passwordentrybox.get(), "Admin"))
                        mydatabaseobj.commit()
                        messagebox.showinfo("Success", "Admin Account created successfully")
                        self.mywindow.destroy()
                        parent.myparent()

                except Exception as ex:
                    messagebox.showerror("Error Occured", "Error in fetching due to " + str(ex))
                finally:
                    mydatabaseobj.close()
        except Exception as ex:
                messagebox.showerror("Error Occured", "Error creating database due to " + str(ex))



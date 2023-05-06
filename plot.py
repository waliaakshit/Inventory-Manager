from tkinter import *
from tkinter import ttk, messagebox
from tkinter.messagebox import askquestion
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk
from matplotlib.figure import Figure

import pymysql
import tkinter as tk

class PlotFrame:
    def __init__(self, myframe):
        self.mytop = Toplevel(myframe)

        self.mytop.geometry("1130x560+213+128")
        self.mytop.title("Plot Generation")
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

        # initiating with the next frame
        self.TNotebook1_t1 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t1, padding=3)
        self.TNotebook1.tab(0, text="Product Rank Data Plot", compound="left", underline="-1", )
        self.TNotebook1_t1.configure(background="#ffe5b4")
        self.TNotebook1_t1.configure(highlightbackground="#d9d9d9")
        self.TNotebook1_t1.configure(highlightcolor="black")

        self.TNotebook1_t0 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t0, padding=3)
        self.TNotebook1.tab(1, text="Revenue Data Plot", compound="left"
                            , underline="-1", )
        self.TNotebook1_t0.configure(background="#ffe5b4")
        self.TNotebook1_t0.configure(highlightbackground="#d9d9d9")
        self.TNotebook1_t0.configure(highlightcolor="black")

        self.TNotebook1_t2 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t2, padding=3)
        self.TNotebook1.tab(2, text="Clear Database", compound="left"
                            , underline="-1", )
        self.TNotebook1_t2.configure(background="#ffe5b4")
        self.TNotebook1_t2.configure(highlightbackground="#d9d9d9")
        self.TNotebook1_t2.configure(highlightcolor="black")

        ##implement the actual buttons meant to be shown on both of the windows itself.
        self.Button4 = tk.Button(self.TNotebook1_t1)
        self.Button4.place(relx=0.452, rely=0.063, height=20, width=80)
        self.Button4.configure(activebackground="#ececec")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#d9d9d9")
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''Plot the data''', command=self.doit)

        self.mytablearea = tk.Frame(self.TNotebook1_t1)
        self.mytablearea.place(relx=0.04, rely=0.188, height=371, width=1000)

        self.mytablearea2 = tk.Frame(self.TNotebook1_t0)
        self.mytablearea2.place(relx=0.04, rely=0.188, height=371, width=1000)

        self.Button40 = tk.Button(self.TNotebook1_t0)
        self.Button40.place(relx=0.452, rely=0.063, height=20, width=80)
        self.Button40.configure(activebackground="#ececec")
        self.Button40.configure(activeforeground="#000000")
        self.Button40.configure(background="#d9d9d9")
        self.Button40.configure(disabledforeground="#a3a3a3")
        self.Button40.configure(foreground="#000000")
        self.Button40.configure(highlightbackground="#d9d9d9")
        self.Button40.configure(highlightcolor="black")
        self.Button40.configure(pady="0")
        self.Button40.configure(text='''Plot the data''', command=self.doit2)

        self.Button42 = tk.Button(self.TNotebook1_t2)
        self.Button42.place(relx=0.41, rely=0.372, height=200, width=200)
        self.Button42.configure(activebackground="#ececec")
        self.Button42.configure(activeforeground="#000000")
        self.Button42.configure(background="#d9d9d9")
        self.Button42.configure(disabledforeground="#a3a3a3")
        self.Button42.configure(foreground="#000000")
        self.Button42.configure(highlightbackground="#d9d9d9")
        self.Button42.configure(highlightcolor="black")
        self.Button42.configure(pady="0")
        self.Button42.configure(text='''Clear Data''', command=self.doit3)
        self.Button42["state"] = DISABLED

    def doit(self):
        try:
            mydatabaseobj = pymysql.connect(host="localhost", user="root", password="",
                                            db="office")
            try:

                with mydatabaseobj.cursor() as myconn:
                    myconn.execute("select prod_names,rank from prodrank")
                    myresultdata = myconn.fetchall()
                    self.list_labels1=[]
                    self.list_data1=[]
                    for row in myresultdata:
                        self.list_labels1.append(str(row[0]))
                        self.list_data1.append(int(row[1]))

                    self.f=Figure(figsize=(5,5),dpi=100)
                    self.a=self.f.add_subplot(111)
                    k=range(len(self.list_labels1))
                    self.a.bar(self.list_labels1,self.list_data1,width=0.4)


                    self.canvas=FigureCanvasTkAgg(self.f,self.mytablearea)
                    self.canvas.draw()
                    self.canvas.get_tk_widget().pack(expand=True)

                    if myresultdata == None:
                        messagebox.showerror("Products are yet to be sold in this month")

            except Exception as ex:
                messagebox.showerror("Error Occured", "Error in fetching due to " + str(ex))
            finally:
                mydatabaseobj.close()
        except Exception as ex:
            messagebox.showerror("Error Occured", "Error creating database due to " + str(ex))


    def doit2(self):
        try:
            mydatabaseobj = pymysql.connect(host="localhost", user="root", password="",
                                            db="office")
            try:

                with mydatabaseobj.cursor() as myconn:
                    myconn.execute("select day,sum(revenue) from ordertable group by day")
                    myresultdata = myconn.fetchall()
                    self.list_labels2=[]
                    self.list_data2=[]

                    if myresultdata == None:
                        messagebox.showerror("No Revenue Generated Yet in this month")
                    else:
                        for row in myresultdata:
                            self.list_labels2.append(str(row[0]))
                            self.list_data2.append(int(row[1]))

                        self.f2=Figure(figsize=(5,5),dpi=100)
                        self.a2=self.f2.add_subplot(111)
                        self.a2.bar(self.list_labels2,self.list_data2,width=0.1)


                        self.canvas2=FigureCanvasTkAgg(self.f2,self.mytablearea2)
                        self.canvas2.draw()
                        self.canvas2.get_tk_widget().pack(expand=True)

            except Exception as ex:
                messagebox.showerror("Error Occured", "Error in fetching due to " + str(ex))
            finally:
                mydatabaseobj.close()
        except Exception as ex:
            messagebox.showerror("Error Occured", "Error creating database due to " + str(ex))

    def doit3(self):
        try:
            mydatabaseobj = pymysql.connect(host="localhost", user="root", password="",
                                            db="office")
            try:

                with mydatabaseobj.cursor() as myconn:
                    myconn.execute("DELETE FROM prodrank")
                    myconn.execute("DELETE FROM ordertable")
                    myconn.execute("DELETE FROM attendtable")
            except Exception as ex:
                messagebox.showerror("Error Occured", "Error in executing delete commands due to " + str(ex))
            finally:
                mydatabaseobj.close()
        except Exception as ex:
            messagebox.showerror("Error Occured", "Error in connecting to the database " + str(ex))


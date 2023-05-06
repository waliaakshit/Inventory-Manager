import traceback
from tkinter import *
from tkinter import ttk, messagebox
from tkinter.messagebox import askquestion
from random import seed
from random import randint
from random import choice
from datetime import date
from datetime import datetime
import smtplib

import pymysql as pymysql
import tkinter as tk

class AddQuote:
    def __init__(self, myframe):
        self.estimated_time = 0
        self.estimated_price = 0
        self.curr_price = 0
        self.curr_time = 0
        self.identifier = None
        self.mytop = Toplevel(myframe)
        self.mytop.geometry("1130x560+213+128")
        self.mytop.title("Bill generator")
        self.mytop.configure(background="#ffe5b4")
        self.mytop.configure(highlightbackground="#d9d9d9")
        self.mytop.configure(highlightcolor="black")

        self.Frame1 = tk.Frame(self.mytop)
        self.Frame1.place(relx=0.011, rely=0.013, relheight=0.991
                          , relwidth=0.991)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#ffe5b4")

        self.TNotebook1 = ttk.Notebook(self.Frame1)
        self.TNotebook1.place(relx=0.011, rely=0.019, relheight=0.971, relwidth=0.983)
        self.TNotebook1.configure(width=884)
        self.TNotebook1.configure(takefocus="")
        self.TNotebook1_t1 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t1, padding=3)
        self.TNotebook1.tab(0, text="Bill generation", compound="left", underline="-1",)
        self.TNotebook1_t1.configure(background="#ffe5b4")
        self.TNotebook1_t1.configure(highlightbackground="#d9d9d9")
        self.TNotebook1_t1.configure(highlightcolor="black")
        self.TNotebook1_t2 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t2, padding=3)
        self.TNotebook1.tab(1, text="Bill Cancellation", compound="left", underline="-1",)
        self.TNotebook1_t2.configure(background="#ffe5b4")
        self.TNotebook1_t2.configure(highlightbackground="#d9d9d9")
        self.TNotebook1_t2.configure(highlightcolor="black")

        self.Label1 = tk.Label(self.TNotebook1_t1)
        self.Label1.place(relx=0.015, rely=0.059, height=40, width=179)
        self.Label1.configure(background="#ffe5b4")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Customer Name''')


        self.Entry1 = tk.Entry(self.TNotebook1_t1)
        self.Entry1.place(relx=0.16, rely=0.059, height=36, relwidth=0.262)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")

        self.Button1 = tk.Button(self.TNotebook1_t1)
        self.Button1.place(relx=0.443, rely=0.059, height=42, width=168)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Search''', command=self.searchinfo)

        self.Label2 = tk.Label(self.TNotebook1_t1)
        self.Label2.place(relx=0.015, rely=0.176, height=40, width=179)
        self.Label2.configure(background="#ffe5b4")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Email ID''')


        self.Entry2 = tk.Entry(self.TNotebook1_t1)
        self.Entry2.place(relx=0.16, rely=0.191, height=36, relwidth=0.409)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")

        self.TSeparator1 = ttk.Separator(self.TNotebook1_t1)
        self.TSeparator1.place(relx=0.007, rely=0.279, relwidth=0.983)

        self.Button2 = tk.Button(self.TNotebook1_t1)
        self.Button2.place(relx=0.636, rely=0.059, height=82, width=148)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Random''', command=self.genrantime)

        self.Label3 = tk.Label(self.TNotebook1_t1)
        self.Label3.place(relx=0.022, rely=0.353, height=41, width=176)
        self.Label3.configure(background="#ffe5b4")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''Quantity''')

        self.Entry3 = tk.Entry(self.TNotebook1_t1)
        self.Entry3.place(relx=0.163, rely=0.353, height=46, relwidth=0.106)
        self.Entry3.configure(background="white")
        self.Entry3.configure(disabledforeground="#a3a3a3")
        self.Entry3.configure(font="TkFixedFont")
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(insertbackground="black")

        self.Label4 = tk.Label(self.TNotebook1_t1)
        self.Label4.place(relx=0.296, rely=0.353, height=51, width=187)
        self.Label4.configure(background="#ffe5b4")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='''Name''')

        self.Entry4 = tk.Entry(self.TNotebook1_t1)
        self.Entry4.place(relx=0.45, rely=0.353, height=46, relwidth=0.18)
        self.Entry4.configure(background="white")
        self.Entry4.configure(disabledforeground="#a3a3a3")
        self.Entry4.configure(font="TkFixedFont")
        self.Entry4.configure(foreground="#000000")
        self.Entry4.configure(insertbackground="black")

        self.Entry4.bind("<Return>", self.iftheprodexists)

        #here apply the key binding to check if the record even exists or not

        self.Button3 = tk.Button(self.TNotebook1_t1)
        self.Button3.place(relx=0.658, rely=0.338, height=50, width=308)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Add To Order''', command=self.makeorder)

        self.Text1 = tk.Text(self.TNotebook1_t1)
        self.Text1.place(relx=0.022, rely=0.471, relheight=0.491, relwidth=0.705)

        self.Text1.configure(background="white")
        self.Text1.configure(font="TkTextFont")
        self.Text1.configure(foreground="black")
        self.Text1.configure(highlightbackground="#d9d9d9")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(selectbackground="blue")
        self.Text1.configure(selectforeground="white")
        self.Text1.configure(wrap="word")

        self.Button4 = tk.Button(self.TNotebook1_t1)
        self.Button4.place(relx=0.776, rely=0.5, height=122, width=248)
        self.Button4.configure(activebackground="#ececec")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#d9d9d9")
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''Save in Database''', command=self.saveordertable)

        self.Button5 = tk.Button(self.TNotebook1_t1)
        self.Button5.place(relx=0.776, rely=0.765, height=122, width=248)
        self.Button5.configure(activebackground="#ececec")
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(background="#d9d9d9")
        self.Button5.configure(disabledforeground="#a3a3a3")
        self.Button5.configure(foreground="#000000")
        self.Button5.configure(highlightbackground="#d9d9d9")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(pady="0")
        self.Button5.configure(text='''Send Email''', command=self.sendemailto)

        self.Label1 = tk.Label(self.TNotebook1_t2)
        self.Label1.place(relx=0.015, rely=0.059, height=40, width=179)
        self.Label1.configure(background="#ffe5b4")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Random Number''')

        self.Entry11 = tk.Entry(self.TNotebook1_t2)
        self.Entry11.place(relx=0.16, rely=0.059, height=36, relwidth=0.262)
        self.Entry11.configure(background="white")
        self.Entry11.configure(disabledforeground="#a3a3a3")
        self.Entry11.configure(font="TkFixedFont")
        self.Entry11.configure(foreground="#000000")
        self.Entry11.configure(insertbackground="black")

        self.Button11 = tk.Button(self.TNotebook1_t2)
        self.Button11.place(relx=0.443, rely=0.059, height=42, width=168)
        self.Button11.configure(activebackground="#ececec")
        self.Button11.configure(activeforeground="#000000")
        self.Button11.configure(background="#d9d9d9")
        self.Button11.configure(disabledforeground="#a3a3a3")
        self.Button11.configure(foreground="#000000")
        self.Button11.configure(highlightbackground="#d9d9d9")
        self.Button11.configure(highlightcolor="black")
        self.Button11.configure(pady="0")
        self.Button11.configure(text='''Del Order''', command=self.deelorder)

        self.Label21 = tk.Label(self.TNotebook1_t2)
        self.Label21.place(relx=0.015, rely=0.176, height=40, width=179)
        self.Label21.configure(background="#ffe5b4")
        self.Label21.configure(disabledforeground="#a3a3a3")
        self.Label21.configure(foreground="#000000")
        self.Label21.configure(text='''Timestamp''')

        self.Entry21 = tk.Entry(self.TNotebook1_t2)
        self.Entry21.place(relx=0.16, rely=0.191, height=36, relwidth=0.409)
        self.Entry21.configure(background="white")
        self.Entry21.configure(disabledforeground="#a3a3a3")
        self.Entry21.configure(font="TkFixedFont")
        self.Entry21.configure(foreground="#000000")
        self.Entry21.configure(insertbackground="black")

    def genrantime(self):
        list_seeds = [1, 2, 3, 4, 5, 6, 7]
        random_choice = choice(list_seeds)
        seed(random_choice)
        self.random_quant = randint(0, 100)
        self.today=date.today()
        now = datetime.now()
        current_time = now.strftime("%H_%M_%S")
        self.time_ent_table = str(self.today.year) + "_" + str(self.today.month) + "_" + str(self.today.day) + "_" + current_time
        self.timestamp = "timestamp identifier :: " + self.time_ent_table
        self.Text1.delete('1.0', END)
        self.identifier = "random identifier :: " + str(self.random_quant) + "\n" + self.timestamp
        self.Text1.insert('1.0', self.identifier)
        self.Button2["state"] = DISABLED

    def searchinfo(self):
        try:
            mydatabaseobj = pymysql.connect(host="localhost", user="root", password="",
                                            db="office")
            try:

                with mydatabaseobj.cursor() as myconn:
                    myconn.execute("select * from phonebook where custname=%s", (self.Entry1.get()))
                    myresultdata = myconn.fetchone()
                    if myresultdata is not None:
                        self.Entry2.insert(0,myresultdata[1])
                    else:
                        messagebox.showerror("No Records Found", "No Customer records were added yet.")
                    self.Text1.delete('1.0', END)

            except Exception as ex:
                messagebox.showerror("Error Occured", "Error in fetching due to " + str(ex))
            finally:
                mydatabaseobj.close()
        except Exception as ex:
            messagebox.showerror("Error Occured", "Error creating database due to " + str(ex))

    def sendemailto(self):
        #official email address to be used to represent the store in the market
        self.sender_address = "bbenditlikepythontutorial9@gmail.com"
        self.receiver_address = self.Entry2.get()
        self.sender_password = "python234"
        mail_contnts = "Subject:Order placement" + "\n" + "\n" + self.Text1.get('1.0', END)
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(self.sender_address, self.sender_password)
        server.sendmail(self.sender_address, self.receiver_address, mail_contnts)
        self.Entry1.delete(0, END)
        self.Entry2.delete(0, END)
        server.quit()

    def saveordertable(self):
        try:
            mydatabaseobj = pymysql.connect(host="localhost", user="root", password="",
                                            db="office")
            try:

                with mydatabaseobj.cursor() as myconn:
                    myconn.execute("insert into ordertable(ordernumber,timestamp,day,revenue,estime) values(%s,%s,%s,%s,%s)", (self.random_quant,str(self.time_ent_table),int(self.today.day),self.estimated_price,self.estimated_time))

                    mydatabaseobj.commit()
                    messagebox.showinfo("Success", "Order Saved Successfully", parent=self.TNotebook1_t1)
                    old_da=self.Text1.get("1.0",END)
                    stringg = "Time to deliver:: " + str(self.estimated_time) + "\n" + "Total Price:: " + str(self.estimated_price) + "\n"
                    self.Text1.delete('1.0', END)
                    self.Text1.insert('1.0', old_da + stringg)
                    self.estimated_time=0
                    self.estimated_price=0

            except Exception as ex:
                messagebox.showerror("Error Occured", "Error in connecting due to " + str(ex))
            finally:
                mydatabaseobj.close()
        except Exception as ex:
            messagebox.showerror("Error Occured", "Error creating database due to " + str(ex))

    def deelorder(self):
        answer = askquestion("Confirm", "Do you really want to delete?", icon="warning")

        if answer == "yes":
            try:
                mydatabaseobj = pymysql.connect(host="localhost", user="root", password="",
                                                db="office")
                try:

                    with mydatabaseobj.cursor() as myconn:
                        myconn.execute(
                            "delete from ordertable where timestamp=%s",
                            (self.Entry21.get()))
                        mydatabaseobj.commit()
                        messagebox.showinfo("Success", "Order Deleted Successfully", parent=self.TNotebook1_t2)
                except Exception as ex:
                    messagebox.showerror("Error Occured", "Error in insert query due to " + str(ex))

                finally:
                    mydatabaseobj.close()

                self.Entry11.delete(0,END)
                self.Entry21.delete(0,END)

            except Exception as ex:
                messagebox.showerror("Error Occured", "Error creating database due to " + str(ex))

    def makeorder(self):

        #we have to make changes to the attributes of the order table also at this very instant of time.

        self.estimated_time += self.curr_time
        self.estimated_price += self.curr_price*int(self.Entry3.get())
        string = "quantity:: "+self.Entry3.get() + " X " + "Product Name:: " + self.Entry4.get() + "price:: " + str(self.curr_price*int(self.Entry3.get())) + "\n"
        old_data = self.Text1.get('1.0', END)
        self.Text1.delete('1.0', END)
        self.Text1.insert('1.0', old_data + string )
        self.Entry3.delete(0, END)
        self.Entry4.delete(0, END)
        self.curr_time = 0
        self.curr_price = 0

    def iftheprodexists(self,ev):
        try:
            mydatabaseobj = pymysql.connect(host="localhost", user="root", password="",
                                            db="office")
            try:

                with mydatabaseobj.cursor() as myconn:
                    myconn.execute("select * from producttable where name=%s", (self.Entry4.get()))
                    myresultdata = myconn.fetchone()
                    if myresultdata is None:
                        messagebox.showerror("error","No Products Found")
                        self.Entry4.delete(0,END)
                        self.Entry3.delete(0,END)
                    else:
                        #we have to considered that the product exists in the data base

                        myconn.execute("select * from prodrank where prod_names=%s", (self.Entry4.get()))
                        myresultdata2=myconn.fetchone()
                        if myresultdata2 is None:
                            myconn.execute("insert into prodrank(prod_names,rank) "
                            "values(%s,%s)", (self.Entry4.get(),self.Entry3.get()))
                            mydatabaseobj.commit()
                        else:
                            old_rank=int(myresultdata2[1])
                            new_rank=old_rank + int(self.Entry3.get())
                            myconn.execute("update prodrank set rank=%s where prod_names=%s", (new_rank,myresultdata[0]))
                            mydatabaseobj.commit()
                        #add the information into the prodrank table

                        self.curr_price = int(myresultdata[1])
                        self.curr_time = int(myresultdata[3])



            except Exception as ex:
                messagebox.showerror("Error Occured", "Error in fetching due to " + str(ex))
            finally:
                mydatabaseobj.close()
        except Exception as ex:
            messagebox.showerror("Error Occured", "Error creating database due to " + str(ex))

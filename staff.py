import time
import traceback
from tkinter import *
from tkinter import ttk, messagebox
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import askquestion

import pymysql as pymysql
import tkinter as tk

from PIL import ImageTk
from datetime import date
from tkcalendar import DateEntry



class AddStaff:

    def __init__(self, myframe):
        self.mytop = Toplevel(myframe)
        self.mytop.geometry("1130x560+213+128")
        self.mytop.title("Staff")
        self.mytop.configure(background="#ffe5b4")
        self.mytop.configure(highlightbackground="#d9d9d9")
        self.mytop.configure(highlightcolor="black")

        self.Frame1 = tk.Frame(self.mytop)
        self.Frame1.place(relx=0.006, rely=0.013, relheight=0.964
                          , relwidth=0.991)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#ffe5b4")


        self.TNotebook1 = ttk.Notebook(self.Frame1)
        self.TNotebook1.place(relx=0.006, rely=0.014, relheight=0.973
                              , relwidth=0.986)
        self.TNotebook1.configure(takefocus="")
        self.TNotebook1_t1 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t1, padding=3)
        self.TNotebook1.tab(0, text="Hiring Information", compound="left", underline="-1", )
        self.TNotebook1_t1.configure(background="#ffe5b4")
        self.TNotebook1_t1.configure(highlightbackground="#d9d9d9")
        self.TNotebook1_t1.configure(highlightcolor="black")
        self.TNotebook1_t2 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t2, padding=3)
        self.TNotebook1.tab(1, text="Search and Update", compound="left", underline="-1", )
        self.TNotebook1_t2.configure(background="#ffe5b4")
        self.TNotebook1_t2.configure(highlightbackground="#d9d9d9")
        self.TNotebook1_t2.configure(highlightcolor="black")

        self.Label1 = tk.Label(self.TNotebook1_t1)
        self.Label1.place(relx=0.416, rely=0.015, height=60, width=155)
        self.Label1.configure(background="#ffe5b4")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Starting Date''')

        self.Label2 = tk.Label(self.TNotebook1_t1)
        self.Label2.place(relx=0.013, rely=0.152, height=41, width=159)
        self.Label2.configure(background="#ffe5b4")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''First name''')

        self.Label3 = tk.Label(self.TNotebook1_t1)
        self.Label3.place(relx=0.409, rely=0.152, height=41, width=168)
        self.Label3.configure(background="#ffe5b4")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''Last Name''')

        self.Label4 = tk.Label(self.TNotebook1_t1)
        self.Label4.place(relx=0.013, rely=0.242, height=41, width=166)
        self.Label4.configure(background="#ffe5b4")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='''Qualfication''')

        self.Label5 = tk.Label(self.TNotebook1_t1)
        self.Label5.place(relx=0.013, rely=0.333, height=41, width=169)
        self.Label5.configure(background="#ffe5b4")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(text='''Email Address''')

        self.Label6 = tk.Label(self.TNotebook1_t1)
        self.Label6.place(relx=0.013, rely=0.424, height=41, width=169)
        self.Label6.configure(background="#ffe5b4")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(text='''DOB''')

        ##this is just going to be used along the DOB column
        self.dt = DateEntry(self.TNotebook1_t1, foreground='white', borderwidth=2)
        self.dt.place(relx=0.136, rely=0.424, relheight=0.062, relwidth=0.151)


        ##this is the DOB too but used in the second page
        self.Label62 = tk.Label(self.TNotebook1_t2)
        self.Label62.place(relx=0.013, rely=0.424, height=41, width=169)
        self.Label62.configure(background="#ffe5b4")
        self.Label62.configure(disabledforeground="#a3a3a3")
        self.Label62.configure(foreground="#000000")
        self.Label62.configure(text='''DOB''')

        self.dob = DateEntry(self.TNotebook1_t2, foreground='white', borderwidth=2)
        self.dob.place(relx=0.136, rely=0.424, relheight=0.062, relwidth=0.151)

        ## dt is basicaly going to be used for the case scenario of the input condition
        ## dob is used for updation and modification of the records itself. hence this is the solution

        self.Label8 = tk.Label(self.TNotebook1_t1)
        self.Label8.place(relx=0.013, rely=0.606, height=41, width=169)
        self.Label8.configure(background="#ffe5b4")
        self.Label8.configure(disabledforeground="#a3a3a3")
        self.Label8.configure(foreground="#000000")
        self.Label8.configure(text='''Phone Number''')

        self.Label9 = tk.Label(self.TNotebook1_t1)
        self.Label9.place(relx=0.013, rely=0.697, height=41, width=169)
        self.Label9.configure(background="#ffe5b4")
        self.Label9.configure(disabledforeground="#a3a3a3")
        self.Label9.configure(foreground="#000000")
        self.Label9.configure(text='''Landline Number''')

        self.Label10 = tk.Label(self.TNotebook1_t1)
        self.Label10.place(relx=0.012, rely=0.773, height=41, width=170)
        self.Label10.configure(background="#ffe5b4")
        self.Label10.configure(disabledforeground="#a3a3a3")
        self.Label10.configure(foreground="#000000")
        self.Label10.configure(text='''Address''')

        self.Label16 = tk.Label(self.TNotebook1_t1)
        self.Label16.place(relx=0.012, rely=0.900, height=41, width=170)
        self.Label16.configure(background="#ffe5b4")
        self.Label16.configure(disabledforeground="#a3a3a3")
        self.Label16.configure(foreground="#000000")
        self.Label16.configure(text='''Salary''')

        self.Button1 = tk.Button(self.TNotebook1_t1)
        self.Button1.place(relx=0.306, rely=0.900, height=24, width=55)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Save''', command=self.saveinfo)

        self.Button2 = tk.Button(self.TNotebook1_t1)
        self.Button2.place(relx=0.823, rely=0.515, height=24, width=55)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Upload''',command=self.uploadimage)

        
        self.today = date.today()
        v = StringVar(self.TNotebook1_t1, value=self.today)
        self.Entry1 = tk.Entry(self.TNotebook1_t1)
        self.Entry1.place(relx=0.532, rely=0.045, height=36, relwidth=0.132)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(text=self.today)
        self.Entry1.configure(textvariable=v)

        self.Label12 = tk.Label(self.TNotebook1_t2)
        self.Label12.place(relx=0.416, rely=0.015, height=60, width=155)
        self.Label12.configure(background="#ffe5b4")
        self.Label12.configure(disabledforeground="#a3a3a3")
        self.Label12.configure(foreground="#000000")
        self.Label12.configure(text='''Starting Date''')

        u=StringVar(self.TNotebook1_t2, value=self.today)
        self.Entry12 = tk.Entry(self.TNotebook1_t2)
        self.Entry12.place(relx=0.532, rely=0.045, height=36, relwidth=0.132)
        self.Entry12.configure(background="white")
        self.Entry12.configure(disabledforeground="#a3a3a3")
        self.Entry12.configure(font="TkFixedFont")
        self.Entry12.configure(foreground="#000000")
        self.Entry12.configure(insertbackground="black")
        self.Entry12.configure(text=self.today)
        self.Entry12.configure(textvariable=u)

        self.Entry2 = tk.Entry(self.TNotebook1_t1)
        self.Entry2.place(relx=0.136, rely=0.242, height=36, relwidth=0.529)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")

        self.Entry3 = tk.Entry(self.TNotebook1_t1)
        self.Entry3.place(relx=0.136, rely=0.333, height=36, relwidth=0.529)
        self.Entry3.configure(background="white")
        self.Entry3.configure(disabledforeground="#a3a3a3")
        self.Entry3.configure(font="TkFixedFont")
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(insertbackground="black")

        self.Label11 = tk.Label(self.TNotebook1_t1)
        self.Label11.place(relx=0.409, rely=0.455, height=41, width=165)
        self.Label11.configure(background="#ffe5b4")
        self.Label11.configure(disabledforeground="#a3a3a3")
        self.Label11.configure(foreground="#000000")
        self.Label11.configure(text='''Gender''')

        self.gender=StringVar()
        self.Radiobutton1 = tk.Radiobutton(self.TNotebook1_t1)
        self.Radiobutton1.place(relx=0.539, rely=0.455, relheight=0.056
                                , relwidth=0.069)
        self.Radiobutton1.configure(activebackground="#ececec")
        self.Radiobutton1.configure(activeforeground="#000000")
        self.Radiobutton1.configure(background="#ffe5b4")
        self.Radiobutton1.configure(disabledforeground="#a3a3a3")
        self.Radiobutton1.configure(foreground="#000000")
        self.Radiobutton1.configure(highlightbackground="#d9d9d9")
        self.Radiobutton1.configure(highlightcolor="black")
        self.Radiobutton1.configure(justify='left')
        self.Radiobutton1.configure(text='''Male''',takefocus="")
        self.Radiobutton1.configure(value="Male", variable=self.gender)

        self.Radiobutton2 = tk.Radiobutton(self.TNotebook1_t1)
        self.Radiobutton2.place(relx=0.61, rely=0.455, relheight=0.056
                                , relwidth=0.069)
        self.Radiobutton2.configure(activebackground="#ececec")
        self.Radiobutton2.configure(activeforeground="#000000")
        self.Radiobutton2.configure(background="#ffe5b4")
        self.Radiobutton2.configure(disabledforeground="#a3a3a3")
        self.Radiobutton2.configure(foreground="#000000")
        self.Radiobutton2.configure(highlightbackground="#d9d9d9")
        self.Radiobutton2.configure(highlightcolor="black")
        self.Radiobutton2.configure(justify='left')
        self.Radiobutton2.configure(text='''Female''',takefocus="")
        self.Radiobutton2.configure(variable=self.gender,value="Female")

        self.Label13 = tk.Label(self.TNotebook1_t1)
        self.Label13.place(relx=0.409, rely=0.621, height=41, width=162)
        self.Label13.configure(background="#ffe5b4")
        self.Label13.configure(disabledforeground="#a3a3a3")
        self.Label13.configure(foreground="#000000")
        self.Label13.configure(text='''Blood Group''')

        self.Label14 = tk.Label(self.TNotebook1_t1)
        self.Label14.place(relx=0.409, rely=0.697, height=41, width=166)
        self.Label14.configure(background="#ffe5b4")
        self.Label14.configure(disabledforeground="#a3a3a3")
        self.Label14.configure(foreground="#000000")
        self.Label14.configure(text='''Religion''')

        self.Text1 = tk.Text(self.TNotebook1_t1)
        self.Text1.place(relx=0.136, rely=0.788, relheight=0.100, relwidth=0.561)

        self.Text1.configure(background="white")
        self.Text1.configure(font="TkTextFont")
        self.Text1.configure(foreground="black")
        self.Text1.configure(highlightbackground="#d9d9d9")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(selectbackground="blue")
        self.Text1.configure(selectforeground="white")
        self.Text1.configure(wrap="word")

        self.bg=StringVar()

        self.TCombobox3 = ttk.Combobox(self.TNotebook1_t1)
        self.TCombobox3.place(relx=0.532, rely=0.621, relheight=0.062
                              , relwidth=0.151)
        self.TCombobox3.configure(textvariable=self.bg, state='readonly')
        self.TCombobox3.set('Choose Blood Group')
        self.TCombobox3.configure(values=('A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-'))
        self.TCombobox3.configure(takefocus="")

        self.religion=StringVar()

        self.TCombobox4 = ttk.Combobox(self.TNotebook1_t1)
        self.TCombobox4.place(relx=0.532, rely=0.697, relheight=0.062
                              , relwidth=0.151)
        self.TCombobox4.configure(textvariable=self.religion, state='readonly')
        self.TCombobox4.set('Choose Religion')
        self.TCombobox4.configure(values=('Hindu', 'Sikh', 'Muslim', 'Christian', 'Other'))
        self.TCombobox4.configure(takefocus="")

        self.Entry4 = tk.Entry(self.TNotebook1_t1)
        self.Entry4.place(relx=0.136, rely=0.621, height=36, relwidth=0.158)
        self.Entry4.configure(background="white")
        self.Entry4.configure(disabledforeground="#a3a3a3")
        self.Entry4.configure(font="TkFixedFont")
        self.Entry4.configure(foreground="#000000")
        self.Entry4.configure(insertbackground="black")


        self.Entry5 = tk.Entry(self.TNotebook1_t1)
        self.Entry5.place(relx=0.136, rely=0.712, height=36, relwidth=0.158)
        self.Entry5.configure(background="white")
        self.Entry5.configure(disabledforeground="#a3a3a3")
        self.Entry5.configure(font="TkFixedFont")
        self.Entry5.configure(foreground="#000000")
        self.Entry5.configure(insertbackground="black")

        self.Entry6 = tk.Entry(self.TNotebook1_t1)
        self.Entry6.place(relx=0.136, rely=0.152, height=36, relwidth=0.145)
        self.Entry6.configure(background="white")
        self.Entry6.configure(disabledforeground="#a3a3a3")
        self.Entry6.configure(font="TkFixedFont")
        self.Entry6.configure(foreground="#000000")
        self.Entry6.configure(insertbackground="black")

        self.Entry7 = tk.Entry(self.TNotebook1_t1)
        self.Entry7.place(relx=0.532, rely=0.167, height=36, relwidth=0.132)
        self.Entry7.configure(background="white")
        self.Entry7.configure(disabledforeground="#a3a3a3")
        self.Entry7.configure(font="TkFixedFont")
        self.Entry7.configure(foreground="#000000")
        self.Entry7.configure(insertbackground="black")

        self.Label15 = tk.Label(self.TNotebook1_t2)
        self.Label15.place(relx=0.013, rely=0.061, height=31, width=166)
        self.Label15.configure(background="#ffe5b4")
        self.Label15.configure(disabledforeground="#a3a3a3")
        self.Label15.configure(foreground="#000000")
        self.Label15.configure(text='''Batch ID Number''')

        self.Label152 = tk.Label(self.TNotebook1_t2)
        self.Label152.place(relx=0.013, rely=0.061, height=31, width=166)
        self.Label152.configure(background="#ffe5b4")
        self.Label152.configure(disabledforeground="#a3a3a3")
        self.Label152.configure(foreground="#000000")
        self.Label152.configure(text='''Batch ID Number''')

        self.Entry8 = tk.Entry(self.TNotebook1_t2)
        self.Entry8.place(relx=0.136, rely=0.061, height=36, relwidth=0.068)
        self.Entry8.configure(background="white")
        self.Entry8.configure(disabledforeground="#a3a3a3")
        self.Entry8.configure(font="TkFixedFont")
        self.Entry8.configure(foreground="#000000")
        self.Entry8.configure(insertbackground="black")

        self.Entry9 = tk.Entry(self.TNotebook1_t1)
        self.Entry9.place(relx=0.136, rely=0.900, height=36, relwidth=0.145)
        self.Entry9.configure(background="white")
        self.Entry9.configure(disabledforeground="#a3a3a3")
        self.Entry9.configure(font="TkFixedFont")
        self.Entry9.configure(foreground="#000000")
        self.Entry9.configure(insertbackground="black")

        self.img = tk.Label(self.TNotebook1_t1)
        self.img.place(relx=0.753, rely=0.015, relheight=0.505
                           , relwidth=0.204)

        self.img1 = tk.Label(self.TNotebook1_t2)
        self.img1.place(relx=0.753, rely=0.015, relheight=0.505
                           , relwidth=0.204)

        self.filename = ImageTk.PhotoImage(file="images/default.png")

        self.img1.config(image=self.filename)

        self.filename1 = ImageTk.PhotoImage(file="images/default.png")

        self.img.config(image=self.filename1)




        self.Label22 = tk.Label(self.TNotebook1_t2)
        self.Label22.place(relx=0.013, rely=0.152, height=41, width=159)
        self.Label22.configure(background="#ffe5b4")
        self.Label22.configure(disabledforeground="#a3a3a3")
        self.Label22.configure(foreground="#000000")
        self.Label22.configure(text='''First name''')

        self.Label32 = tk.Label(self.TNotebook1_t2)
        self.Label32.place(relx=0.409, rely=0.152, height=41, width=168)
        self.Label32.configure(background="#ffe5b4")
        self.Label32.configure(disabledforeground="#a3a3a3")
        self.Label32.configure(foreground="#000000")
        self.Label32.configure(text='''Last Name''')

        self.Label42 = tk.Label(self.TNotebook1_t2)
        self.Label42.place(relx=0.013, rely=0.242, height=41, width=166)
        self.Label42.configure(background="#ffe5b4")
        self.Label42.configure(disabledforeground="#a3a3a3")
        self.Label42.configure(foreground="#000000")
        self.Label42.configure(text='''Qualfication''')

        self.Label52 = tk.Label(self.TNotebook1_t2)
        self.Label52.place(relx=0.013, rely=0.333, height=41, width=169)
        self.Label52.configure(background="#ffe5b4")
        self.Label52.configure(disabledforeground="#a3a3a3")
        self.Label52.configure(foreground="#000000")
        self.Label52.configure(text='''Email Address''')

        self.Label82 = tk.Label(self.TNotebook1_t2)
        self.Label82.place(relx=0.013, rely=0.606, height=41, width=169)
        self.Label82.configure(background="#ffe5b4")
        self.Label82.configure(disabledforeground="#a3a3a3")
        self.Label82.configure(foreground="#000000")
        self.Label82.configure(text='''Phone Number''')

        self.Label92 = tk.Label(self.TNotebook1_t2)
        self.Label92.place(relx=0.013, rely=0.697, height=41, width=169)
        self.Label92.configure(background="#ffe5b4")
        self.Label92.configure(disabledforeground="#a3a3a3")
        self.Label92.configure(foreground="#000000")
        self.Label92.configure(text='''Landline Number''')

        self.Label102 = tk.Label(self.TNotebook1_t2)
        self.Label102.place(relx=0.012, rely=0.773, height=41, width=170)
        self.Label102.configure(background="#ffe5b4")
        self.Label102.configure(disabledforeground="#a3a3a3")
        self.Label102.configure(foreground="#000000")
        self.Label102.configure(text='''Address''')

        self.Label162 = tk.Label(self.TNotebook1_t2)
        self.Label162.place(relx=0.012, rely=0.900, height=41, width=170)
        self.Label162.configure(background="#ffe5b4")
        self.Label162.configure(disabledforeground="#a3a3a3")
        self.Label162.configure(foreground="#000000")
        self.Label162.configure(text='''Salary''')


        self.Button3 = tk.Button(self.TNotebook1_t2)
        self.Button3.place(relx=0.366, rely=0.900, height=24, width=55)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Update''', command=self.updateinfo)

        #the following table is used to find the record in the database by using thr first name
        self.Button4 = tk.Button(self.TNotebook1_t2)
        self.Button4.place(relx=0.426, rely=0.900, height=24, width=55)
        self.Button4.configure(activebackground="#ececec")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#d9d9d9")
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''Search''', command=self.searchinfo)

        self.Button12 = tk.Button(self.TNotebook1_t2)
        self.Button12.place(relx=0.306, rely=0.900, height=24, width=55)
        self.Button12.configure(activebackground="#ececec")
        self.Button12.configure(activeforeground="#000000")
        self.Button12.configure(background="#d9d9d9")
        self.Button12.configure(disabledforeground="#a3a3a3")
        self.Button12.configure(foreground="#000000")
        self.Button12.configure(highlightbackground="#d9d9d9")
        self.Button12.configure(highlightcolor="black")
        self.Button12.configure(pady="0")
        self.Button12.configure(text='''Delete''', command=self.deleteinfo)

        self.Button22 = tk.Button(self.TNotebook1_t2)
        self.Button22.place(relx=0.823, rely=0.515, height=24, width=55)
        self.Button22.configure(activebackground="#ececec")
        self.Button22.configure(activeforeground="#000000")
        self.Button22.configure(background="#d9d9d9")
        self.Button22.configure(disabledforeground="#a3a3a3")
        self.Button22.configure(foreground="#000000")
        self.Button22.configure(highlightbackground="#d9d9d9")
        self.Button22.configure(highlightcolor="black")
        self.Button22.configure(pady="0")
        self.Button22.configure(text='''Upload''', command=self.uploadimage)

        self.Entry22 = tk.Entry(self.TNotebook1_t2)
        self.Entry22.place(relx=0.136, rely=0.242, height=36, relwidth=0.529)
        self.Entry22.configure(background="white")
        self.Entry22.configure(disabledforeground="#a3a3a3")
        self.Entry22.configure(font="TkFixedFont")
        self.Entry22.configure(foreground="#000000")
        self.Entry22.configure(insertbackground="black")

        self.Entry32 = tk.Entry(self.TNotebook1_t2)
        self.Entry32.place(relx=0.136, rely=0.333, height=36, relwidth=0.529)
        self.Entry32.configure(background="white")
        self.Entry32.configure(disabledforeground="#a3a3a3")
        self.Entry32.configure(font="TkFixedFont")
        self.Entry32.configure(foreground="#000000")
        self.Entry32.configure(insertbackground="black")

        self.Label112 = tk.Label(self.TNotebook1_t2)
        self.Label112.place(relx=0.409, rely=0.455, height=41, width=165)
        self.Label112.configure(background="#ffe5b4")
        self.Label112.configure(disabledforeground="#a3a3a3")
        self.Label112.configure(foreground="#000000")
        self.Label112.configure(text='''Gender''')

        self.gende = StringVar()
        self.Radiobutton12 = tk.Radiobutton(self.TNotebook1_t2)
        self.Radiobutton12.place(relx=0.539, rely=0.455, relheight=0.056
                                , relwidth=0.069)
        self.Radiobutton12.configure(activebackground="#ececec")
        self.Radiobutton12.configure(activeforeground="#000000")
        self.Radiobutton12.configure(background="#ffe5b4")
        self.Radiobutton12.configure(disabledforeground="#a3a3a3")
        self.Radiobutton12.configure(foreground="#000000")
        self.Radiobutton12.configure(highlightbackground="#d9d9d9")
        self.Radiobutton12.configure(highlightcolor="black")
        self.Radiobutton12.configure(justify='left')
        self.Radiobutton12.configure(text='''Male''', takefocus="")
        self.Radiobutton12.configure(value="Male", variable=self.gende)

        self.Radiobutton22 = tk.Radiobutton(self.TNotebook1_t2)
        self.Radiobutton22.place(relx=0.61, rely=0.455, relheight=0.056
                                , relwidth=0.069)
        self.Radiobutton22.configure(activebackground="#ececec")
        self.Radiobutton22.configure(activeforeground="#000000")
        self.Radiobutton22.configure(background="#ffe5b4")
        self.Radiobutton22.configure(disabledforeground="#a3a3a3")
        self.Radiobutton22.configure(foreground="#000000")
        self.Radiobutton22.configure(highlightbackground="#d9d9d9")
        self.Radiobutton22.configure(highlightcolor="black")
        self.Radiobutton22.configure(justify='left')
        self.Radiobutton22.configure(text='''Female''', takefocus="")
        self.Radiobutton22.configure(variable=self.gende, value="Female")

        self.Label132 = tk.Label(self.TNotebook1_t2)
        self.Label132.place(relx=0.409, rely=0.621, height=41, width=162)
        self.Label132.configure(background="#ffe5b4")
        self.Label132.configure(disabledforeground="#a3a3a3")
        self.Label132.configure(foreground="#000000")
        self.Label132.configure(text='''Blood Group''')

        self.Label142 = tk.Label(self.TNotebook1_t2)
        self.Label142.place(relx=0.409, rely=0.697, height=41, width=166)
        self.Label142.configure(background="#ffe5b4")
        self.Label142.configure(disabledforeground="#a3a3a3")
        self.Label142.configure(foreground="#000000")
        self.Label142.configure(text='''Religion''')

        self.Text12 = tk.Text(self.TNotebook1_t2)
        self.Text12.place(relx=0.136, rely=0.788, relheight=0.100, relwidth=0.561)

        self.Text12.configure(background="white")
        self.Text12.configure(font="TkTextFont")
        self.Text12.configure(foreground="black")
        self.Text12.configure(highlightbackground="#d9d9d9")
        self.Text12.configure(highlightcolor="black")
        self.Text12.configure(insertbackground="black")
        self.Text12.configure(selectbackground="blue")
        self.Text12.configure(selectforeground="white")
        self.Text12.configure(wrap="word")


        self.b = StringVar()

        self.TCombobox32 = ttk.Combobox(self.TNotebook1_t2)
        self.TCombobox32.place(relx=0.532, rely=0.621, relheight=0.062
                              , relwidth=0.151)
        self.TCombobox32.set('Choose Blood Group')
        self.TCombobox32.configure(textvariable=self.b, state='readonly')
        self.TCombobox32.configure(values=('A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-'))
        self.TCombobox32.configure(takefocus="")

        self.religio = StringVar()

        self.TCombobox42 = ttk.Combobox(self.TNotebook1_t2)
        self.TCombobox42.place(relx=0.532, rely=0.697, relheight=0.062
                              , relwidth=0.151)
        self.TCombobox42.configure(textvariable=self.religio, state='readonly')
        self.TCombobox42.set('Choose Religion')
        self.TCombobox42.configure(values=('Hindu', 'Sikh', 'Muslim', 'Christian', 'Other'))
        self.TCombobox42.configure(takefocus="")



        self.Entry42 = tk.Entry(self.TNotebook1_t2)
        self.Entry42.place(relx=0.136, rely=0.621, height=36, relwidth=0.158)
        self.Entry42.configure(background="white")
        self.Entry42.configure(disabledforeground="#a3a3a3")
        self.Entry42.configure(font="TkFixedFont")
        self.Entry42.configure(foreground="#000000")
        self.Entry42.configure(insertbackground="black")

        self.Entry52 = tk.Entry(self.TNotebook1_t2)
        self.Entry52.place(relx=0.136, rely=0.712, height=36, relwidth=0.158)
        self.Entry52.configure(background="white")
        self.Entry52.configure(disabledforeground="#a3a3a3")
        self.Entry52.configure(font="TkFixedFont")
        self.Entry52.configure(foreground="#000000")
        self.Entry52.configure(insertbackground="black")

        self.Entry62 = tk.Entry(self.TNotebook1_t2)
        self.Entry62.place(relx=0.136, rely=0.152, height=36, relwidth=0.145)
        self.Entry62.configure(background="white")
        self.Entry62.configure(disabledforeground="#a3a3a3")
        self.Entry62.configure(font="TkFixedFont")
        self.Entry62.configure(foreground="#000000")
        self.Entry62.configure(insertbackground="black")

        self.Entry72 = tk.Entry(self.TNotebook1_t2)
        self.Entry72.place(relx=0.532, rely=0.167, height=36, relwidth=0.132)
        self.Entry72.configure(background="white")
        self.Entry72.configure(disabledforeground="#a3a3a3")
        self.Entry72.configure(font="TkFixedFont")
        self.Entry72.configure(foreground="#000000")
        self.Entry72.configure(insertbackground="black")


        self.Entry92 = tk.Entry(self.TNotebook1_t2)
        self.Entry92.place(relx=0.136, rely=0.900, height=36, relwidth=0.145)
        self.Entry92.configure(background="white")
        self.Entry92.configure(disabledforeground="#a3a3a3")
        self.Entry92.configure(font="TkFixedFont")
        self.Entry92.configure(foreground="#000000")
        self.Entry92.configure(insertbackground="black")


        #started to work with the tree view configurations frm this very point
        mytablearea = Frame(self.TNotebook1_t2)
        scrollbarx = Scrollbar(mytablearea, orient=HORIZONTAL)
        scrollbary = Scrollbar(mytablearea, orient=VERTICAL)

        self.mytable = ttk.Treeview(mytablearea, columns=("sr_no", "fname", "phone"),
                                    xscrollcommand=scrollbarx.set, yscrollcommand=scrollbary.set)
        self.mytable['show'] = 'headings'

        #setting up the individual scrollbars to heed to its commands
        scrollbarx.config(command=self.mytable.xview)
        scrollbary.config(command=self.mytable.yview)

        scrollbarx.pack(side=BOTTOM, fill=X)
        scrollbary.pack(side=RIGHT, fill=Y)

        self.mytable.heading("sr_no", text="Sr No")
        self.mytable.heading("fname", text="Name")
        self.mytable.heading("phone", text="Phone")

        #defining the visualizations of the mytable area
        #the first column is basically called as the phantom column and we always have to devisualise it
        self.mytable.column('#0', stretch=NO, minwidth=0, width=0)
        self.mytable.column('#1', stretch=NO, minwidth=0, width=70)
        self.mytable.column('#2', stretch=NO, minwidth=0, width=70)
        self.mytable.column('#3', stretch=NO, minwidth=0, width=70)

        self.mytable.bind("<ButtonRelease-1>", self.fetchbysrno)
        self.mytable.pack()
        mytablearea.place(relx=0.720, rely=0.694, relheight=0.159, width=220)


    def searchinfo(self):
        try:
            mydatabaseobj = pymysql.connect(host="localhost", user="root", password="",
                                            db="office")
            try:

                with mydatabaseobj.cursor() as myconn:
                    myconn.execute("select sr_no, fname,phone from stafftable"
                                   " where fname like %s", (self.Entry62.get() + "%"))
                    myresultdata = myconn.fetchall()
                    self.mytable.delete(*self.mytable.get_children())
                    for row in myresultdata:
                        self.mytable.insert('', END, value=(row))

                    if myresultdata == None:
                        messagebox.showerror("No Records Found", "No Staff added yet.")

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
        self.batchdi = selectedRow[0]
        try:
            mydatabaseobj = pymysql.connect(host="localhost", user="root", password="",
                                            db="office")
            try:

                with mydatabaseobj.cursor() as myconn:
                    myconn.execute("select * from stafftable where sr_no=%s",
                                   (self.batchdi))
                    myresultdata = myconn.fetchall()

                    for row in myresultdata:

                        self.Entry8.delete(0, END)
                        self.Entry8.insert(0, self.batchdi)
                        self.Entry62.delete(0, END)
                        self.Entry62.insert(0, row[1])
                        self.Entry72.delete(0, END)
                        self.Entry72.insert(0, row[2])
                        self.Entry22.delete(0, END)
                        self.Entry22.insert(0, row[3])


                        self.Entry92.delete(0, END)
                        self.Entry92.insert(0, row[4])
                        self.Entry42.delete(0, END)
                        self.Entry42.insert(0, row[5])

                        self.Entry52.delete(0, END)
                        self.Entry52.insert(0, row[6])
                        self.dob.delete(0, END)
                        self.dob.insert(0, row[8])


                        self.Text12.delete('1.0', END)
                        self.Text12.insert('1.0', row[9])

                        #this is basically considered to be defined as the starting of the admission date
                        self.Entry12.delete(0, END)
                        self.Entry12.insert(0, row[12]) #instad of addt use entry1

                        self.filename4 = ImageTk.PhotoImage(file="images//" + row[10])

                        self.img1.config(image=self.filename4)

                        self.Entry32.delete(0,END)
                        self.Entry32.insert(0,row[14])

                        self.TCombobox42.set(row[11])
                        self.TCombobox32.set(row[13])

                        if row[7] == "Male":
                            self.gende.set("Male")
                        else:
                            self.gende.set("Female")

                    if myresultdata == None:
                        messagebox.showerror("No Records Found", "No Staff added yet.")

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
                        "update stafftable set fname=%s,lname=%s,qualf=%s,salary=%s,phone=%s,landline=%s,gender=%s,DOB=%s,address=%s,religion=%s,strtdate=%s,bg=%s,email=%s where sr_no=%s",
                        (self.Entry62.get(), self.Entry72.get(), self.Entry22.get(), self.Entry92.get(),
                         self.Entry42.get(),self.Entry52.get(), self.gende.get(),self.dob.get_date(),self.Text12.get('1.0',END),self.TCombobox42.get(),self.Entry12.get(),self.b.get(),self.Entry32.get() ,self.batchdi
                         ))
                    mydatabaseobj.commit()
                    messagebox.showinfo("Success", "Record Updated Successfully", parent=self.TNotebook1_t1)
            except Exception as ex:
                messagebox.showerror("Error Occured", "Error in insert query due to " + str(ex))
            finally:
                mydatabaseobj.close()
            self.gende.set(" ")

            self.Entry42.delete(0, END)
            self.Entry62.delete(0, END)
            self.Entry72.delete(0, END)

            self.religio.set("Choose Religion")
            self.b.set("Choose Blood Group")

            self.filename3 = ImageTk.PhotoImage(file="images/default.png")

            self.img1.config(image=self.filename3)

            self.Entry22.delete(0, END)
            self.Entry32.delete(0,END)
            self.Entry52.delete(0, END)
            self.Entry92.delete(0,END)
            self.Entry8.delete(0,END)

            self.mytable.delete(*self.mytable.get_children())
            self.Text12.delete('1.0', END)

            self.dob.delete(0, END)

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
                            "delete from stafftable where sr_no=%s",
                            (self.batchdi))
                        mydatabaseobj.commit()
                        messagebox.showinfo("Success", "Record Deleted Successfully", parent=self.TNotebook1_t1)
                except Exception as ex:
                    messagebox.showerror("Error Occured", "Error in insert query due to " + str(ex),
                                         )

                finally:
                    mydatabaseobj.close()

                self.gende.set(" ")
                self.gende.set(" ")

                self.Entry42.delete(0, END)
                self.Entry62.delete(0, END)
                self.Entry72.delete(0, END)

                self.religio.set("Choose Religion")
                self.b.set("Choose Blood Group")

                self.filename1 = ImageTk.PhotoImage(file="images/default.png")

                self.img1.config(image=self.filename1)

                self.Entry22.delete(0, END)
                self.Entry32.delete(0, END)
                self.Entry52.delete(0, END)
                self.Entry92.delete(0,END)
                self.Entry8.delete(0,END)

                self.mytable.delete(*self.mytable.get_children())
                self.Text12.delete('1.0', END)
                self.dob.delete(0, END)



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

    def saveinfo(self):

            try:
                mydatabaseobj = pymysql.connect(host="localhost", user="root", password="", db="office")
                try:
                    with mydatabaseobj.cursor() as myconn:
                        myconn.execute(
                        "insert into stafftable(fname,lname,qualf,salary,phone,landline,gender,DOB,address,image,religion,strtdate,bg,email) "
                        "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                        (self.Entry6.get(), self.Entry7.get(), self.Entry2.get(),
                          self.Entry9.get(),self.Entry4.get(),self.Entry5.get(), self.gender.get(),self.dt.get_date(),
                          self.Text1.get('1.0',END),self.myfinalname, self.TCombobox4.get(),self.Entry1.get(), self.TCombobox3.get(),self.Entry3.get()))

                        mydatabaseobj.commit()
                        messagebox.showinfo("Success", "Record Saved Successfully",parent=self.TNotebook1_t1)

                except Exception as ex:
                    messagebox.showerror("Error Occured","Please Fill All Blocks!",parent=self.TNotebook1_t1)
                finally:
                    mydatabaseobj.close()

                self.gender.set(" ")
                self.TCombobox3.set("Choose Blood Group")
                self.TCombobox4.set("Choose Religion")

                self.Entry2.delete(0, END)
                self.Entry3.delete(0,END)

                self.Entry3.delete(0, END)
                self.filename2 = ImageTk.PhotoImage(file="images/default.png")
                self.Entry6.delete(0,END)
                self.img.config(image=self.filename2)
                self.Entry4.delete(0, END)
                self.Entry7.delete(0,END)
                self.Entry5.delete(0, END)
                self.Entry9.delete(0,END)

                self.Text1.delete('1.0', END)
                self.dt.delete(0, END)


            except Exception as ex:
                messagebox.showerror("Error Occured", "Error creating database due to " + str(ex))
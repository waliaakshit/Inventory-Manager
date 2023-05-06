from tkinter import *
import tkinter as tk
from tkinter import ttk
import webbrowser
from PIL import Image, ImageTk

from staff import AddStaff
from misc import MiscClass
from quotation import AddQuote
from phonebook import AddPhone
from product import AddProduct
from changepass import ChangePass
from attendance import Att
from plot import PlotFrame
import login


class myparent:
    def __init__(self):
        self.mytop=Tk()
        self.mytop.geometry("%dx%d+%d+%d" % (self.mytop.winfo_screenwidth(), self.mytop.winfo_screenheight(), 0, 0))
        self.mytop.title("    MOBI RETAIL    ")
        self.mytop.configure(relief="groove")
        self.mytop.configure(background="#ffe5b4")

        self.Frame1 = tk.Frame(self.mytop)
        self.Frame1.place(relx=0.007, rely=0.014, relheight=0.979, relwidth=0.139)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#ffe5b4")
        self.Frame1.configure(width=190)




        self.Button3 = tk.Button(self.Frame1)
        self.Button3.place(relx=0.053, rely=0.246, height=45, width=167)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.student = PhotoImage(file="../MOBIretail/images/Chevron Right_32px.png")
        self.Button3.configure(relief="groove")
        self.Button3.configure(text="Staff Management",command=self.addstaffframe,image=self.student,compound=LEFT)
        self.Button3.configure(width=167)

        self.Button4 = tk.Button(self.Frame1)
        self.Button4.place(relx=0.053, rely=0.333, height=45, width=167)
        self.Button4.configure(activebackground="#ececec")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#d9d9d9")
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")

        self.Button4.configure(pady="0")

        self.staff = PhotoImage(file="../MOBIretail/images/Chevron Right_32px.png")
        self.Button4.configure(relief="groove")
        self.Button4.configure(text="Prod. Management", command=self.addproductframe, image=self.staff,compound=LEFT)
        self.Button4.configure(width=167)



        self.Button5 = tk.Button(self.Frame1)
        self.Button5.place(relx=0.053, rely=0.507, height=45, width=167)
        self.Button5.configure(activebackground="#ececec")
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(background="#d9d9d9")
        self.Button5.configure(disabledforeground="#a3a3a3")
        self.Button5.configure(foreground="#000000")
        self.Button5.configure(highlightbackground="#d9d9d9")
        self.Button5.configure(highlightcolor="black")

        self.fee = PhotoImage(file="../MOBIretail/images/Chevron Right_32px.png")
        self.Button5.configure(relief="groove")
        self.Button5.configure(text="Plot generation", command=self.plotframe, image=self.fee, compound=LEFT)
        self.Button5.configure(width=167)

        self.Button6 = tk.Button(self.Frame1)
        self.Button6.place(relx=0.053, rely=0.42, height=45, width=167)
        self.Button6.configure(activebackground="#ececec")
        self.Button6.configure(activeforeground="#000000")
        self.Button6.configure(background="#d9d9d9")
        self.Button6.configure(disabledforeground="#a3a3a3")
        self.Button6.configure(foreground="#000000")
        self.Button6.configure(highlightbackground="#d9d9d9")
        self.Button6.configure(highlightcolor="black")

        self.exam = PhotoImage(file="../MOBIretail/images/Chevron Right_32px.png")
        self.Button6.configure(relief="groove")
        self.Button6.configure(text="    Phonebook    ", command=self.phonoframe, image=self.exam, compound=LEFT)
        self.Button6.configure(width=167)

        self.Button7 = tk.Button(self.Frame1)
        self.Button7.place(relx=0.053, rely=0.681, height=45, width=167)
        self.Button7.configure(activebackground="#ececec")
        self.Button7.configure(activeforeground="#000000")
        self.Button7.configure(background="#d9d9d9")
        self.Button7.configure(disabledforeground="#a3a3a3")
        self.Button7.configure(foreground="#000000")
        self.Button7.configure(highlightbackground="#d9d9d9")
        self.Button7.configure(highlightcolor="black")

        self.misc = PhotoImage(file="../MOBIretail/images/Chevron Right_32px.png")
        self.Button7.configure(relief="groove")
        self.Button7.configure(text="Bill generate",command=self.addquoteframe,image=self.misc,compound=LEFT)
        self.Button7.configure(width=167)

        self.Button10 = tk.Button(self.Frame1)
        self.Button10.place(relx=0.053, rely=0.768, height=45, width=167)
        self.Button10.configure(activebackground="#ececec")
        self.Button10.configure(activeforeground="#000000")
        self.Button10.configure(background="#d9d9d9")
        self.Button10.configure(disabledforeground="#a3a3a3")
        self.Button10.configure(foreground="#000000")
        self.Button10.configure(highlightbackground="#d9d9d9")
        self.Button10.configure(highlightcolor="black")

        self.misc1 = PhotoImage(file="../MOBIretail/images/Chevron Right_32px.png")
        self.Button10.configure(relief="groove")
        self.Button10.configure(text="Miscellaneous", command=self.miscframe, image=self.misc1, compound=LEFT)
        self.Button10.configure(width=167)

        self.Button8=tk.Button(self.Frame1)
        self.Button8.place(relx=0.053, rely=0.594, height=45, width=167)
        self.att = PhotoImage(file="../MOBIretail/images/Chevron Right_32px.png")
        self.Button8.configure(relief="groove")
        self.Button8.configure(activebackground="#ececec")
        self.Button8.configure(activeforeground="#000000")
        self.Button8.configure(background="#d9d9d9")
        self.Button8.configure(disabledforeground="#a3a3a3")
        self.Button8.configure(foreground="#000000")
        self.Button8.configure(highlightbackground="#d9d9d9")
        self.Button8.configure(highlightcolor="black")
        self.Button8.configure(text="    Attendance    ", command=self.attframe, image=self.att, compound=LEFT)

        self.Frame2 = tk.Frame(self.mytop)
        self.Frame2.place(relx=0.161, rely=0.014, relheight=0.128
                          , relwidth=0.831)
        self.Frame2.configure(relief='groove')
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief="groove")
        self.Frame2.configure(background="#ffe5b4")
        self.Frame2.configure(width=1135)

        self.Button1 = tk.Button(self.Frame2)
        self.Button1.place(relx=0.925, rely=0.222, height=38, width=38)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")

        self.signout = PhotoImage(file="../MOBIretail/images/Sign Out_32px.png")

        self.Button1.configure(image=self.signout, command=self.logout)


        self.Button2 = tk.Button(self.Frame2)
        self.Button2.place(relx=0.811, rely=0.222, height=38, width=110)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(relief="groove")
        self.Button2.configure(text='''Change Password''')
        self.Button2.configure(width=110,command=self.changepass)

        self.Button9 = tk.Button(self.Frame2)
        self.Button9.place(relx=0.700, rely=0.222, height=38, width=110)
        self.Button9.configure(activebackground="#ececec")
        self.Button9.configure(activeforeground="#000000")
        self.Button9.configure(background="#d9d9d9")
        self.Button9.configure(disabledforeground="#a3a3a3")
        self.Button9.configure(foreground="#000000")
        self.Button9.configure(highlightbackground="#d9d9d9")
        self.Button9.configure(highlightcolor="black")
        self.Button9.configure(pady="0")
        self.Button9.configure(relief="groove")
        self.Button9.configure(text='''Latest News''')
        self.Button9.configure(width=110, command=self.gotowebsite)

        self.TSeparator2 = ttk.Separator(self.Frame2)
        self.TSeparator2.place(relx=0.018, rely=0.778, relwidth=0.449)

        self.Label1 = tk.Label(self.Frame2)
        self.Label1.place(relx=0.009, rely=0.222, height=41, width=517)
        self.Label1.configure(background="#ffe5b4")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(justify='left')
        self.Label1.configure(text='''    MOBI RETAIL    ''',font=('Arial Black','18','bold'))
        self.Label1.configure(width=517)

        self.TSeparator1 = ttk.Separator(self.mytop)
        self.TSeparator1.place(relx=0.154, rely=0.014, relheight=0.979)
        self.TSeparator1.configure(orient="vertical")

        self.menubar = tk.Menu(self.mytop, font="TkMenuFont")
        self.mytop.configure(menu=self.menubar)

    def addstaffframe(self):
        AddStaff(self.mytop)

    def miscframe(self):
        MiscClass(self.mytop)

    def addproductframe(self):
        AddProduct(self.mytop)

    def addquoteframe(self):
        AddQuote(self.mytop)

    def phonoframe(self):
        AddPhone(self.mytop)

    def logout(self):
        self.mytop.destroy()
        login.login()

    def changepass(self):
        ChangePass(self.mytop)

    def plotframe(self):
        PlotFrame(self.mytop)

    def attframe(self):
        Att(self.mytop)

    def gotowebsite(self):
        webbrowser.open("https://www.gsmarena.com/news.php3")


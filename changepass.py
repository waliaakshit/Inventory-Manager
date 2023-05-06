from tkinter import *
from tkinter import messagebox, ttk
import pymysql
import parent

class ChangePass:
    def __init__(self, myframe):
        self.root = Toplevel(myframe)
        self.root.title("Change Password")
        self.root.geometry("800x450+260+110")
        self.root.configure(background="#ffe5b4")
        lb4=Label(self.root, text="User Name")
        lb1=Label(self.root, text="Current Password")
        lb2=Label(self.root, text="New Password")
        lb3=Label(self.root, text="Confirm Password")

        self.unamebox = Entry(self.root)
        self.currentpassbox = Entry(self.root)
        self.unamebox.focus_set()
        self.newpassbox = Entry(self.root,show="*")
        self.confirmpassbox = Entry(self.root,show="*")
        create_btn=Button(self.root, text="Change Password", command=self.changepassword)
        self.root.resizable(0, 0)
        lb1.configure(background="#ffe5b4")
        lb2.configure(background="#ffe5b4")
        lb3.configure(background="#ffe5b4")
        lb4.configure(background="#ffe5b4")
        lb4.place(x=50,y=50)
        lb1.place(x=50,y=100)
        lb2.place(x=50,y=150)
        lb3.place(x=50,y=200)
        self.unamebox.place(x=200, y=50)
        self.currentpassbox.place(x=200,y=100)
        self.newpassbox.place(x=200,y=150)
        self.confirmpassbox.place(x=200,y=200)
        create_btn.place(x=200,y=250)


        self.root.mainloop()

    def changepassword(self):

        if self.newpassbox.get() == self.confirmpassbox.get():
            try:
                    myobj=pymysql.connect(host="localhost", user="root",
                                          password="", db="office")
                    try:
                        with myobj.cursor() as myconn:

                            affected_rows = myconn.execute("update usertable "
                                           "set pass=%s "
                                           "where uname=%s "
                                           "and pass=%s",
                                           (self.confirmpassbox.get(), self.unamebox.get(), self.currentpassbox.get()))


                            myobj.commit()
                            if affected_rows > 0:
                                messagebox.showinfo("Success", "Password updated Successfully", parent=self.root)


                            else:
                                messagebox.showwarning("Warning", "Old Password is wrong", parent=self.root)



                    except Exception as ex:
                            messagebox.showerror("Error Occured", "Error occured in Query due to " + str(ex))
                    finally:
                            myobj.close()
                            self.root.destroy()

            except Exception as ex:
                    messagebox.showerror("Error Occured", "Error occured in Connection due to " + str(ex))
        else:
            messagebox.showwarning("Warning", "Password does not match")
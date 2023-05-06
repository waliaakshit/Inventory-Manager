from tkinter import *
from time import sleep

import login

class splash:
    def __init__(self):
        self.mytop = Tk()
        self.mytop.configure(background="#000000")
        self.mytop.configure(highlightbackground="#d9d9d9")
        self.mytop.configure(highlightcolor="black")
        self.mytop.geometry("%dx%d+%d+%d" % (self.mytop.winfo_screenwidth(), self.mytop.winfo_screenheight(), 0, 0))
        self.mytop.title("INITIATING THE RETAIL PROGRAM...")
        Label(self.mytop,text="Loading...",font="Bahnschrift 15",bg="black",fg="#FFBD09").place(x=490,y=320)
        for i in range(16):
            Label(self.mytop,fg="#1F2732",width=2,height=1).place(x=(i+22)*22,y=350)
        self.mytop.update()
        self.play_animation()

        #self.mytop.after(5000, self.do_it)
        self.mytop.mainloop()

    def play_animation(self):
        for i in range(3):
            for j in range(16):
                Label(self.mytop,bg="#FFBD09",width=2,height=1).place(x=(j+22)*22,y=350)
                sleep(0.06)
                self.mytop.update_idletasks()

                #make the block dark
                Label(self.mytop, bg="#1F2732", width=2, height=1).place(x=(j + 22) * 22, y=350)
        else:
            self.mytop.destroy()
            login.login()
            exit()
    #def do_it(self):
    #    self.mytop.destroy()
    #    login.login()
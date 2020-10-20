from tkinter import *
import sys
w = Tk()
w.title("Gmail")

w.configure(bg = "white")
w.geometry("600x400")

def nextb():

    bn = Tk()
    bn.title("Gmail")
    bn.geometry("600x400")
    bn.configure(bg = "white")
    def exit():
        bn.destroy()
    asd = Label(bn, text="You have successfuly loged in to your gmail account", font = "callibri 15", bg = "white")
    asq = Label(bn, text="Click next to use your gmail account", font = "callibri 15", bg = "white")
    asq.grid(row=11, column=5, columnspan = 2)
    asd.grid(row=10, column=5)
    zx = Button(bn, text="Next", font="callibri 15", fg="white", bg="blue")
    zx.place(x=400, y=330)
    xc = Button(bn, text="Exit", font="callibri 15", fg="white", bg="blue", command=lambda:exit())
    xc.place(x=500, y=330)


def cancel():
    sys.exit()
def create_an_account():

    import sys
    ki = Tk()
    ki.title("Gmail")
    ki.configure(bg="white")
    ki.geometry("600x400")

    def cancels():
        ki.destroy()


    fr = Label(ki, text="Create an Account", font="callibri 40", fg="blue", bg="white")
    fr.grid(row=0, column=0)

    Label(ki, text="Account name:", font = "callibri", bg = "white") .place(x=10, y=70)
    Label(ki, text="Password:", font = "callibri", bg = "white") .place(x=10, y=100)
    Label(ki, text="Confirm Password:", font="callibri", bg = "white" ) .place(x=10, y=130)
    Entry(ki, width = 35, borderwidth = 5) .place(x=200, y=70)
    Entry(ki, width = 35, borderwidth = 5) .place(x=200, y=100)
    Entry(ki, width = 35, borderwidth = 5) .place(x=200, y=130)

    m = Button(ki, text="Cancel", font = "callibri 15", bg="white", fg="blue", command=cancels)
    m.place(x=470, y=330)
"""
asdf = PhotoImage(file="C://Users//sweet//Desktop//Python projects//Notification//gmail.png")
w.iconphoto(False, asdf)
"""
a = Label(w, text="Gmail", font = "callibri 40", fg = "red", bg = "white")
a.grid(row = 0, column = 0)

a = Label(w, text="Log-in", font = "callibri 30", fg = "red", bg = "white")
a.grid(row = 1, column = 0)


Label(w, text="Account name:", font = "callibri", bg = "white") .grid(row = 6, column = 20)
Label(w, text="Password:", font = "callibri", bg = "white") .grid(row = 9, column = 20)

g = Entry(w, width = 35, borderwidth = 5)
g.grid(row=6, column=21)

i = Entry(w, width = 35, borderwidth = 5)
i.grid(row=9, column=21)

v = Button(w, text="Create an account", font = "callibri 15", bg="blue", fg="white", command=create_an_account)
v.place(x=40, y=330)

m = Button(w, text="Next", font = "callibri 15", bg="blue", fg="white", command=nextb)
m.place(x=400, y=330)

m = Button(w, text="Cancel", font = "callibri 15", bg="white", fg="blue", command=cancel)
m.place(x=470, y=330)

c = Button(w, text="Forgot Password? Click Here", font = "callibri", fg = "blue", bg = "white", borderwidth = -1)
c.grid(row=10, column=21)




w.mainloop()

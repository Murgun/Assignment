import webbrowser as wb

from tkinter import *
obj = Tk(className="Search Engine")

e = Entry(obj, font=("Times new roman",25))
e.grid()

def Navigate():
    query = e.get()
    wb.open("https://www.hotstar.com/results?search_query="+query)

b = Button(obj, text="search", command= Navigate, font=("Times new roman",25))
b.grid()

b1 = Button(obj, text="close", command= obj.destroy, font=("Times new roman",25))
b1.grid()

obj.mainloop()
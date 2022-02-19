from calendar import c
from multiprocessing.sharedctypes import Value
from tkinter import *
from tkinter import ttk
root = Tk()
root.title("calculator")
root.resizable(width='False', height='False')
icon = PhotoImage(file ='my_photo.png')
root.call('wm','iconphoto',root._w,icon)


def insert(text):

    if text != "=": 
        En.insert("end", text )
        
    else:
        try:
            operation = eval(En.get())
            En.delete( 0 ,"end")
            En.insert( 0 ,"{}".format (operation))
            
        except:
            En.delete( 0 ,"end")
            En.insert( 0 ,"math error")
    



def button(text , clmn ,rw ):
    ttk.Button(root , text = text , command = lambda:insert(text)).grid(column = clmn,row = rw , ipady=5 , ipadx=5)

En = ttk.Entry(root,font = "arial 16")
En.grid(column = 0 , row = 0 , columnspan = 3, ipadx = 4, ipady = 8)


button("-", 0 , 1 )
button("*", 1 , 1 )
button("/", 2 , 1 )
button("7", 0 , 2 )
button("8", 1 , 2 )
button("9", 2 , 2 )
button("4", 0 , 3 )
button("5", 1 , 3 )
button("6", 2 , 3 )
button("1", 0 , 4 )
button("2", 1 , 4 )
button("3", 2 , 4 )
button("0", 0 , 5 )
button(".", 1 , 5 )
button("=", 2 , 5 )
button("+", 2 , 6 )
button("c", 1 , 6 )
button("%", 0 , 6 )
root.mainloop()

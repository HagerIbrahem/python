from tkinter import *

window = Tk() 

window.title(" calculator ")
window.geometry('1000x2000') 

Button(window, bd = '5' ,text="1",background="blue",command = print("1")).place(x=1,y=1) #pack(side = TOP)
Button(window, bd = '5' ,text="2",background="blue",command = print("2")).place(x=10,y=10) #pack(side = TOP)
Button(window, bd = '5' ,text="3",background="blue",command = print("3")).place(x=20,y=20) #pack(side = TOP)
Button(window, bd = '5' ,text="4",background="blue",command = print("4")).place(x=30,y=30) #pack(side = TOP)
Button(window, bd = '5' ,text="5",background="blue",command = print("5")).place(x=40,y=40) #pack(side = TOP)
Button(window, bd = '5' ,text="6",background="blue",command = print("6")).place(x=50,y=50) #pack(side = TOP)
Button(window, bd = '5' ,text="7",background="blue",command = print("7")).place(x=60,y=60) #pack(side = TOP)
Button(window, bd = '5' ,text="8",background="blue",command = print("8")).place(x=70,y=70) #pack(side = TOP)
Button(window, bd = '5' ,text="9",background="blue",command = print("9")).place(x=80,y=80) #pack(side = TOP)

Button(window,text = "Close the window", bd = '5', command = window.destroy).pack(side = BOTTOM)




window.mainloop ()
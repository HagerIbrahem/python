from tkinter import *

window = Tk() 

window.title(" calculator ")
window.geometry('500x400') 

var = StringVar() 
 
operation =""

def click(char):
   global operation 
   operation +=char
   var.set(operation)


def Result():
   res=eval (var.get())
   global operation 
   operation += "=" + str(res)
   var.set(operation)
   operation =""
   
def clear ():
  #  operation.delete(len(var.get()-1))
    operation=""
    var.set(operation)




ent=Entry (window, bd = '30' ,textvariable=var).grid(row =0)
    

#                   ***********************  ROW1  ******************************
Button(window, bd = '30' ,text="1",background="white",command =lambda:click("1")).grid(row =1,column = 0) 
Button(window, bd = '30' ,text="2",background="white",command =lambda:click("2")).grid(row =1,column = 1)      
Button(window, bd = '30' ,text="3",background="white",command =lambda:click("3")).grid(row =1,column = 2)      
                                                                                     
Button(window, bd = '30' ,text="+",background="cyan",command =lambda:click("+")).grid(row =1,column = 3) 
 
#                   ***********************  ROW2  ******************************
Button(window, bd = '30' ,text="4",background="white",command =lambda:click("4")).grid(row =2 ,column = 0)      
Button(window, bd = '30' ,text="5",background="white",command =lambda:click("5")).grid(row =2 ,column = 1)      
Button(window, bd = '30' ,text="6",background="white",command =lambda:click("6")).grid(row =2 ,column = 2)      
                                                                                                 
Button(window, bd = '30' ,text="-",background="cyan",command =lambda:click("-")).grid(row =2 ,column = 3) 

#                   ***********************  ROW3  ******************************                                                                                                   
Button(window, bd = '30' ,text="7",background="white",command =lambda:click("7")).grid(row =3 ,column = 0)      
Button(window, bd = '30' ,text="8",background="white",command =lambda:click("8")).grid(row =3 ,column = 1)      
Button(window, bd = '30' ,text="9",background="white",command =lambda:click("9")).grid(row =3 ,column = 2) 
                                                                                     
Button(window, bd = '30' ,text="*",background="cyan",command =lambda:click("*")).grid(row =3 ,column = 3)  
 
#                   ***********************  ROW4  ******************************
Button(window, bd = '30' ,text=".",background="white",command =lambda:click(".")).grid(row =4 ,column = 0)      
Button(window, bd = '30' ,text="0",background="white",command =lambda:click("0")).grid(row =4 ,column = 1) 
Button(window, bd = '30' ,text="/",background="cyan",command =lambda: click("/")).grid(row =4 ,column = 3)  

#                     ********************* show result ***************************    
Button(window, bd = '30' ,text="=",background="yellow",command =lambda:Result()).grid(row =4 ,column = 2) 

#                     ********************* TO clear ***************************    
Button(window, bd = '30' ,text="cls",background="yellow",command =lambda:clear()).grid(row =4 ,column = 4)                                                                                     

#                     ********************  close window ************************                                                                                                         
Button(window,text = "Close the window", bd = '5', command = window.destroy).grid(row =6 ,column = 2)    


window.mainloop ()

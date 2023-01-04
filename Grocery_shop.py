import sys
import os
import csv
f1= open("Grocery_database.csv",'w')
dic={"banana":{"avilable quantity":1 ,"price":15} ,"cherry":{"avilable quantity":1 ,"price":20}}
f1.write ("banana,")
f1.write ("avilable quantity ,")
f1.write ('1')
f1.write (" ,price ,")
f1.write ('15')
f1.write ("\n")
f1.close()
def add_product ():
    N_prod =int(input("enter no.of products you want add")) 
    f1= open("Grocery_database.csv",'a')
    for n in range(N_prod):
      new_prod =input("enter name of product")
      f1.write (new_prod  +',')
      
      quantity =input("enter no.of kgs") 
      f1.write ("avilable quantity ,")
      f1.write (str(quantity)  +',')      
      
      price =int(input("enter price of product"))
      f1.write (" ,price ,")
      f1.write (str(price)  +',')
      f1.write ("\n")
      f1= open("Grocery_database.csv",'r')
      print(f1.read())
      
      f1.close()
      

def change_cost ():
    data =csv.reader(open("Grocery_database.csv",'r'))
    product= input("enter product you want change it's price ")
    for line in data:
       if(product == line[0] ) :
         price =int (input("enter the new price for this product"))
         line[4]= price 
       else:
          print("Product invalid")
          break
    
def buying():
#               take no.of products 
    N_prod =int(input("enter no.of products you want to buy"))
    data =csv.reader(open("Grocery_database.csv",'r'))
    f1= open("pill.text",'w')
    f1.write("                ITI shop fatora")
    for n in range(int(N_prod)):
#          take product name & check if it valid   
      prod_name =input("enter name of product")
      count=0
      for line in data:
         if(prod_name ==line[0] ):
           count+=1
    #          take no.of kgs & check if it's valid 
           quantity =int(input("enter no.of kgs"))
           if(quantity<=int(line[2])):
              line[2]-=quantity
              f1= open("pill.text",'a')
              f1.write(prod_name + ' -      ')
              f1.write(quantity + '-        ')
              f1.write(str(line[4] + '/n'))
              f1.close()
           else:
              print("quantity not avilable")
          
           
         if count==0:
           print("product not found")       
    pill_chose = int(input("if want print pill enter 1")) 
    if(pill_chose == 1):   
        f1= open("pill.text",'r')
        print(f1.read())    
      
print ("Welcom to ITI shop")
while(1):
  choise= int (input("If owner enter 1, if buyer enter 2,if want close system enter 3"))
  if choise==1:
    owner_ch =int(input("If want add product enter 1, if want show products enter 2, if want change cost enter 3"))
    if owner_ch==1:
        add_product ()
    elif owner_ch==2:
        f1= open("Grocery_database.csv",'r')
        print (f1.read())
    elif owner_ch==3:
       change_cost ()
    else:
     print("Invalid choice ")
     
  elif choise ==2:
    buyer_ch =int(input("If want show products enter 1, if want to buy enter 2 "))
    if buyer_ch==1:
        f1= open("Grocery_database.csv",'r')
        print (f1.read())
    elif buyer_ch==2:    
      buying()
    else:
     print("Invalid choice ")
   
  elif choise ==3:
   print("Hope to see you here again")
   break
  else:
     print("Invalid choice ")
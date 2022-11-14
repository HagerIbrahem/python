while 1:
 x= input("enter 1 if want Seintific mode or 2 if want programming mode")
 if int(x)==1:
   y,z,op =input("enter 2 values & operator").split(" ",2)
   if op == '+':
    print(int(y)+int(z))
    
   elif  op == '-':
    print(int(y)-int(z))  
   elif  op == '*':
    print(int(y)*int(z))
   elif  op == '/':
    print(int(y)/int(z)) 
   elif  op == '%':
    print(int(y)%int(z))  
   elif  op == '**':
    print(int(y)**int(z))      
   else:
    print("Invalid operator")
 
 elif int(x)==2:
    y,op =input("enter value & type of convet b for binary h for hexadecimal o for octal").split(" ",1) 
    if op == 'b':
     print(bin(int(y)))
    elif  op == 'o':
     print(oct(int(y))) 
    elif  op =='h':
     print(hex(int(y)))
    else:
     print("Invalid operator")
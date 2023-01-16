rows =  int (input("enter number of rows"))
 
for n in range (0 , rows): 
   print((rows-1-n) *" "  + ((2*n)+1) * '*')       
  
for n in range (rows):    
   print('*')

for n in range (0 , rows): 
   print((n) * " "  + ((rows+2)-(2*n)) * '*')  
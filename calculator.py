x = float(input("enter the value"))
y = float(input("enter the 2nd value"))

opration = (str(input("enter the oprations ('+' , '-' , '/' , '*' ): ")))

if opration == '+':
    print("result:" , ( x + y))
    
elif opration == '-':
    print("result" , ( x - y ))

elif opration == '/':
    if y == 0:
        print("error: division by zero is not allowed")
    else:
        print("result:", (x / y))
    

elif opration == '*':
    print("result" , ( x * y ))

else:
  print("error")

                     

    



 

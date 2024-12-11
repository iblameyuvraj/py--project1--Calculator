# py--project1--Calculator
<br>
My first Python project is a basic calculator that performs addition, subtraction, multiplication, and division. It takes user input for numbers and the operation, then displays the result. This project helped me understand Python basics like handling inputs, using conditions, and performing calculations.
<br>
<br>






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

                     

    



 

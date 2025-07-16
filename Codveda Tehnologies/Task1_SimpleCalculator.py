#Task to do:
#Develope a basic calculator that can perform four primary arithmetic operations:
#(addition,subtraction,mutliplicatin and the division...)

#Objectives:
#(1)Create functions for each operations.
#(2)Take two inputs from user and allow them to select the desired operation.
#(3)Handle division by zero with an appropiate error messages.


choice=int(input("YOUR CHOICE???\n1 for addition\n2 for subtarction\n3 for multiplication\n4 for divison\n"))
num1 = int(input("Enter your First Number: "))
num2 = int(input("Enter your Second Number: "))

#ADDITION:
def add(num1,num2):
    addition=int(num1+num2)
    return(addition)
    
#SUBTRACTION:
def subtract(num1,num2):
    subtraction=int(num1-num2)
    return(subtraction)
    
#MULTIPLICATION:
def product(num1,num2):
    multiplication=int(num1*num2)
    return(multiplication)
    
#DIVISION:    
def quotient(num1,num2):
   if num2 == 0:
       print("Error: Cannot divide by zero!")
   else:
       division=int(num1//num2)
       return(division)
    
#Solutions:)
if choice==1:
  plus=add(num1,num2)
  print(plus)

elif choice==2:
    sub=subtract(num1,num2)
    print(sub)

elif choice==3:
    mult=product(num1,num2)
    print(mult)

elif choice==4:
    div=quotient(num1,num2)
    print(div) 

else:
    print("AN INVALID CHOICE")

# P R O G R A M --- E N D :)




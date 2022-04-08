
#A simple calculator that allows users to add, subtract, multiply or divide two numbers together. 

#Welcome functiom
def welcome():
    print("Welcome \n Options: add(int,int) , subtract(int,int) , multiply(int,int) , divide(int,int) ")

#Add function that takes in two variables
def add(num1, num2):
    print(num1+num2)


#Subtraction function that takes in two variables
def subtract(num1, num2):
    print(num1-num2)


#Multiply function that takes in two variables
def multiply(num1, num2):
    print(num1*num2)


#Division function that takes in two variables
def divide(num1, num2):
    print(num1//num2)

#Call for welcome() to be executed
if __name__ == "__main__":
    welcome()
  

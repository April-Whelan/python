# This function will call for the code inside that will specify if a number inputted by the user is odd or even. 
def OddOEven():

  #Ask for user input
    user_input = int(input("Enter a number: ")) 
    
    if (user_input % 2) == 0:
        
        print("{0} is an even number".format(user_input)) #format formats the values and places them within the placeholder ( {} ) format() returns formatted string. 

        print('---------------------------------------------------------')

    else:
        
        print("{0} is an odd number".format(user_input))

print('---------------------------------------------------------') 
  
  #This code will return the highest number from a set of specified numbers. 
def highest():
    num1 = 100
    num2 = 14
    num3 = 1217

    #If statement that translates to: If num1 is greater than or equal to num2 and if num1 is greater than or equal to num3, print num1
    if  (num1 >= num2) and (num1 >= num3):
        
        print(num1)
        
    elif(num2 >= num1) and (num2 >= num3):
        
         print(num2)
         
    else:
         print('---------------------------------------------------------')
         print(num3)
#In this case the output will be 1217. 
  
  #This code will return the lowest number from a set of specified numbers. 
def lowest():
    num1 = 100
    num2 = 14
    num3 = 1217

   #If statement that translates to: if num1 is less than or equal to num2 and num3, print num1
    if  (num1 <= num2) and (num1 <= num3):
        
        print(num1)
        
    elif(num2 <= num1) and (num2 <= num3):

         print('---------------------------------------------------------')
        
         print(num2)
        
        
    else:
        
        print(num3)
        
   #In this case the output will be 14. 

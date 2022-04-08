
# Code that will print out a happy birthday message followed by the correct ordinal that corrsponds with the number given. Example: Happy 21ST, 22ND, 23RD birthday! 

#create happy birthday function to be called
def happy_birthday():
   
 #Specify the int variable
    age = 24
  
 #Change the variable age from an int into a string. 
    ordinal = str(age)
 
#if, elif and else statements to cover a number of different options. 

# The // symbol is an operator and is floor division that will result into whole number adjusted to the left in the number line. 
    if age // 10 == 1:
    
 #The +- symbol is an operator and will add the two values together and assigns the final value to ordinal. 
         ordinal += ('th')
         
  #The % symbol is a modulo and will return the remainder of diving the left hand operand by the right hand operand. 
    elif age % 10 == 1:
         ordinal += ('st')
         
    elif age % 10 == 2:
         ordinal += ('nd')
         
    elif age % 10 == 3:
         ordinal += ('rd')
         
    else:
         ordinal += ('th')

    #Print a sentence to console. In this instance it will read 'Happy 24th birthday!'
    print("Happy" + " " +  ordinal + " " + "birthday!")

    
    # This next block of code is used for manipulating a string sentence. 
    
    #Create function name change
    def name_change():
    
  
#Assign sentence to fullname variable 

    fullname = "Jane Emma Doe"
   
#Split the name into a list
    fullname.split()

  # Get the index of the last name
    last = fullname.split()[2]
    
   #Get the index of the first name
    first = fullname.split()[0]
    
   #Print last name
    print(last)
    
    #Formatting for readability
    print('---------------------------------------------------------')
    
    #Print first name
    print(first)
    
    print('---------------------------------------------------------')
   
  #Reverse the name 
    print("Reversed: " + fullname[::-1])

    print('---------------------------------------------------------')

def totala():
    
    print("Jane Emma Doe".count('a'))

    print('---------------------------------------------------------')

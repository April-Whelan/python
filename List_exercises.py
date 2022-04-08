#This document will showcase some exercises that showcase the use of lists. 

def num_list():

  #Store 10 numbers inside a list
    numbers = [2, 3, 8, 9, 12, 13, 14, 15, 18, 25]

    #Create a second empty list that we can add values to later 
    second_list = []

    #Loop through number list
    for less in numbers:

      #If a number that is less than 5 is found... add it to the second_list.
        if less < 5:

            second_list.append(less)
            
        #Finally, print the second list. 
            print(second_list)

   #Next Function
          
   def fruit_alpha():

    #Create a list with 5 strings inside. 
    
    fruit_list = ["Dragonfruit", "Lime", "Clementine", "Kiwi", "Apple"] 

    #Use the sort() method to sort the strings in alphabetical order.
    
    #print the list. 
    print(sorted(fruit_list))

    #Create a new list with 5 strings inside. 
    veg_list = ["Broccoli", "Spinach", "Pototo", "Peas", "Garlic"]

    #use sorted to sort the strings inside both lists in alphabetical order and print them as one sorted list. 
    merge = sorted(fruit_list + veg_list)

    print(merge)

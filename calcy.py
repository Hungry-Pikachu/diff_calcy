

name = input("What's your name champ ?  ")
print ("Hello " + name)
print('''
      
      
      
      I am a calulator which can perform calculations just like normal calcy's , but with some fun 
      I can perform like other normal calcy's here but with some more functions ...::))))
      I can calculate upto 5 numbers straight and no mix calculations ...:(
      I am upgrading myself but it will tak some time till then , let's perform some calculations ....:)))
      
      ''')

no_of_numbers = input(" Firstly ,  tell me how many numbers you want to calculate(must be atleast 2 ..) ")




if no_of_numbers == 2:

    print('''
      
      Here's a small guide on how to use me .. :)
      press 1 to perform Addition ,
      press 2 to perform Subtraction,
      press 3 to perform Multiplication,
      press 4 to perform Division 
      
      ''')

    operator = input("Which operation do you want to perform .. ?    ")

    
    if operator ==  '1' :
        num1 = int(input("Enter 1st number : "))
        num2 = int(input("Enter 2nd number : "))
        res = num1 + num2 
        print("Your solution is : " + str(res))
    
    elif operator == '2' :
        num1 = int(input("Enter 1st number : "))
        num2 = int(input("Enter 2nd number : "))
        res = num1 - num2
        print("Your solution is : " + str(res))
    
    elif operator == '3' :
        num1 = int(input("Enter 1st number : "))
        num2 = int(input("Enter 2nd number : "))
        res = (num1 * num2)
        print("Your solution is : " + str(res))
    
    elif operator == '4' :
        num1 = int(input("Enter 1st number : "))
        num2 = int(input("Enter 2nd number : "))
        res = (num1 / num2)
        print("Your solution is : " + str(res))
    
    else :
        print("Incorrect input :( .............. Please try again . ")
        
elif no_of_numbers == '3' :
    print('''
      
      Here's a small guide on how to use me .. :)
      press 1 to perform Addition ,
      press 2 to perform Subtraction,
      press 3 to perform Multiplication,
      press 4 to perform Division 
      
      ''')

    operator = input("Which operation do you want to perform .. ?    ")

    
    if operator ==  '1' :
        num1 = int(input("Enter 1st number : "))
        num2 = int(input("Enter 2nd number : "))
        num3 = int(input("Enter 3rd number :  "))
        res = num1 + num2 + num3
        print("Your solution is : " + str(res))
    
    elif operator == '2' :
        num1 = int(input("Enter 1st number : "))
        num2 = int(input("Enter 2nd number : "))
        num3 = int(input("Enter 3rd number :  "))
        res = num1 - num2 - num3
        print("Your solution is : " + str(res))
    
    elif operator == '3' :
        num1 = int(input("Enter 1st number : "))
        num2 = int(input("Enter 2nd number : "))
        num3 = int(input("Enter 3rd number :  "))
        res = num1 * num2 * num3
        print("Your solution is : " + str(res))
    
    elif operator == '4' :
        num1 = int(input("Enter 1st number : "))
        num2 = int(input("Enter 2nd number : "))
        num3 = int(input("Enter 3rd number :  "))
        res = num1 / num2 / num3
        print("Your solution is : " + str(res))
    
    else :
        print("Incorrect input :( .............. Please try again . ")
else:
    print("Invalid Input. Please try again..:)) ")
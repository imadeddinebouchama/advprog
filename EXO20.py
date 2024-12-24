
user_list = []

while True:
   
    number = float(input("\nEnter a number (0 to stop): "))
    
   
    if number == 0:
        print("\nProgram ended!")
        break
    
 
    user_list.append(number)
    
  
    print("\nCurrent List:", user_list)
    print("Sorted List:", sorted(user_list))

numbers = [1, 2, 3, 4, 5]


print("Initial list:", numbers)

while True:
    
    index = int(input("Enter the index (or -1 to stop): "))
    
    
    if index == -1:
        break

    
    if 0 <= index < len(numbers):
    
        new_value = int(input("Enter the new value: "))
        
        
        numbers[index] = new_value
        
        
        print("Updated list:", numbers)
    else:
        print("Invalid index. Please try again.")

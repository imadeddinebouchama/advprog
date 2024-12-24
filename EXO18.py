numbers = [1, 2, 3, 4, 5]

while True:
    print("\nCurrent list:", numbers)
    print("\nMenu:")
    print("1. Append an element")
    print("2. Insert an element at a specific position")
    print("3. Pop an element")
    print("4. Remove an element")
    print("5. Quit")
    
    choice = input("\nEnter your choice (1-5): ")
    
    if choice == '1':
        num = int(input("Enter the number to append: "))
        numbers.append(num)
        print("Number appended successfully!" , numbers)
        
    elif choice == '2':
        pos = int(input("Enter the position to insert: "))
        num = int(input("Enter the number to insert: "))
        if 0 <= pos <= len(numbers):
            numbers.insert(pos, num)
            print("Number inserted successfully!", numbers)
        else:
            print("Invalid position!")
            
    elif choice == '3':
        if numbers:
            popped = numbers.pop()
            print(f"Popped element: {popped}")
        else:
            print("List is empty!")
            
    elif choice == '4':
        num = int(input("Enter the number to remove: "))
        if num in numbers:
            numbers.remove(num)
            print("Number removed successfully!", numbers)
        else:
            print("Number not found in the list!")
            
    elif choice == '5':

        break
        
    else:
        print("Invalid choice! Please select 1-5")
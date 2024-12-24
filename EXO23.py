
while True:
    try:
        N = int(input("Enter a positive integer: "))
        if N > 0:
            break
        else:
            print("Please enter a positive number.")
    except ValueError:
        print("Please enter a valid integer.")


for number in range(-N, N + 1):
    if number != 0:  
        print(number)
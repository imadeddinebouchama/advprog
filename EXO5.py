
name1 = input("Enter first runner's name: ")
time1 = float(input("Enter first runner's time (seconds): "))

name2 = input("Enter second runner's name: ")
time2 = float(input("Enter second runner's time (seconds): "))


if time1 < time2:
    print(f"{name1} was faster!")
elif time2 < time1:
    print(f"{name2} was faster!")
else:
    print("It's a tie!")
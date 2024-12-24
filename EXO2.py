temp = int(input("Enter the temperature: "))

# Check conditions from coldest to warmest
if temp < 0:
    print("It's freezing!")
if temp < 10:
    print("It's cold!")
if temp < 20:
    print("It's cool!")

print("Stay safe!")
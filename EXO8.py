
number = int(input("Enter an integer: "))


if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")

elif number % 3 == 0:
    print("Fizz")

elif number % 5 == 0:
    print("Buzz")
else:
    print("The number is not divisible by 3 or 5.")

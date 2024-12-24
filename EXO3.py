
amount = float(input("Enter total purchase amount: "))
items = int(input("Enter number of items: "))
day = input("Enter day of week (Monday-Sunday): ").lower()


discount = 0


if day in ["monday", "tuesday", "wednesday", "thursday", "friday"]:
    discount = 0.10  
elif day in ["saturday", "sunday"]:
    discount = 0.20  


if items > 5:
    discount += 0.05  


final_price = amount * (1 - discount)

print(f"Total discount: {discount*100}%")
print(f"Final price: {final_price:.2f}")
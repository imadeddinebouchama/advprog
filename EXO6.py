price = float(input("Enter price in dinars: "))

dinars = int(price)
centimes = int((price - dinars) * 100)

print(f"Dinars: {dinars}")
print(f"Centimes: {centimes}")
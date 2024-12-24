
cities = []


while True:
    city = input("Enter a city name (or type 'stop' to finish): ")
    if city.lower() == 'stop':
        break
    else:
        
        population = len(city)*1000000
        cities.append((city, population))


cities.sort(key=lambda x: x[1], reverse=True)

# Print the cities and their populations in order
print("\nCities sorted by population (largest to smallest):")
for city, population in cities:
    print(f"{city}: {population}")

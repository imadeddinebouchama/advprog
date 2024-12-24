

people = int(input("Enter total number of people: "))
taxi_size = int(input("Enter how many people fit in one taxi: "))


full_taxis = people // taxi_size


remaining_people = people % taxi_size


if remaining_people > 0:
    total_taxis = full_taxis + 1
else:
    total_taxis = full_taxis

print("You need", total_taxis, "taxis")
print("Last taxi will have", remaining_people, "people ")
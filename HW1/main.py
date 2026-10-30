# HW1: Group Trip Budget Calculator.

# The program
   #-The program intends to calculate the shared costs of a group trip and determine how much each traveler should pay.
   #-The calculation considers five inputs: the number of travelers, the number of nights, the nightly accommodation cost for the whole group, the total transportation cost for the whole trip, and the daily food cost per person.
   #-Using these inputs, it calculates the total accommodation, food, and trip costs, then divides the total expenses equally among all travelers.
   #-The program assumes that trip duration is one day longer than the number of nights and that all expenses are shared equally.

##Sample inputs and their corresponding variables:

Travelers: 4
Nights: 2
Accommodation_per_night_for_whole_group: 120
Transport_for_whole_trip_for_whole_group: 80
Food_per_person_per_day: 15

Total_accommodation: 240.0
Total_food: 180.0
Total_trip: 500.0
Cost_per_traveler: 125.0

##Calculation steps:

# 1.Collect trip information from the user
travelers = int(input("Travelers: "))
nights = int(input("Nights: "))
accommodation = int(input("Nightly accommodation cost: "))
transportation = int(input("Total transportation cost: "))
food = int(input("Daily food cost per person: "))
# 2.Calculate the total number of trip days
days = nights + 1 #Assuming the trip duration is one day longer than the number of nights.
# 3.Calculate total accommodation cost
total_accommodation = accommodation * nights
# 4.Calculate total food cost
total_food = food * travelers * days
# 5.Calculate total trip cost
total_trip_cost = total_accommodation + transportation + total_food
# 6.Calculate cost per traveler
cost_per_traveler = total_trip_cost / travelers
# 7.Display the results
print("Total accommodation cost:", total_accommodation)
print("Total food cost:", total_food)
print("Total trip cost:", total_trip_cost)
print("Cost per traveler:", cost_per_traveler)



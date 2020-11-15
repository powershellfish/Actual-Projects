# Random Restaurant Generator
# Demonstrated the elif clause, and random module (with randint)
# Tired of picking the same restaurant over and over again on date night?
# Tire no more. This program will generate a random restaurant that
# corresponds to a random integer (thanks, random.randint!)
# Updating for Bailey

import random

print("Thinking of a place to eat tonight...")
print("I think I have just the right thing!")

restaurant = random.randint(1,10)

if restaurant == 1:
    # jake and telly's
    print("Jake and Telly's")

elif restaurant == 2:
    # phantom canyon
    print("Phantom Canyon")

elif restaurant == 3:
    # mcdonalds
    print("McDonalds")

elif restaurant == 4:
    # noodles
    print("Noodles and Co.")

elif restaurant == 5:
    # N3
    print("N3 Taphouse")

elif restaurant == 7:
    # fuzzy's
    print("Fuzzy's Tacos")

elif restaurant == 8:
    # heart of jerusalem
    print("Heart of Jerusalem")

elif restaurant == 9:
    # cmb
    print("Colorado Mountain Brewery")

elif restaurant == 10:
    # front range
    print("Front Range BBQ")

else:
    print("Illegal restaurant value! No dinner! for you!")

input("\n\nPress the enter key to exit.")

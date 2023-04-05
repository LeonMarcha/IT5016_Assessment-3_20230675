# Revisions in attempted compliance with PEP8
print("Welcome to the Zodiac finder")
year = int(input("Please enter a year: "))
year_name = ("Dragon", "Snake", "Horse", "Sheep", "Monkey", "Rooster",
             "Dog", "Pig", "Rat", "Ox", "Tiger", "Hare"
             )
# I'm not sure where to break the list, this looks good enough?
if year % 12 == 0:
    print(year_name[0])
elif (year - 2000) % 12 == 1:
    print(year_name[1])
elif (year - 2000) % 12 == 2:
    print(year_name[2])
elif (year - 2000) % 12 == 3:
    print(year_name[3])
elif (year - 2000) % 12 == 4:
    print(year_name[4])
elif (year - 2000) % 12 == 5:
    print(year_name[5])
elif (year - 2000) % 12 == 6:
    print(year_name[6])
elif (year - 2000) % 12 == 7:
    print(year_name[7])
elif (year - 2000) % 12 == 8:
    print(year_name[8])
elif (year - 2000) % 12 == 9:
    print(year_name[9])
elif (year - 2000) % 12 == 10:
    print(year_name[10])
elif (year - 2000) % 12 == 11:
    print(year_name[11])

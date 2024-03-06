print("================ Mad-Lib ================")
print("Enter your name")
name = input(">> ").capitalize()
print("Enter an adjective")
adjective = input(">> ")
print("Enter a verb")
verb = input(">> ")
print("Enter a place")
place = input(">> ")
print("Enter a food")
food = input(">> ")
print("Enter a vehicle")
vehicle = input(">> ")
print(name+" is a very "+adjective+" person to be around. They love to "+verb+" in "+place+". Their favourite food is "+food+" which they eat in the "+vehicle+". ") 

print("================ Convert Minutes into Seconds ================")
print("Enter the number of minutes that you'd like to convert")
minutes = int(input(">> "))
seconds = minutes * 60
print(seconds, "seconds")

print("================ Birthday Cards ================")
print("Enter that how many cards Cruella received for her last birthday")
cards_for_Cruella = int(input(">> "))
cards_for_Jane = cards_for_Cruella * 2
print("Jane receives at least", cards_for_Jane, "cards.")

print("================ Age to Days ================")
DAYS_IN_A_YEAR = 365
years = int(input("Enter your age in years: "))
days = years * DAYS_IN_A_YEAR
days_to_100_years = DAYS_IN_A_YEAR*100 - days
print("You are", days, "days old. In", days_to_100_years, "days you will be 100 years old!")

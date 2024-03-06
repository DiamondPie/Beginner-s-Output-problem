# This is the one-line version of the homework :P
# Each of them only needs 1 line, but it can run normally, as same as the normal one

print("================ Mad-Lib ================")
print("{} is a very {} person to be around. They love to {} in {}. Their favourite food is {} which they eat in the {}.".format(*[(ask := lambda: input(f"Enter {'your' if key == 'name' else 'an' if key[0] in ['a', 'e', 'i', 'o', 'u'] else 'a'} "+key+"\n>> "))().capitalize() if not index else ask() for index, key in enumerate(["name", "adjective", "verb", "place", "food", "vehicle"])])) # Add placeholders into the list on my left
# You can add more {} in the sentence and more placeholders into the list
# (at the end of the line of code) to insert more variables 
# (however they should be ORDERED)

print("================ Convert Minutes into Seconds ================")
print(int(input("Enter the number of minutes that you'd like to convert\n>> "))*60, "seconds")

print("================ Birthday Cards ================")
print("Jane receives at least", int(input("Enter that how many cards Cruella received for her last birthday\n>> "))*2, "cards.")

print("================ Age to Days ================")
print("You are {} days old. In {} days you will be 100 years old!".format(days := int(input("Enter your age in years: "))*365, 365*100-days))

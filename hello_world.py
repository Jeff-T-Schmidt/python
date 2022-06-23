# message = 'Helloooo Python World!'
# print(message)

# message = "Hello from crash course!"
# print(message)

# first_name = "ada"
# last_name = 'lovelace'
# full_name = f"{first_name} {last_name}"
# message = f"Hello, {full_name.title()}!"
# print(message)

# print("\tPython")

# message = "One of Python's strengths is its diverse community"
# print(message)

# print(2+2)

# import this


# names = ['nate', 'jeff', 'igor', 'josh']

# print(names[0].title())
# message = f"{names[0].title()} is lame!"
# print(message)
# names.append('wyland')
# print(names)
# names.insert(0, 'brady')
# print(names)
# del names[1]
# print(names)

# popped_names = names.pop(0)
# print(names)
# print(popped_names)

# bad_magic = 'igor'
# names.remove(bad_magic)
# print(names)
# print(f"\n {bad_magic.title()} is bad at magic!")

# names.insert(0, 'zebra')
# names.sort()
# print(names)
# print(len(names))


# squares = []

# for value in range(1,11):
#     # square = value **2
#     squares.append(value**2)
# print(squares)

# squares = [value**2 for value in range(1,11)]
# print(squares)

# my_foods = ['ice cream', 'chocolate cake', 'candy']
# wife_foods = my_foods[:]

# my_foods.append('cheesecake')
# wife_foods.append('korean food')

# print('My fav foods are:')
# for my_food in my_foods:
#     print(my_food)

# print("\nMy wife's fav foods are:")
# for wife_food in wife_foods:
#     print(wife_food)

# foods = ("veg","rice", "beans", "bread", "meat")
# for food in foods:
# # food[0] = 'water'
#     print(food)
# foods = ("\nveg","rice", "beans", "stuff", "water")
# for food in foods:
#     print(food)

# tosh_friends = ['liam', 'jesse', 'niko', 'star', 'brenda', 'jeff']

# for tosh_friend in tosh_friends:
#     print(f"{tosh_friend.title()} is Tosh's friend!")
#     print(f"Tosh should go and stay at your house, if that is cool {tosh_friend.title()}.\n")\


# Got it to work!
# banned_users = ['tosh', 'jeff', 'brenda', 'john']
# users = ["nancy", 'brady', 'john']

# for banned_user in banned_users:
#     print(f"{banned_user.title()} you can't leave a message")
# for user in users:
#     if banned_user != user:
#         print(f"\n{user.title()} you are free to leave a comment!")

# user_0 = {
#     'first_name':'jeff',
#     'last__name': 'schmidt',
#     'middle_name':'tosh'
# }
# for k, v in user_0.items():
#     print(f"\nKey: {k}")
#     print(f"Value: {v}")

# 6/23/2022

# prompt = "if you tell me your name, I will personalize a message for you."
# prompt += "\nWhat is your name?"

# name = input(prompt)
# print(f"\nHello {name.title()}")

# height = input("How tall are you, in inches?")
# height = int(height)

# if height >= 48:
#     print("\nYou are tall enough to ride")
# else:
#     print("\nYou aren't tall enough, sorry, better luck next year!")

# prompt = "\nWhat pizza toppings would you like"
# prompt += "\n(Enter 'quit' when you are finished)"

# while True:
#         pizza_toppings = input(prompt)

#         if pizza_toppings == 'quit':
#             print("Thank you, pizza is going in the oven, see ya soon!")
#             break
#         else:
#             print(f"{pizza_toppings.title()} has been added to the pie!")

# responses = {}
# polling_active = True

# while polling_active:
#     name = input("\nWhat is your name?")
#     response = input("Which mountain would you like to climb someday?")

#     responses[name.title()]= response

#     repeat = input("Would you like to let another person resond? (yes/no)") 
#     if repeat == 'no':
#         polling_active = False

# print("----Polling results----")
# for name, response in responses.items():
#     print(f"{name} would like to climb {response}.")

# def make_sandwich(size, *toppings):
#     print(f"Making a {size}-inch sandwhich with the following toppings:")
#     for topping in toppings:
#         print(f"-{topping}")

# make_sandwich(10, 'ham', 'turkey', 'lettuce', 'tomato')

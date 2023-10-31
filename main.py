# print("Hello World")

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# anotherdict = {

# }

# program_langs = ["Python", "C", "Javascript", "C++"]

# def fourth_place(langs):
#     """Return the 4th item is the list argument.

#     Args:
#         langs: a list of programming languages as strings

#     Returns:
#     str: the 4th item of the langs list as a string
# """
#     try:
#         return langs[3]
#     except:
#         return ("Less Than 4 Items")


# print(fourth_place(program_langs))


# def dict_sayer(dict):

#     """Checks to see if the dictionary argument that it takes is empty or not

#     Args:
#         dict: any dictionary

#     Returns:
#         True if the dictionary has items
#         False if the dictionary does not have any items   
# """
#     for key, value in dict.items():
#         print(f"{key}: {value}")
#         return True
#     if dict == {}:
#         print(f"{dict} is empty")
#         return False
# dict_sayer(thisdict)


# def galaxy(home_planet, *args, **kwargs):
#     """List planets
    
#     Args:
#         home_planet: positional argument for the users home planet
#         args: argument that allows the user to list as many planets as they can think of
#         kwargs: keyword argument that allows the user to set pluto_is_planet to True or False

#     Prints:
#         The users home planet. The varying number of planets as strings and wheter the user thinks that pluto is a planet as a boolean
#     """
    
#     strargs = ", ".join(args)
 
#     print(f"{home_planet}: {strargs}: {kwargs}")

    

# galaxy("earth", "mercury", "mars", "jupiter", "venus", "uranus", "saturn", pluto_is_planet=False)



class Cat:
    def __init__(self, color, name):
        self.color = color
        self.name = name

    def meow(self):
        print("Mmmrreow!")
    
siamese = Cat("black", "Jeff")

print(siamese.name)

sphinx = Cat("grey", "Jeffy")

sphinx.meow()
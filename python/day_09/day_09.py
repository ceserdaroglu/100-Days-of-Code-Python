programming_dictionary = {
    "Bug":"An error in a program that prevents the program from running as expected.",
    "Function":"A piece of code that you can easily call over and over again.",
    "Loop":"The action of doing something over and over again.",
}
print(programming_dictionary["Bug"])

#adding new items to dictionary.
programming_dictionary["Dysi"]="Ceren's nick name."
print(programming_dictionary)

#create an empty dictionary.
empty_dictionary = {}

#wipe an existing dictionary
# programming_dictionary={}
# print(programming_dictionary)

#edit an item in a dictionary.
programming_dictionary["Bug"] = "Bug is bug."
print(programming_dictionary)

#loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

#Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}
#nesting a list in a dictionary
travel_log = {
    "France": ["Paris", "Lille","Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

#nesting dictionary in a dictionary
travel_log = {
    "France":{"cities_visited": ["Paris", "Lille","Dijon"],"total_visits":123},
    "Germany":{"cities_visited": ["Berlin", "Hamburg", "Stuttgart"],"total_visits":5},
}
#nesting dictionary in a list
travel_log = [
    {"country": "France",
     "cities_visited": ["Paris", "Lille","Dijon"],
     "total_visits":123
    },
    {"country": "Germany",
     "cities_visited":["Berlin", "Hamburg", "Stuttgart"],
     "total_visits":5
     },
]
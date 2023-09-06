# def greet():
#     print("Hello")
#     print("How do you do?")
#     print("Isn't the weather nice today?")

# greet()
#----------------------------------------------------------------------------------
# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")

# greet_with_name(input("What is your name?"))
#----------------------------------------------------------------------------------
def greet_with(name,location):
    print(f"Hello {name}")
    print(f"How do you do {name}?")
    print(f"Isn't the weather nice today {location}?")
greet_with(input("What is your name?"),input("What is location?"))

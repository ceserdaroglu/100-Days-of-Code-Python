print("Welcome to the rollercoaster!")

height = int(input("What is your height in cm? "))
if height>=120:
    print("You can ride the rollercoaster!")
    age=int(input("What is your age?"))
    
    if age <12:
        ticket=5
        print("Young ticket is $5.")
    elif age<=18:
        ticket=7
        print("Young adult ticket is $7.")
    elif age >= 45 and age <=55:
        ticket=0
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        ticket=12
        print("Adult ticket is $5.")
    photo=input("Do you photo taken? Y or N. ")
    if photo=="Y":
        ticket+=3
        print(f"Your ticket is ${ticket}.")
    else:
        print(f"Your ticket is ${ticket}.")
else:
    print("Sorry, you have to grow taller before you can ride.")
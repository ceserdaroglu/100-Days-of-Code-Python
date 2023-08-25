
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")


s_pizza= 15
m_pizza= 20
l_pizza= 25

s_pepperoni = 2
pepperoni = 3
cheese= 1

pizza = 0

if size == "S":
    pizza=pizza+s_pizza
elif size == "M":
    pizza+=m_pizza
elif size == "L" :
    pizza+=l_pizza
else:
    print("Please choose.")

if add_pepperoni == "Y":
    if size== "S":
        pizza += s_pepperoni
    elif size == "M" or size == "L":
        pizza +=pepperoni
if extra_cheese == "Y":
    pizza += cheese

print(f"Your final bill is: ${pizza}.")
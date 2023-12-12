# import turtle 

# timmy =turtle.Turtle()

from turtle import Turtle, Screen
timmy = Turtle()
print(timmy)
timmy.shape("turtle")
#timmy.color("red")
timmy.color("coral") #rengini değiştirdik
timmy.forward(100)  #100 adım ileri

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
from turtle import Turtle, Screen
from random import randint
screen = Screen()
screen.setup(width=500,height=400)
user_input = screen.textinput(title="Make your bet", prompt="Type the color you want to bet on")

#Creating a list of colors for the turtles
colors = ["red", "blue", "green", "yellow", "orange", "purple"]

# creating an empty list to append objects of turtles
turtles = []

# Y coordinate starts at 120 and decreased by 50 which gives space to turtles 
y = 120
for name in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(name)
    new_turtle.penup()
    new_turtle.goto(-200, y)
    y = y - 50
    turtles.append(new_turtle)

#initialising the is_race_on variable to false
is_race_on = False

# Race starts if user_input in colors
if user_input in colors:
    is_race_on = True

else:
    screen.bgcolor("lightyellow")
    new_turtle.hideturtle()
    new_turtle.goto(0, 0)
    new_turtle.write(f"🚫 '{user_input}' is not in the race!\nTry red, blue, green, orange, yellow or purple.",
                  align="center", font=("Arial", 12, "bold"))
    
# Race starts if the user_input isin Colors
while is_race_on:
    # It will loop through the each turtle
    for turtle in turtles:
        #Checks the turtle x coordinate is > 230
        if turtle.xcor() > 230:
            if user_input == turtle.pencolor():
                print(f"Victory is yours! The turtle {turtle.pencolor} rules the race!")
                is_race_on = False
            else:
                print(f"Oops! Your turtle took a nap mid-race. Better luck next time! {turtle.pencolor()} won the game")
                is_race_on = False
        else:
            rand_num = randint(1,10)
            turtle.forward(rand_num)

#Dont close the screen until the user wants to close it
screen.exitonclick()
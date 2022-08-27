from turtle import Turtle, Screen
import random


screen = Screen()
screen.title("Race is on!!")
is_race_on = False
screen.setup(width=1000, height=600)
user_bet = screen.textinput(title="Make your bet", prompt="which turtle will win the race? Enter a color")
screen.title(f"Player selected {user_bet} Turtle. Good luck!!")
turtle_colors = ["red", "blue", "green", "orange", "purple", "brown"]
y_position = [-100, -50, 0, 50, 100, 150]
all_turtles = []
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(turtle_colors[turtle_index])
    new_turtle.goto(x=-480, y=y_position[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 470:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                screen.title(f"You won! The {winning_color} turtle is the winner!")
            else:
                screen.title(f"You lost! The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()


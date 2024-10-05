from turtle import Turtle ,Screen
import random
is_race_on=False
myscreen=Screen()
myscreen.setup(width=500,height=400)
user_bet=myscreen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color(red,orange,yellow,green,blue,purple): ")
color=["red","orange","yellow","green","blue","purple"]
y_position = [-70,-40,-10,20,50,80]


all_turtle=[]


for i in range (0,6):   
    new_turtle=Turtle(shape="turtle")
    new_turtle.color(color[i])
    new_turtle.penup()
    new_turtle.goto(x=-240,y=y_position[i])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on=True
while is_race_on:

    for turtle in all_turtle:
        if turtle.xcor()>230:
            is_race_on=False
            winning_color =turtle.pencolor()
            if winning_color==user_bet:
                print(f"You've won! The {winning_color} turtle is the  winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        rand_distance=random.randint(0,10)
        turtle.forward(rand_distance)

    
myscreen.exitonclick()
from turtle import Screen, Turtle
from paddle import Paddle

screen = Screen()
screen.setup(width=800,height=600) # Set the size of the screen
screen.bgcolor("black") # Set the background color to black
screen.title("Pong") # Set the title of the window
screen.tracer(0)

r_paddle = Paddle(position=(350,0))   
l_paddle = Paddle(position=(-350,0))


screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")
    
game_is_on = True

while game_is_on:
    screen.update()

screen.exitonclick()
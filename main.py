from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800,height=600) # Set the size of the screen
screen.bgcolor("black") # Set the background color to black
screen.title("Pong") # Set the title of the window
screen.tracer(0)

r_paddle = Paddle(position=(350,0))   
l_paddle = Paddle(position=(-350,0))

ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")
    
game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    # Detect for collision with the top or bottom wall
    if ball.ycor() > 280 or ball.ycor() < - 280:  # Assuming window height is 600
        ball.bounce_y()
        
    # Detect collision with paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320
        or ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    #Detect when r_paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    
    #Detect when l_paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()






screen.exitonclick()
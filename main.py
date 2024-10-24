from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=800,height=600) # Set the size of the screen
screen.bgcolor("black") # Set the background color to black
screen.title("Pong") # Set the title of the window


paddle = Turtle("square")
paddle.color("white")
paddle.shapesize(stretch_wid=5,stretch_len=1)
paddle.penup()
paddle.goto(350,0)
    
def go_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)

def go_down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)     
    


screen.listen()
screen.onkey(go_up,"Up")
screen.onkey(go_down,"Down")
    

screen.exitonclick()
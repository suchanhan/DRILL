import turtle

def turtle_w():
    turtle.setheading(90)
    turtle.forward(50)
    turtle.stamp()

def turtle_s():
    turtle.setheading(270)
    turtle.forward(50)
    turtle.stamp()

def turtle_a():
    turtle.setheading(180)
    turtle.forward(50)
    turtle.stamp()

def turtle_d():
    turtle.setheading(0)
    turtle.forward(50)
    turtle.stamp()

def restart():
    turtle.reset()


turtle.shape('turtle')
turtle.onkey(turtle_w,'w')
turtle.onkey(turtle_s,'s')
turtle.onkey(turtle_a,'a')
turtle.onkey(turtle_d,'d')
turtle.onkey(restart,'Escape')

turtle.listen()

turtle.exitonclick()


        
    



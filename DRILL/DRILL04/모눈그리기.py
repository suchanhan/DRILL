import turtle

turtle.penup()
turtle.goto(-250,-250)
turtle.pendown()
count=6
while(count>0):
   turtle.forward(500)
   turtle.penup()
   turtle.back(500)
   turtle.left(90)
   turtle.forward(100)
   turtle.pendown()
   turtle.right(90)
   count=count-1

   

turtle.penup()
turtle.goto(-250,-250)
turtle.left(90)
coun=6
while(coun>0):
   turtle.forward(500)
   turtle.penup()
   turtle.back(500)
   turtle.right(90)
   turtle.pendown()
   turtle.forward(100)
   turtle.left(90)
   coun=coun-1

   
turtle.undo()
turtle.undo()
turtle.goto(-250,-250)
turtle.left(90)

turtle.forward(500)
turtle.exitonclick()

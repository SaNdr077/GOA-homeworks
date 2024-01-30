from turtle import *

# we want to paint a house

width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door
forward (70)
color("yellow")
begin_fill()
left(90)
forward(120)    #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

#drawing a roof
penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right (150)
forward(200)
left(120)
forward(200)
end_fill()

#drawing the left windows
penup()
goto(0, 70)
pendown()
color("blue")
begin_fill()
right(240)
forward(30)
left(90)
forward(40)
left(90)
forward(30)
left(90)
forward(40)
end_fill()

#drawing the right windows
penup()
goto(200, 70)
pendown()
color("blue")
begin_fill()
left(270)
forward(30)
right(90)
forward(40)
right(90)
forward(30)
right(90)
forward(40)
end_fill()


exitonclick()
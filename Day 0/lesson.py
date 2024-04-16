from turtle import *

width(3)
speed(20)
#we went to paint a home

color("brown")
begin_fill()
forward(100)
left(90)

forward(100)
left(90)

forward(100)
left(90)

forward(100)
left(90)
end_fill()
#end  of squere

#drawing door


forward(35)
color("orange")
begin_fill()
left(90)
forward(50)
right(90)
forward(30)
right(90)
forward(50)
end_fill()
#end drawing a door


penup()
goto(100,  100)
pendown()
color("green")
begin_fill()
right(150)
forward(100)
left(120)
forward(100)
end_fill()



#drawing window

penup()
goto(40,  70)
pendown()
color("purple")
begin_fill()
right(60)
forward(25)
right(90)
forward(25)
right(90)
forward(25)
right(90)
forward(25)

penup()
goto(90,  70)
pendown()
right(90)
forward(25)
right(90)
forward(25)
right(90)
forward(25)
right(90)
forward(25)
end_fill()












exitonclick()
from turtle import  *


shape("turtle")
speed(2)
width(5)
#we went tu paint a home
color("green")

forward(100)
begin_fill()
left(90)

forward(100)
left(90)

forward(100)
left(90)

forward(100)
left(90)
end_fill()
#end



#drawing dor

forward(40)
color("brown")
begin_fill()
left(90)
forward(45)
right(90)
forward(30)
right(90)
forward(45)
end_fill()
#end of drawing door

#drawing roof

penup()
goto(100,  100)
pendown()
color("red")
begin_fill()
right(150)
forward(100)
left(120)
forward(100)
end_fill()
#end of drawing roof

#drawing window

penup()
goto(40, 70)
color("purple")
begin_fill()
left(90)
right(150)
pendown()
forward(20)
left(90)
right(180)
forward(20)
left(90)
right(180)
forward(20)
left(90)
right(180)
forward(20)
end_fill()


penup()
goto(90,  70)
color("purple")
begin_fill()
left(90)
right(180)
pendown()
forward(20)
left(90)
right(180)
forward(20)
left(90)
right(180)
forward(20)
left(90)
right(180)
forward(20)
end_fill()
#end of drawing window


exitonclick()
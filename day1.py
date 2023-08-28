from turtle import *
#we want to paint a house

#step1 : one draw a square
#speed(30)
shape("turtle")
width(7)
begin_fill()
color("silver")
forward (200)
left (90)

forward (200)
left(90)

forward(200)
left(90)

forward (200)
left(90)
end_fill()
#end of square

#draw a door
forward(75)
begin_fill()
color("brown")
left(90)
forward(100)
right(90)
forward(50)
right(90)
forward(100)
end_fill()

#roof
penup()
goto(200,200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#window
penup()
goto(20,125)
pendown()
color("black")
right(150)
forward(60)
right(90)
forward(35)
right(90)
forward(60)
right(90)
forward(35)

penup()
goto(83, 125)
pendown()

right(90)
forward(60)
right(90)
forward(35)
right(90)
forward(60)
right(90)
forward(35)

penup()
goto(180, 125)
pendown()

forward(35)
right(90)
forward(60)
right(90)
forward(35)
right(90)
forward(60)


#1stfloor
penup()
goto(20,20)
pendown()
right(180)
forward(80)
right(90)
forward(35)
right(90)
forward(80)
right(90)
forward(35)

penup()
goto(180,20)
pendown()

forward(35)
right(90)
forward(80)
right(90)
forward(35)
right(90)
forward(80)


penup()
goto(200,200)
pendown()
color("blue")
begin_fill()
left(135)
forward(35)
right(135)
forward(200)
right(45)
forward(35)
end_fill()
penup()
goto(100,373)
pendown()

begin_fill()
right(180)
forward(35)
right(105)
forward(200)
end_fill()
#forward(200)

#doorhandle
penup()
goto(79,50)
pendown()

color("black")
forward(5)



exitonclick()
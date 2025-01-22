import turtle as t 
t.bgcolor ("#89CFF0") # background color 

t.width (4)
t.speed(0)
t.color("#F4C2C2", "white") 
t.begin_fill()
for y in range (36): #bottom circle
    t.forward (20)
    t.right(10)
t.end_fill ()


t.color("#F4C2C2", "white") 
t.begin_fill()
for y in range (36): #middle circle
    t.forward (15)
    t.left(10)
t.end_fill ()

    
t.penup()
t.goto(0,172)
t.pendown()    
t.color("#F4C2C2", "white")
t.begin_fill()
for x in range (36): #top circle
    t.forward(10)
    t.left(10)
t.end_fill()

#left eye
t.penup()
t.goto(-20,232)
t.pendown()
t.color("black")
t.begin_fill()
t.circle(10)
t.end_fill ()

#right eye 
t.penup ()
t.goto (30,232)
t.pendown()
t.color("black")
t.begin_fill()
t.circle(10)
t.end_fill()

#smile
t.penup()
t.goto(-15,202)
t.pendown()
t.setheading(270)
t.circle(20,180)

t.penup()
t.goto(-15,202)
t.pendown()
t.setheading(270)
t.circle(20,180)
# right arm
t.penup()
t.goto(95,100)
t.pendown()
t.setheading(300)
t.forward(90)
# left arm
t.penup()
t.goto(-80,100)
t.pendown()
t.setheading(240)
t.forward(90)
t.mainloop ()# to hold the turtle screen 

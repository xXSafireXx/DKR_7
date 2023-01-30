from turtle import *
import turtle
import keyboard
j=1
def fractdraw(stp, rule, ang, dept, t):
   turtle.pencolor('white')
   if dept > 0:
      x = lambda: fractdraw(stp, "a", ang, dept - 1, t)
      y = lambda: fractdraw(stp, "b", ang, dept - 1, t)
      left = lambda: t.left(ang)
      right = lambda: t.right(ang)
      forward = lambda: t.forward(stp)
      if rule == "a":
        left(); y(); forward(); right(); x(); forward(); x(); right(); forward(); y(); left();
      if rule == "b":
        right(); x(); forward(); left(); y(); forward(); y(); left(); forward(); x(); right();
def DKR(j):
 screen = Screen()
 shape = Shape("compound")        
 turtle=Turtle(visible=False)
 turtle.pencolor('white')
 turtle.ht()
 turtle.speed(0)
 turtle.begin_poly()
 fractdraw(5, "a", 90,j, turtle)
 turtle.end_poly()
 shape.addcomponent(turtle.get_poly(),"white","black")
 screen.register_shape(str(j),shape)
 x=-200
 y=200
 z=1
 turtle = Turtle(visible=False)
 peano=Turtle(shape=str(j))
 peano.penup()
 peano.speed("slowest")
 peano.resizemode("пользователь")
 while keyboard.is_pressed('enter')!=True:
        if keyboard.is_pressed('1'):
            screen.clear()
            j=1
            DKR(j)
            exit
        if keyboard.is_pressed('2'):
            screen.clear()
            j=2
            DKR(j)
            exit
        if keyboard.is_pressed('3'):
            screen.clear()
            j=3
            DKR(j)
            exit
        if keyboard.is_pressed('4'):
            screen.clear()
            j=4
            DKR(j)
            exit
        if keyboard.is_pressed('5'):
            screen.clear()
            j=5
            DKR(j)
            exit
        if keyboard.is_pressed('D'):
            x=x+10
        if keyboard.is_pressed('W'):
            y=y+10
        if keyboard.is_pressed('S'):
            y=y-10
        if keyboard.is_pressed('A'):
            x=x-10
        if keyboard.is_pressed('Z'):
             z=z+1
        if (keyboard.is_pressed('C')) and (z>1):
             z=z-1
        peano.shapesize(z,z,z )
        peano.goto(x,y)
        peano.shapesize()
 screen.exitonclick()
 return(j)
DKR(j)

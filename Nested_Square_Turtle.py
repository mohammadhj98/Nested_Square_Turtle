#Mohammad HajeForosh

import turtle
import math

def square(length):    
    for i in range(4): 
            my_pen.forward(length) 
            my_pen.left(90)

tut = turtle.Screen() 

tut.bgcolor("green") 

tut.title("Turtle") 
my_pen = turtle.Turtle()
turtle.setworldcoordinates(-100, -100, 400, 400)

my_pen.pensize(3)        
my_pen.color("orange") 
tut = turtle.Screen()
#Square 1
length = 300 
square(length)
#Square 2
length =length//2    #150
my_pen.goto(length,0)
my_pen.left(45)
new_length=math.sqrt((length)**2+(length)**2)
square(new_length) 

#Square 3
my_pen.goto(length//2,length//2)    #(75,75) 
my_pen.right(45)
square(length)
#Square 4
my_pen.goto(length,length//2)   #(150,75)
my_pen.left(45)
length =length//2 #75
new_length=math.sqrt((length)**2+(length)**2)
square(new_length)
##########
my_pen.right(135)
my_pen.forward(length)


my_pen.goto(0,0) 
my_pen.left(135)
my_pen.forward(new_length)



my_pen.goto(length,length*2)
my_pen.left(135)
my_pen.forward(length)
my_pen.up()

my_pen.goto(0,length*4)
my_pen.left(135)
my_pen.down()
my_pen.forward(new_length)


my_pen.goto(length*2,length*3)
my_pen.left(135)
my_pen.forward(length)


my_pen.goto(length*4,length*4)
my_pen.left(135)
my_pen.forward(new_length)

my_pen.goto(length*4,length*2)
my_pen.right(45)
my_pen.forward(length)
my_pen.up()

my_pen.goto(length*3,length)
my_pen.left(135)
my_pen.down()
my_pen.forward(new_length)
my_pen.up()


my_pen.goto(200,-90)
my_pen.down()
my_pen._write("Mohammad HajeForosh", "right","Arial")
my_pen.up()
my_pen.setpos(500,-100)

 




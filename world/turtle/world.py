from random import randint, random
import turtle
import random
from world import obstacles

positions = []

pen = turtle.Turtle()
my_ninja = turtle.Turtle
pen.pencolor('red')
pen.speed(1000)
pen.left(180)
pen.penup()
pen.forward(100)
pen.pendown()
pen.right(90)
pen.forward(200)
pen.right(90)
pen.forward(200)
pen.right(90)
pen.forward(400)
pen.right(90)
pen.forward(200)
pen.right(90)
pen.forward(200)
pen.right(90)
pen.penup()
pen.forward(100)
pen.left(90)
pen.pencolor('black')

real_ninja = turtle
def place_obstacle(position):
    real_ninja.ht()
    real_ninja.pencolor('red')
    real_ninja.pensize(1)
    real_ninja.speed(1000)
    real_ninja.penup()
    real_ninja.goto(position)
    real_ninja.pendown()
    real_ninja.forward(4)
    real_ninja.left(90)
    real_ninja.forward(4)
    real_ninja.left(90)
    real_ninja.forward(4)
    real_ninja.left(90)
    real_ninja.forward(4)
    real_ninja.left(90)
    real_ninja.penup()

for i in range(len(positions)): 
    place_obstacle((positions[i][0]))

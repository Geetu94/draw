import turtle
def drwaing(t, angle):
  length = 2
  for i in range(40):
    t.forward(length)
    t.right(angle)
    t.forward(length)
    t.right(angle)
    length = length + 5
wn = turtle.Screen()       
wn.bgcolor("pink")
guido = turtle.Turtle()   
guido.color('blue')
guido = turtle.Turtle()    
guido.color('blue')
drwaing(guido, 90)
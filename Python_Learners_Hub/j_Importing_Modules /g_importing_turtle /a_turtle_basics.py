import turtle as t
# t.penup()
# t.speed('slowest')
# t.bgcolor('Dodger blue')
# t.shape('turtle')
# t.setheading(0)
# t.forward(80)
# t.forward(100)
# t.left(90)
# t.forward(50)
# t.

def Rectangle(horizontal, vertical, color):
    t.pendown()
    t.pensize(1)
    t.color(color)
    t.begin_fill()
    for counter in range (1,3):
        t.forward(horizontal)
        t.right(90)
        t.forward(vertical)
        t.right(90)
    # t.end_fill()
    t.penup()

'''
turtle.shape("arrow")      "arrow" (default): Standard arrow shape.
turtle.shape("turtle")     "turtle": A small turtle.
turtle.shape("circle")      "circle": A circle.
turtle.shape("square")      "square": A square.
turtle.shape("triangle")    "triangle": An equilateral triangle.
turtle.shape("classic")     "classic": The classic turtle shape.

'''
    
def main():
    t.shape("circle")
    t.setheading(0)
    t.penup()
    t.speed("slowest")
    t.bgcolor("yellow")
    Rectangle(80,60,"black")
    return 0

def forward_triangle (length):
    t.forward(length)
    t.left(120)  # or turtle.right(120) for a different orientation
    t.forward(length)
    t.left(120)
    t.forward(length)
    return 0
    
def square(length):
    for i in range(4):
        t.forward(length)
        t.left(90)
    return 0

def rectangle(length, width):
    for i in range(2):
        t.forward(length)
        t.left(90)
        t.forward(width)
        t.left(90)
        return 0

def circle(radius):
    t.circle(radius)
    return 0

def pentagon(length):
    for i in range(5):
        t.forward(length)
        t.left(72)
    
def hexagon(length):
    for i in range(6):
        t.forward(length)
        t.left(60)

def octagon(length):
    for i in range(8):
        t.forward(length)
        t.left(45)
        return 0
    
def star(length):
    for i in range(5):
        t.forward(length)
        t.right(144)
        return 0

def spiral(length):
    for i in range(36):
        t.forward(length)
        t.right(10)
    length += i  # Increment to create a spiral effect


if __name__ == "__main__":
    main()
        

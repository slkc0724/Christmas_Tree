import turtle
turtle.shape("turtle")

def star(turtle, color, size, x, y):
	turtle.penup()
	turtle.goto(x,y)
	turtle.pendown()
	turtle.color(color)
	turtle.fillcolor(color)
	turtle.begin_fill()
	for i in range(5):
		turtle.right(75)
		turtle.forward(size * 2)
		turtle.left(75)
		turtle.forward(size * 2)
		turtle.right(72)
	turtle.end_fill()

def tree_first(turtle, color):
	turtle.penup()
	turtle.left(89.5)
	turtle.backward(56)
	turtle.left(180)
	turtle.pendown()
	turtle.color(color)
	turtle.fillcolor(color)

def tree_second(turtle):
	size = 50
	for i in range(3):
		turtle.begin_fill()
		turtle.right(30)
		for i in range(3):
			turtle.forward(size * 3)
			turtle.left(120)
		turtle.end_fill()
		turtle.left(30)
		turtle.penup()
		turtle.forward(88)
		turtle.pendown()
		size = (size / 2) * 3

def tree_base(turtle, color, size):
	turtle.forward(205)
	turtle.pendown()
	turtle.color(color)
	turtle.fillcolor(color)
	turtle.pendown()
	turtle.begin_fill()
	turtle.left(90)
	turtle.forward(size / 2)
	turtle.right(90)
	turtle.forward((size / 2) * 3)
	turtle.right(90)
	turtle.forward(size)
	turtle.right(90)
	turtle.forward((size / 2) * 3)
	turtle.right(90)
	turtle.forward(size / 2)
	turtle.end_fill()
	turtle.penup()
	turtle.color("red")
	turtle.right(90)
	turtle.forward(size)
	turtle.right(90)
	turtle.forward(100)
	turtle.right(180)
	turtle.write("Merry", font = 1000)
	turtle.forward(size + 100)
	turtle.write("Christmas", font = 1000)
	turtle.hideturtle()

star(turtle, "yellow", 15, 0, 300)
tree_first(turtle, "green")
tree_second(turtle)
tree_base(turtle, "brown", 70)

turtle.done()
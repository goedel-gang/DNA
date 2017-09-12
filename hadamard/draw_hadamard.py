import sys, turtle
from matrices import Matrix

t = turtle.Turtle()
t.speed(0)
t.penup()
t.hideturtle()

s = turtle.Screen()

def square(x, y, base):
	t.setpos(x, y)
	t.fill(True)
	t.setheading(0)

	for _ in range(4):
		t.forward(base)
		t.left(90)

#the length of the codes will be 2 ** size

size = int(sys.argv[1])

base = int(sys.argv[2])

try:

	H = Matrix([[1]])

	while size:
		size -= 1

		H = H.append_right(H).append_under(H.append_right(H * -1))

	H = H.append_under(H * -1)

	for y, row in enumerate(H):
		for x, i in enumerate(row):
			if i == 1:
				square(x * base - len(H[0]) * base / 2 , y * base - len(H) * base / 2, base)

	raw_input()

except KeyboardInterrupt:
	pass

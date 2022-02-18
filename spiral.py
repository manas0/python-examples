import math
import turtle


bob = turtle.Turtle()
bob.lt(90)
r1 = 0
r2 = 1
for i in range(360):	
	bob.fd(100)
	bob.lt(math.degrees(math.atan(1/math.sqrt(i+1))))

turtle.mainloop()



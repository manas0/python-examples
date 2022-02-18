import math
import turtle



def Koch(t, x):
	if(x<=1):
		t.fd(3*x)
		return
	
	Koch(t, (int)(x/3))

	t.lt(60)
	Koch(t, (int)(x/3))
	
	t.rt(120)
	Koch(t, (int)(x/3))
		
	t.lt(60)
	Koch(t, (int)(x/3))
	

def snowflake(t, x):
	Koch(t,x)
	t.rt(120)
	Koch(t, x)
	t.rt(120)
	Koch(t, x)
	t.rt(120)
	
	

def draw(t, length, n):
	if n == 0:
		return
	angle = 50
	t.fd(length*n)
	t.lt(angle)
	draw(t, length, n-1)
	t.rt(2*angle)
	draw(t, length, n-1)
	t.lt(angle)
	t.bk(length*n)

bob = turtle.Turtle()
snowflake(bob,100)
turtle.mainloop()



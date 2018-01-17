import math
def square_area(n):
	m=n*n
	return m

def circle_area(r):
	m=2*math.pi*r
	return m

def sphere_area(r):
	m=(4/3)*math.pi*(r**3)
	return m

m=int(input("Enter the length:"))
n=int(input("Enter the radius:"))

print("The area of square is:",square_area(m))
print("The area of circle is:",circle_area(n))
print("The area of sphere is:",sphere_area(n))



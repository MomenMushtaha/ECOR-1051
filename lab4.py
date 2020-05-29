#Momin Mushtaha
#101114546

from math import pi,sqrt,sin

#ex1

def area_of_disk(radius):
   """
       area_of_disk() takes the parameter as the radius 
       of the circle, then it returns the disk area
       pi * radius^2
   """
   return pow(pi * radius,2)

#ex2

def distance(x1,y1,x2,y2):
   """
       takes x1,y1 and x2,y2. then it
       returns the distance between the points
       
   """
   return sqrt(pow((x2-x1),2) + pow((y2-y1),2))

#ex3

def area_of_circle(xc,yc,xp,yp):
   """
       the function takes a point x and y cordinates from the centre
       of the circle point xc and point yc. and another point x and y
       coridinates point xp and point yp, and then it returns the area
       of a circle
   """
   #camputes the difference(distance) between center point(xc,yc) and point(xp,yp)
   #computes area of the distance found afterwards.
   return area_of_disk(distance(xc,yc,xp,yp))


#ex4

def height(length, angle):
   """
   takes the length and the angle of the ladder
   and returns the hight of it using sin function
    """
   # returns height reached by ladder by ground for that use sin function
   return length * sin(angle)   



#calling functions
print(area_of_disk(10))

print(distance(200,50,40,10))

print(area_of_circle(200,50,40,10))

print(height(50, 70))
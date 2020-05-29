#Momin Mushtaha
#101114546

import math


#function definitions 

#ex1
def area_of_disk(radius):
     return math.pi * radius ** 2 

def area_of_ring(outer, inner):   
     return area_of_disk(outer) - area_of_disk(inner)

#ex2
LITRES_PER_GALLON = 4.54609 
KMS_PER_MILE = 1.60934 

def convert_to_litres_per_100_km(mpg):
     return (LITRES_PER_GALLON) / (mpg * KMS_PER_MILE)

#ex3
def accumulated_amount(principal, rate, n, time):
     return principal*((1+(rate/n))**(n*time))
     

#ex4
def area_of_cone(height, radius):
     return math.pi*radius*(math.sqrt((radius**2+height**2)))



#calls of functions 


#ex1 function calls

area = area_of_disk(5) 
print(area)
area = area_of_disk(5.0) 
print(area)
area = area_of_ring(10, 5)
print(area)
area = area_of_ring(10.0, 5.0) 
print(area)


#ex2 function calls 

print(convert_to_litres_per_100_km(32))
print(convert_to_litres_per_100_km(32.0))
#works for real numbers and integers 
#print(convert_to_litres_per_100_km(0))
#results in an error with 0


#ex3 function calls 

#if n is 0 it will result in an error
#print(accumulated_amount(1500, 4, 0, 8))
#if rate is 0 the principal is returned regardless of the other values
print(accumulated_amount(1500, 0, 3, 8))
#if principal is 0, 0 is returned regardless of the other values
print(accumulated_amount(0, 0.08, 3, 8))
print(accumulated_amount(1500, 0.08, 3, 8))


#ex4 function calls 

print((area_of_cone(6,2)))
print((area_of_cone(7,3)))
print((area_of_cone(9,6)))
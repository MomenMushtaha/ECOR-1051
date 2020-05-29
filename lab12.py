#Momin Mushtaha
#101114546

# ECOR 1051 Lab 12 File: lab12-linearRegression.py
from typing import Set, Tuple

# See Practical Programming, Chapter 8, section Type Annotations For Lists,
# and Chapter 11, first paragraph of section Creating New Type Annotations. 

#ex2
def get_points(filename:str) -> Set[Tuple[float, float]]:
    """Return a set of (x, y) points.
    
    >>> get_points()
    [(1.0, 5.0), (2.0, 8.0), (3.5, 12.5) ]
    # The order of the points may vary, depending on how sets are implemented
    # in the version of Python you're using.
    """
    infile = open (filename,'r')
    s = infile.readlines()
    z= [string.strip() for string in s]
    tuple_list=[]
    for i in range (len(z)):
        string = z[i].split()
        tuple_list.append((float(string[0]),float(string[1])))
    return tuple_list

#ex3 & ex4
def fit_line_to_points(points: Set[Tuple[float, float]]) -> Tuple[float, float]: 
    sumx = 0
    sumy = 0
    sumxx = 0
    sumxy = 0
    n = len(get_points('lab12-data.txt'))
    for x,y in get_points('lab12-data.txt'):
        sumx += x
        sumxx += (x**2)          
        sumy += y
        sumxy += (x*y)     
        m = ((sumx*sumy) - (n*sumxy)) / ((sumx*sumx) - (n*sumxx))
        b = ((sumx*sumxy)-(sumxx*sumy)) / ((sumx*sumx)-(n*sumxx))
    return ('the best fit line is y = ' + str(m) + ' x + ' + str(b))

#ex5
def read_points(filename: str) -> Set[Tuple[float, float]]:
    infile = open ('lab12-data.txt','r')
    return infile.read()
    

#calling functions
print ("ex1")
print (get_points('lab12-data.txt'))

print("ex3 & ex4")
print (fit_line_to_points(get_points('lab12-data.txt')))

print("ex7")
print (read_points('lab12-data'))
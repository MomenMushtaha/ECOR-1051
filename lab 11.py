#Momin Mushtaha
#101114546

#ex1
"""step1"""
#>>> point1 = [1.0, 2.0]
#>>> point1
#[1.0, 2.0]

#>>> point1.append(3.0)
#>>> point1
#[1.0, 2.0, 3.0]

"""
#step2
"""
#>>> point1.pop(0)
#1.0
#>>> point1
#[2.0, 3.0]
"""
"""
#>>> point1.pop()
#3.0
#>>> point1
#[2.0]
"""
#step3
"""
#>>> point1 = (1.0, 2.0)
#>>> type(point1)
#<class 'tuple'>
#>>> point1
#(1.0, 2.0)
"""
#step4
"""
#>>> x = point1[0]
#>>> y = point1[1]
#>>> x
#1.0
#>>> y
#2.0

#>>> point2 = (4.0, 6.0)
#>>> x,y = point2
#>>> x
#4.0
#>>> y
#6.0
"""
#step5
"""
#>>> point2[0] = 2.0
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#TypeError: 'tuple' object does not support item assignment

#>>> point2.append(4.0)
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#AttributeError: 'tuple' object has no attribute 'append'

#>>> point2.pop(0)
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#AttributeError: 'tuple' object has no attribute 'pop'

"""step6"""

#>>> points = [(1.0, 5.0), (2.0, 8.0), (3.5, 12.5)]
#>>> points[0]
#(1.0, 5.0)
#>>> points[1]
#(2.0, 8.0)
#>>> points[2]
#(3.5, 12.5)


#ex2
def average (list)->list:
    """The function returns a new list of tuples. The three numbers 
    in each tuple are the integer average values of the numbers
    in the tuple at the same position in the original list
    >>>average([(27, 219, 134),(27, 219, 134),(27, 219, 134)])
    [(126, 126, 126), (126, 126, 126), (126, 126, 126)]
    """
    newlist = []
    for elem in list:
        avg = sum(elem) // 3
        #elem = elem+1
        newlist.append((avg,)*3)
    return(newlist)

#ex3
#step_1
"""
points = {(1.0, 2.0), (4.0, 6.0), (10.0, -2.0)}
>>> points
{(1.0, 2.0), (10.0, -2.0), (4.0, 6.0)}
"""
"""
>>>point1 = (1.0, 2.0)
>>> point2 = (4.0, 6.0)
>>> point3 = (10.0, -2.0)
>>> points = {point1, point2, point3}
>>> points
{(1.0, 2.0), (10.0, -2.0), (4.0, 6.0)}
"""
"""
>>> points= set()
>>> points.add(point1)
>>> points.add(point2)
>>> points.add(point3)
>>> points
{(1.0, 2.0), (10.0, -2.0), (4.0, 6.0)}
"""
"""
>>> points= set()
>>> points.add(point1)
>>> points.add(point2)
>>> points.add(point3)
>>> points
{(1.0, 2.0), (10.0, -2.0), (4.0, 6.0)}
"""
#step2
"""
>>> points= set()
>>> points.add(point1)
>>> points.add(point2)
>>> points.add(point3)
>>> points
{(1.0, 2.0), (10.0, -2.0), (4.0, 6.0)}
>>> points.add(point2)
>>> points
{(1.0, 2.0), (10.0, -2.0), (4.0, 6.0)}
"""
#step3
"""
>>> points [0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'set' object is not subscriptable
"""
#step4
"""
points = {(1.0, 2.0), (4.0, 6.0), (10.0, -2.0)} 
for point in points:
    print (point)
(1.0, 2.0)
(10.0, -2.0)
(4.0, 6.0)
"""

#ex4
def sum_x(set):
    """the function returns the sum of the x coordinates:
    ​X0+X1+X2+X3+......Xn+1. 
    >>>sum_x({(10,2), (10,3), (6,4)})
    26
    """
    total = 0
    for x,_ in set:
        total += x
    return total

#function calls
print("ex2")
print(average([(27, 219, 134),(27, 219, 134),(27, 219, 134)]))

print("ex4")
print(sum_x({(10,2), (10,3), (6,4)}))
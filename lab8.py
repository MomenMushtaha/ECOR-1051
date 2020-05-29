#Momin Mushtaha
#101114546
#ex1
def first_last6(list):
  """ True if a 6 is the first element and
      the last element or 6 is the first element or 6 is the last element
      if none the function returns False.
     >>list1 = [6,2,2,2,2]
     >>print(first_last6(list1))
     >>True
     >>list2 = [1,1,1,4,2,3]
     >>print(first_last6(list2))
     >>False
     >>list3 = [3,5,6,7,6]
     >>print(first_last6(list3))
     >>True
     >>list4 = [6,7,2,2,6]
     >>print(first_last6(list4))
     >>True
  """
  if ( list[0] == 6 and list[-1] == 6 ) or list[0] == 6 or list[-1] == 6:
    return True
#could be shortened if the question did not specify the False part
  return False




#ex2
def same_first_last(list):
  '''
  returns True if the list is not empty and if the first and last elements are equal.
  Otherwise, the function returns False.
  >>print(same_first_last([1]))
  True
  >>print(same_first_last([]))
  False
  '''
  if(len(list) > 0 and (list[0] == list[-1])):
    return True
  else:
    #could be shortened if not specified 
    return False
    


#ex3

def make_pi():
  '''
  returns first 3 digis of pi
  >>print(make_pi())
  [3,1,4]
  '''
  return [3,1,4]

#ex4

def common_end(list1, list2):
  ''' 
  if one of the ends in both lists are common
  return true 
  if both ends are common return false
  >>print(common_end([1,2,3],[4,3]))
  True
  >>print(common_end([1,2,3],[1,4]))
  True
  '''
  return (list1[0]==list2[0]) or (list1[-1]==list2[-1])


#ex5
def sum3(lstt):
  '''
  returns the sum of the three lists 
  >> print(sum3([1, 2, 3]))
  >> 6
  '''
  list1 = lstt[0]
  list2 = lstt[1]
  list3 = lstt[2]
  return list1 + list2 + list3



#ex6
def rotate_left3(lst):   
  '''
  rotates the list to the left
  >> print(rotate_left3([1,2,3]))
  >> [1,2,0]
  '''
  return [lst[1], lst[2], lst[0]]


#ex7
def reverse3(lst):
  '''
  returns in reverse order
  >> print(reverse3([1, 2, 3]))
  >> [3,2,1]
  '''
  return [lst[2], lst[1], lst[0]]

#ex8
def max_end3(lstt):
  '''
  The function determines whether the first element of the last element of
  a 3 element list is the larger and creates a new list with that value only
  >>print(max_end3([0,1,2]))
  >>[2,2,2]
  '''
  if lstt[0] > lstt[2]:
      return [lstt[0], lstt[0], lstt[0]]
  else:
      return [lstt[2], lstt[2], lstt[2]]



#ex9
def sum2(lst):
  '''
  sums the first 2 integers of a list
  
  >> print(sum2([1,2,3]))
  >> 3
  '''

  if((len(lst))<=1):
    #if empty or only has one element it returns 0
    return 0
  else:
    return lst[0]+lst[1]
  


#ex10
def middle_way(list1,list2):
  '''
  Return a list containing middle elements of
  two list
  >>>print(middle_way([1,2,3],[4,5,6]))
  [2,5]
  '''
  return [list1[1],list2[1]]



#ex11
def make_ends(lst):
  '''
  takes the first and last elements of a list and 
  returns a new list with them
  >> print(make_ends([1,2,3]))
  >>[1,3]
  
  '''
  return [lst[0],lst[-1]]

#ex12

def has23(lstt):
  '''
  checks if the list passed has 2 and 3 it it
  >>print(has23([1,2,3])
  >>True
  '''
  return (2 in lstt) or (3 in lstt)




#testing 
print("ex1")


print(first_last6([6,2,2,2,2]))
print(first_last6([1,1,1,4,2,3]))
print(first_last6([3,5,6,7,6]))
print(first_last6([6,7,2,2,6]))

print("ex2")

print(same_first_last([1]))
print(same_first_last([]))
print(same_first_last([1, 1, 3]))
print(same_first_last([1, 1, 2, 2]))


print("ex3")

print(make_pi())

print("ex4")

print(common_end([1,4,4],[4,4]))
print(common_end([1,2,4],[1,2]))
print(common_end([1,2,3],[1,4,3]))
print(common_end([1,2,3],[4,6]))


print("ex5")

print(sum3([1, 2, 3]))
print(sum3([4, 4, 4]))
print(sum3([2, 2, -11]))

print("ex6")

print(rotate_left3([1,2,3]))

print("ex7")

print(reverse3([1, 2, 3]))
print(reverse3([3, 4, 1]))

print("ex8")

print(max_end3([1, 2, 3]))

print("ex9")

print(sum2([1,2,3]))

print("ex10")

print(middle_way([1,2,3],[4,5,6]))

print("ex11")

print(make_ends([1,2,3]))

print("ex12")

print(has23([1,2,3]))
print(has23([1,1]))
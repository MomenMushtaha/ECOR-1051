#Momin Mushtaha
#101114546


#example 1
def count_evens(lis):
    '''
     number of even integers
     in list given
    '''
    i= 0
    for number in lis:
        #for loop used in here
        if number % 2 == 0:
            i += 1
    #final result
    return i

#example 2
def big_diff(listtt):
    '''
    difference between the biggest and
    the smallest value 
    '''
    length_of_list=len(listtt)
    if(length_of_list < 2):
        return 0
    minimum=listtt[0]
    maximum=listtt[0]
    for q in listtt:
        if maximum<q:
            maximum=q
        if minimum>q:
            minimum=q
    return maximum-minimum
  
  
#example 3
def has22(this_list):
    '''
    returns true if 2 consecutive 2's are included 
    in list, othervise it returns false
    '''
    length=len(this_list)
    for i in range(length-1):
# checks condition
        if this_list[i] == 2 and this_list[i+1] == 2:
            return True
    return False


#example 4   
def centered_average(this_list):
    '''
    returns the average excluding the largest and the smallest integers
    '''
    #shortened 
    #better than a for loop
    return (sum(this_list) - max(this_list) - min(this_list)) / (len(this_list) - 2)   


#testing 
p=0
f=0
print("example 1")
actual = count_evens([5,2,3,3,7,2,7]) 
print("Testing count_evens([5,2,3,3,7,2,7])") 
print("Expected result: 2, Actual result:", actual)
if actual == 2:  
    print ("Test passed")
    p+=1
else: 
    print ("Test failed")
    f+=1
actual = count_evens([4,4,2,2,4,2,6]) 
print("Testing count_evens([4,4,2,2,4,2,6])") 
print("Expected result: 7, Actual result:", actual)
if actual == 7:  
    print ("Test passed")
    p+=1
else: 
    print ("Test failed")
    f+=1
    
print("example 2")
actual = big_diff([5,2,3,3,7,2,7]) 
print("Testing big_diff([5,2,3,3,7,2,7])") 
print("Expected result: 5, Actual result:", actual)
if actual == 5:  
    print ("Test passed")
    p+=1
else:
    print ("Test failed")
    f+=1
actual = big_diff([4,4,2,2,4,2,6]) 
print("Testing big_diff([4,4,2,2,4,2,6])") 
print("Expected result: 4, Actual result:", actual)
if actual == 4:  
    print ("Test passed")
    p+=1
else: 
    print ("Test failed")
    f+=1

print("example 3")
actual = has22([5,2,3,3,7,2,7]) 
print("Testing has22([5,2,3,3,7,2,7])") 
print("Expected result: False, Actual result:", actual)
if actual == False:  
    print ("Test passed")
    p+=1
else: 
    print ("Test failed")
    f+=1
actual = has22([4,4,2,2,4,2,6]) 
print("Testing has22([4,4,2,2,4,2,6])") 
print("Expected result: True, Actual result:", actual)
if actual == True:  
    print ("Test passed")
    p+=1
else: 
    print ("Test failed")
    f+=1
print("example 4")
actual = centered_average([5,2,3,3,7,2,7]) 
print("Testing centered_average([5,2,3,3,7,2,7])") 
print("Expected result: 4, Actual result:", actual)
if actual == 4:  
    print ("Test passed")
    p+=1
else: 
    print ("Test failed")
    f+=1
actual = centered_average([4,4,2,2,4,2,6]) 
print("Testing centered_average([4,4,2,2,4,2,6])") 
print("Expected result: 3.2, Actual result:", actual)
if actual == 3.2:  
    print ("Test passed")
    p+=1
else: 
    print ("Test failed")
    f+=1
    
print(p,'tests passed')
print(f,'tests failed')
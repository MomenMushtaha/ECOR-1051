#Momin Mushtaha
#101114546

#ex1
def bank_statement(list)-> list:
    """The function returns a new list of three numbers: the first will be
    the sum of the deposits, the second (a negative number) will be
    the sum of the withdrawals, and the third will be 
    the current account balance.
    >>>bank_statement([1,2,3,-1,-2,-3])
    [6, -6, 0]
    >>>bank_statement([1,2,-1])
    [3, -1, 2]
    """
    w=0
    d=0
    i=0
    for i in list: 
        if i>0:    
            d +=i
        else:
            w += i
    return ([d,w, d + w])

#ex2
def divisor(n:int)->list:
    """it takes a positive integer n and returns a list of factors
    of the integer
    >>>divisor(6)
    [1,2,3,6]
    """ 
    factors = []
    for i in range(1,n+1):
        if(n%i==0):
            factors += [i]
    return factors  

#ex3
def reverse(list):
    """The function returns a new list that contains all the elements
    of the original list in reverse order
    >>>reverse([1,2,3,4])
    [4, 3, 2, 1]
    """
    length = len(list)
    x = length
    newlist = [None]*length
    for i in list:
        x = x - 1
        newlist[x] = i
    return newlist


#print statements
print ("ex1")
print (bank_statement([1,2,3,-1,-2,-3]))     
print (bank_statement([1,2,-1]))

print ("ex2")
print(divisor(6))

print ("ex3")
print(reverse([4,2,3,2]))
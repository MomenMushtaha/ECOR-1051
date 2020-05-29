#Momin Mushtaha
#101114546

#ex1
def bakers_party(number_of_pastries,weekend):
   '''
   if pastries are between 40 and 60 and its not a weekend it returns true
   if pastries are above 40 and its a weekend it return true
   '''
   #constants
   UPPER_BOND=60
   LOWER_BOND=40
   if (weekend and number_of_pastries>=LOWER_BOND):
        #first condition
      return True 
   elif (weekend!=True and number_of_pastries>=LOWER_BOND and number_of_pastries<=UPPER_BOND):
        #second condition
      return True
   else: 
        #if none
      return False

#ex2
def squirrel_play(temperature, summer):
   '''
   returns true if it is not summer and the temperature is between 60 and 90 
   or returns true if it is summer and the temperature is between 60 and 100
   '''
   UPPER_BOND=90#constants
   LOWER_BOND=60   
   if (summer==False and temperature>=LOWER_BOND and temperature<=UPPER_BOND):
        #fist condition
      return True 
   elif (summer and temperature>=LOWER_BOND and temperature<=UPPER_BOND+10):
        #second condition
      return True 
   else:
        #if none
      return False

#ex3
def great_42(a,b):
   '''
   return true if a or b or a + b or a-b equals 42
   '''
   #can be shortened by on return statement
   return (a==42 or b==42 or a+b==42 or abs(a-b)==42)
        
    

#ex4
def blackjack(a,b):
    """
    takes values a,b and find the closest to 21 but lower than 21
    if both values are greater than 22 function returns value 0.
    """    
    TWENTY_ONE=21
    if(a<=TWENTY_ONE and b<=TWENTY_ONE):
        if(a<b):
            return b
        #first condition
        else:
            return a
        #second condition
        return a
    elif(a<=TWENTY_ONE and b>TWENTY_ONE):
        #if b is bigger than 21
        return a
    elif(b<=TWENTY_ONE and a>TWENTY_ONE):
        #if a is bigger than 21
        return b
    else:
        # if none return 0
        return 0





#ex5
def sum_uniques(a, b, c):
    """
    the sum of a, b, c with removing any duplicates
    """
    sum = 0
    if (a != b and a != c):
        #1st condition
        sum =sum+a
    if (b != a and b !=c):
        #2nd condition
        sum =sum+b
    if (c!=a and c!=b):
        #3rd condition
        sum =sum+c
    return sum


#checking for various conditions
print("ex1")
print(bakers_party(45,False));
print(bakers_party(65,True));
print(bakers_party(30,True));
print(bakers_party(35,False));
print("ex2")
print(squirrel_play(70, True))
print(squirrel_play(100, True))
print(squirrel_play(70, False))
print(squirrel_play(50, True))
print("ex3")
print(great_42(5,40))
print(great_42(4,50))
print(great_42(42,3))
print(great_42(1,42))
print(great_42(56,-30))
print("ex4")
print(blackjack(21,17))
print(blackjack(10,12))
print(blackjack(22,21))
print(blackjack(20,18))
print("ex5")
print(sum_uniques(2, 2, 1))
print(sum_uniques(3, 1, 3))
print(sum_uniques(1, 1, 3))
print(sum_uniques(2, 2, 2))

#Momin Mushtaha
#101114546
def factorial(n: int) -> int:  
   """Return n! for positive values of n.
   >>> factorial(1)  
   1  
   >>> factorial(2)  
   2
   >>> factorial(3)
   6     
   >>> factorial(4) 
   24  
   """ 
   fact = 1 
   for i in range(2,n+1):
      fact = fact * n 
      return fact 
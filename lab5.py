#Momin Mushtaha 
#101114546
"""
ECOR 1051 Lab 5 Solution Template

Author: Momin Mushtaha
101114546

This file is to be used in conjunction with the detailed lab description for Lab 5
Use this file to enter your answers to the series of exercises you will complete.

==========

Exercise 1: Single or Double Quotes - Does it matter?

Example, "haven't" or '"Spam, spam, spam," he said.'

>>> type('Hello')
<class 'str'>
>>> type("goodbye")
<class 'str'>
>>> 'This is a string' 
'This is a string'
>>> "" (An empty string - type two quotes with no spaces between them.) 
''
>>> '"Spam, spam, spam," he said.'
'"Spam, spam, spam," he said.'
>>> "I haven't a clue"
"I haven't a clue"
>>> 'I haven't a clue' 
invalid syntax

Concluding Questions: Generally, either double or single quotes works well but can you give a scenario where one is better than the other?
when there is an apostrophie in the string use double quotes to eliminate confusion. 
when there is a quote inside the string use single quotes to eliminate confusion.

Exercise 2: What operations are permitted with values of type str?

When used with strings, + is the concatenation operator. 

>>> 'Hello, ' + 'world!'
Hello, world!
When used with strings, * is the replication operator.

>>> "Spam" * 3
SpamSpamSpam
>>> 3 * "Spam"
SpamSpamSpam
>>> "Spam" * 0
''
>>> "Spam" * -3
''
There are other operators to try now: - and /

>>> "Hello" - "He"
error
>>> 'Spam' / 3
error

Concluding Questions: What operators work with strings?  Does the order of operands matter?
depends if your using / operand or the - operand they dont work. but they work with the * operand and the + operand
no, the order doesnt matter

Exercise 3 : Understand the string representation

Is  the string '123' the same as the integer 123? 

>>> '123' + 456 
error
>>> '123' + '456'
'123456'
Concluding Question: When a string looks like a number, is it a number or a string?
a string 
"""
#ex4
def repeat(s: str, n: int) -> str:
 """ Return s repeated n times; if n is negative, return the
 empty string. 
2
 >>> repeat('yes', 4)
 'yesyesyesyes'
 >>> repeat('no', 0)
 ''
 >>> repeat('no', -2)
 ''
 >>> repeat('yesnomaybe', 3)
 'yesnomaybeyesnomaybeyesnomaybe'
 """
 return s*n
print(repeat('yesnomaybe', 3))

#ex5
def total_length(s1: str, s2: str) -> int:
 """ Return the sum of the lengths of s1 and s2.
 >>> total_length('yes', 'no')
 5
 >>> total_length('yes', '')
 3
 >>> total_length('YES!!!!', 'Noooooo')
 14
 """
 return len(s1)+len(s2)
  

#ex6
def replicate(string):
  """ replicate the input string with copies equevalent to its characters number
  >>> replicate("cham")
  'chamchamchamcham'
  >>> replicate("air")
  'airairair'
  >>> replicate('lw')
  lwlw
  """
  return len(string) * string


#testing
print(replicate('lw'))
print(repeat('yesnomaybe', 3))
print(total_length('yes', 'no'))

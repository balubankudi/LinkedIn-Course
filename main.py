

x = 100
y = 42

if x == 5:
    print("do five stuff")
elif x == 6:
    print("do six stuff")
else:
    print("do something else")

# Copyright 2009-2017 BHG http://bw.org/

words = ['one', 'two', 'three', 'four', 'five']

n = 0
while(n < 5):
    print(words[n])
    n += 1


# Copyright 2009-2017 BHG http://bw.org/

words = ['one', 'two', 'three', 'four', 'five']

for i in words:
    print(i)

# simple fibonacci series
# the sum of two elements defines the next set

a, b = 0, 1
while b < 1000:
    print(b, end=' ', flush=True)
    a, b = b, a + b

print()  # line ending

# Copyright 2009-2017 BHG http://bw.org/


def function(n):
    print(n)


function(12)

#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def isprime(n):
    if n <= 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    else:
        return True

  #in line 62 i don´t understand the use of Flush      
def list_primes():
    for n in range(100):
      if isprime(n):
        print(n,end=" ",flush=True)
    print()


list_primes()

n = 6
if isprime(n):
    print(f'{n} is prime')
else:
    print(f'{n} not prime')



#defining even numbers
def iseven(n):
    if n <= 1:
        return False
    for x in range(2, n):
        if n % x == 2:
            return False
    else:
        return True
        
def list_even():
    for n in range(100):
      if iseven(n):
        print(n,end=" ",flush=True)
    print()

list_even()


# knowing format

x = 7.8
print('x is {}'.format(x))
print(type(x))


x = [ 1, 2, 3, 4, 5 ]
x[2] = 42
#eventhough initially the amount of x[2] is supposed to be 3, it is changed in the next line
for i in x:
    print('i is {}'.format(i))


#a tuple is like a list except that it is inmutable so we use parenthesis instead of brackets. So the x[2]= 42 will not execute since the initially list is inmutable. See what happens next. it gives error. Conclusion: for inmutable use parenthesis over brackets
#x = ( 1, 2, 3, 4, 5 )
#x[2] = 42

#for i in x:
   # print('i is {}'.format(i))

#print a list of even numbers from 1 to 100 and later add them"
x = range (2, 101, 2)
for i in x:
  print(i)

x = range (2, 101, 2)
sum = 0
for i in x:
    sum += i 
print(sum)


#defining even numbers type 2
def iseven(n):
    if n <= 1:
        return False
    for x in range(1, n):
        if n % 2 == 0:
            return True
    else:
        return False
        
def list_even():
    for n in range(101):
      if iseven(n):
        print(n,end=" ",flush=True)
    print()

list_even()

def list_evensum():
  sum = 0
  for n in range(101):
    if iseven(n):
      sum += n 
  print(sum)

list_evensum()


#Conditional 
x = 2
if x == 0:
    print('zero true')
elif x == 1:
    print('one 1 true')
elif x == 2:
    print('elif 2 true')
elif x == 3:
    print('elif 3 true')
elif False:
    print('elif true')
else:
    print('neither true')

hungry = True
x = 'Feed the bear now!' if hungry else 'Do not feed the bear.'
print(x)

infectedwithcovid19 = True
x = 'stay at home!' if infectedwithcovid19 else 'still stay at home safe'
print(x)


#operators
x = 5
y = 3
z = x + y
z = -z

print(f'result is {z}')

#bitwise operators
x = 0x0a
y = 0x02
z = x | y

print(f'(hex) x is {x:02x}, y is {y:02x}, z is {z:02x}')
print(f'(bin) x is {x:08b}, y is {y:08b}, z is {z:08b}')
#boolean
a = True
b = False
x = ( 'bear', 'bunny', 'tree', 'sky', 'rain' )
y = 'bear'

if y in x:
    print('expression is true')
else:
    print('expression is false')

if y is x[0]:
    print('expression is true')
else:
    print('expression is false')

print(id(y))
print(id(x[0]))

#operator precedence: order in which orders are evaluates
#while loop
secret = 'swordfish'
pw = ''

#while pw != secret:
   # pw = input("What's the secret word? ")

#for loop
animals = ( 'bear', 'bunny', 'dog', 'cat', 'velociraptor' )

for pet in animals:
    print(pet)

animals = ( 'bear', 'bunny', 'dog', 'cat', 'velociraptor' )

for pet in range(5):
    print(pet)


secret = 'swordfish'
pw = ''
auth = False
count = 0
max_attempt = 5

#while pw != secret:
    #count += 1
    #if count > max_attempt: break
    #if count == 3: continue
    #pw = input(f"{count}: What's the secret word?")
#else:
   # auth = True
    
#print ("authorized" if auth else "Calling the FBI")
#normally the while function is built to be false and else is true

#defining functions

def main():
   x = kitten(5, 6, 7)
   print(x)

def kitten(a, b = 1, c = 0):
  print ("Meow")
  print (a, b, c)

if __name__ == '__main__': main()
#notabene: arguments without default should always be before arguement with default

def main():
   x = 5
   kitten (x)
   print(f"in main x is {x}")

def kitten(a):
  a = 3
  print ("Meow")
  print (a)

if __name__ == '__main__': main()
#this is what we call "call by value", and when you pass a variable to a f(x), the f(x) operates on a copy of the variable. the value is passed but not the object it self. A interger is not mutable, 

 #so this is important to understand: an integer is not mutable so it cannot change, so when you assign a new value to an integer, you're actually assigning an entirely different object to the name. The original integer is not changed, the name simply refers to a new object. Passing a value to a function acts exactly the same way. A reference to the object is passed and acts exactly like an assignment. So mutable objects may be changed, and those changes will be reflected in the caller. Immutable objects may not be changed. So function arguments in Python act exactly as assignments in Python, with all the quirks of Python's object model. For the most part, things will work as expected, but be careful with lists and other mutable objects.
#keyword arguments
def main():
    kitten(Buffy = 'meow', Zilla = 'grr', Angel = 'rawr')

def kitten(**kwargs):
    if len(kwargs):
        for k in kwargs:
            print('Kitten {} says {}'.format(k, kwargs[k]))
    else: print('Meow.')

if __name__ == '__main__': main()


#GENERATORS: INCLUSIVE RANGE
def main():
    for i in inclusive_range(25):
        print(i, end = ' ')
    print()

def inclusive_range(*args):
    numargs = len(args)
    start = 0
    step = 1
    
    # initialize parameters
    if numargs < 1:
        raise TypeError(f'expected at least 1 argument, got {numargs}')
    elif numargs == 1:
        stop = args[0]
    elif numargs == 2:
        (start, stop) = args
    elif numargs == 3:
        (start, stop, step) = args
    else: raise TypeError(f'expected at most 3 arguments, got {numargs}')

    # generator
    i = start
    while i <= stop:
        yield i
        i += step

if __name__ == '__main__': main()

def main():
    seq = range(11)
    print_list(seq)

def print_list(o):
    for x in o: print(x, end = ' ')
    print()

if __name__ == '__main__': main()

class RevStr(str):
    def __str__(self):
        return self[::-1]

def main():
    hello = RevStr('Hello, World.')
    print(hello)

if __name__ == '__main__': main()

print (chr(128406))

x = list(range(30))
print(x)


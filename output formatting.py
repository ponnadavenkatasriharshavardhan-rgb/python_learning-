'''

output formatting
-------------------

camma separation(,)
--------------------

name = 'harsha'
age = '23'
print('welcome',name,'age is',age)

f-string (doc-string)
-----------------------

name = 'harsha'
age = '23'
print('welcome',name,'age is',age)
print(f'welcome {name} age is {age} ')

%
----

%s -- all are accpectable

name = 'harsha'
age = '23'
print('name:%s'%name)

%d -- only digits

price = 89
print('name:%d'%price)

%f -- float

price = 89
print('name:%f'%price)

(dot).format()
----------------

name = 'sri'
age = 23
print('name:{}\nage:{}'.format(name,age))


statements
------------

conditions
------------

if
----
-- returns the statement if the condition is true 

age=int(input("enter your age:"))
if age>= 18:
    print(f"your age is {age} and eligable to vote")
    
if - else
-----------
-- else is the fall back statement , incasef condition is false then this else block will execute...

age=int(input("enter your age:"))
if age>= 18:
    print(f"your age is {age} and eligable to vote")
    
    
    
num = int(input("enter a number: "))
if num % 2 == 0:
    print(f'{num} is a even number')
else:
        print(f"{num} is a odd number")
        
          

vol_ = input('enter single letter:')
if vol_ in 'AEIOUaeiou':
    print(f'{vol_} is vol')
else:
        print(f'{vol} is con')
        

so = 'python'
do = so[::-1]
print(do)
if so[::-1] == so:
    print(f'{so} is a pali')
else:
     print(f'{so} not a pali')
     

year_ = int(input("enter a year:"))
if year_ % 4 == 0 and year_ % 100 != 0 or year_ % 400 == 0:
    print(f'{year_} is a leap')
else:
    print(f'{year_} not is a leap')


'''


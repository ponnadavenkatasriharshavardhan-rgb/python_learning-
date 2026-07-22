'''

input formatting
------------------

int   -- int(input())
-----

num=int(input('enter a num:'))
print(num+9)
print(type(num))

string      -- input()
----------

we =input('enter:')
print(type(we))

list
------

nums = list(map(int,input('enter nums:').split()))
print(nums)

nums = input('enter nums:').split()
print(nums)

nums = input('enter nums:').split()
print(nums)

nums = input('enter nums:').split()
print(nums)

tuple
-------

nums = tuple(map(int,input('enter nums:').split()))
print(nums)

nums = eval(input('enter nums:'))
print(type(nums))

***
time_ = input("enter 24 hrs colck:")
parts_ = time_.split(':')
hours_ = int(parts_[0]) - 12
print(hours_,':',parts_[1],'pm')
***



'''





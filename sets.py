'''

set
----
set is an unorderd collection
set do not allows duplicate values inside it..
set mutable..
set is represented in ()

do = {1,2,3,2}
print(do)

# creating a empty set
so = set()
print(type(so))

methods
--------

update
-------
use to add new value into set

syntax -- variable_name.update(itterable)

do = {1,2,3}
do.update([5,9])
print(do)

add
----
syntax -- variable_name.add(value)

do={1,2,3}
do.add('python')
print(do)

remove
-------
used  to del the value from the set , incase if the value is not present in the set will get the keyerror

syntax -- variable_name.remove(value)

do={1,2,3,4}
do.remove(4)
print(do)

discard
--------
used to del the value from the set , but never give any error incase value is not present inside the set....

syntax -- variable_name.discard(value)

do={1,2,3,}
do.discard(4)
print(do)

pop()
------
used to del the value but this pop() will take 0 arguments inside it

syntax -- variable_name.pop()

do={1,2,3,4}
do.pop()
print(do)

operations
------------
union
------
gives all sets value together but no duplicates

do={1,2,3}
so={3,4,5}
print(do|so)
print(do.union(so))

intersection
--------------
coomon va;ues in both sets

do={1,2,3}
so={3,4,5}
print(do&so)
print(do.intersection(so))

difference
------------




do={1,2,3}
so={3,4,5}
print(do-so)
print(do.difference(so))


type convertion
-----------------


int:string;float

string -- str()

num=9
print(type(num))
so=str(num)
print(type(so))

float --float()

num=9
print(type(num))
so = float(num)
print(so)
print(type(so))

float
-------
string -- str()

nums=8.67
print(type(nums))
all_ = str(nums)
print(type(all_))

integer -- int()

nums=8.67
print(type(nums))
all_ = int(nums)
print(all_)
print(type(all_))

string
-------

integer -- int

how = "67 rupp"
print(type(how))
who = int(how)
print(type(who))

how = "67"
print(type(how))
who = int(how)
print(type(who))

float -- float()

how = "67"
print(type(how))
who = float(how)
print(type(who))

list -- list

how = "1234"
print(type(how))
who = list(how)
print(who)
print(type(who))

tuple -- tuple()

how = "1234"
print(type(how))
who = tuple(how)
print(who)
print(type(who))

list
------
string -- str()

nums = [1,2,3,4]
print(type(nums))
all_n = str(nums)
print(type(all_n))

tuple  -- tuple()

nums = [1,2,3,4]
print(type(nums))
all_n = tuple(nums)
print(all_n)
print(type(all_n))

tuple
-------
list -- list()

nums = [1,2,3,4]
print(type(nums))
all_n = list(nums)
print(all_n)
print(type(all_n))

string -- str()

nums = [1,2,3,4]
print(type(nums))
all_n = str(nums)
print(all_n)
print(type(all_n))

(+)

num = 8
num_2 = 9
print(num+num_2)

any_ = 'python is a'
we = ' language'
print(any_ + we)


nums = [1,2]
all_ = [3,4]
print(nums + all_)

'''


num = 8
num_2 = 9
print(num+num_2)

any_ = 'python is a'
we = ' language'
print(any_ + we)


nums = [1,2]
all_ = [3,4]
print(nums + all_)

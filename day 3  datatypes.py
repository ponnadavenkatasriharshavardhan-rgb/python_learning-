'''

to find datatype -- type (variables_name)
to find memory -- id (variables_name)

  datatypes
--------------
int
-----
number =9
print(type(number))

output
-----------
<class 'int'>


float
-------
num = 89.45
print (type(num))

output
--------
<class 'float'>


string
--------
string is a sequence of char that are inclosed in ('',"")
string is a immutable

method
--------
replace ()
------------
used to replace old str with new str

syntax -- variable_name.replace('old_str','new_ str')

so = ' python is a language '
print(so)
print (so.replace ('python','java'))

output
--------
 python is a language 
 java is a language
 

join ()
--------
this method will add the new char after every sub-string

syntax -- ' new_string '.join (variable_name)

so = ' python is a language '
print ('-'.join(so))

output
--------
-p-y-t-h-o-n- -i-s- -a- -l-a-n-g-u-a-g-e-


split ()
----------
so = ' python is a language '
print (so.split(' '))

output
-------
['', 'python', 'is', 'a', 'language', '']



index ()
---------

so = 'python is a language'
print(so.index('n'))

output
--------
0


count()
----------

so = 'python is a language'
print(so.count('n',10,16))

so = 'python is a language'
print(so[19])

output
---------
1
e


list
-------
list is the collection of different datatypes that are represented in [] and separated by ,

list is the muttable datatype

methods
----------

append()
---------
this method is used to add new item into the list and it will add at last index position

any_= [1,2,3,4,5]
any_.append(10)
print(any_)
any_.append(20)
print(any_)

output
-------
[1,2,3,4,5,10]
[1,2,3,4,5,10,20]


extend()
---------

any_= [1,2,3,4,5]
any_.append("python")<class 'int'>
print(any_)
any_.extend("python")
print(any_)

output
----------
[1, 2, 3, 4, 5, 6, 'python']
[1, 2, 3, 4, 5, 6, 'p', 'y', 't', 'h', 'o', 'n']


remove()
---------
the remove will del the item based on the value given
if the value is not in list it will show the error 

any_= [1,2,3,4,5,6]
any_.remove(3)
print(any_)
any_,remove(5)
print(any_)

output
----------
[1, 3, 4, 5, 6]
[1, 3, 4, 6]


pop()
------
the pop will del the item based on the index position given
if the index position is out of range in the list will error 

any_= [1,2,3,4,5,]
any_.pop(2)
print(any_)
any_.pop()
print(any_)

output
---------
[1,2,4,5]
[1,2,4]


'''




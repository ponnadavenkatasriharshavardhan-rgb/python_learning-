'''

tuple
--------
tuple is colection different datatype that are represented in () and separeted by ,
tuple is immutable

methods
--------

index
-------
syntax-- variable_name.index(item)
go = (1,'java',[3,4],('python',78))
print (go.index('java'))

count()
--------
syntax -- variable_name.count(item)

go = (1,'java',[3,4],('python',78))
print(go.coumt(('python',78))) ----o/p--- 1
print(go.count('python')) ---- o/p ---- 0

dict
-----
dict is a key:value pair
keys and values separeted by :
dict is represented by {}
keys must be immutable datatypes

methods
--------
keys
-----
syntax -- dict.keys()

values
---------
syntax -- dict.values()

items
-------
syntax -- dict.items()

details = { 'name':'harsha',
            'ac':12345678,
            'pan':9876543,
            'adhr':123456,
            'pin':3456}
print(details.keys())
print(details.values())
print(details.items())

update
-------
syntax -- dict.update({})

clear
------
syntax -- dict.clear()



'''
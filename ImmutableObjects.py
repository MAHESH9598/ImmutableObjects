a=1000
print(a)
print(type(a))
print(id(a))

b=2000
print(b)
print(type(b))
print(id(b))

""" We can't create two different immutable objects with Same data (or) elements """

c=3000
print(c)
print(type(c))
print(id(c))            ## Address of 'c' is ---> 1858119023344

d=3000
print(d)
print(type(d))
print(id(d))            ## Address of 'd' is ---> 1858119023344


##Example 2
"we can't do modifications"

x=5000
print(x)
print(type(x))
print(id(x))            ## Address of 'x' is ---> 2282243177232

x=8000
print(x)
print(type(x))
print(id(x))            ## Address of 'x' is ---> 2282243177264





"""
Above,
c,d adresses are same
Bcause,
with the same data (or)elements we can not create
two different immutable objects.

'Firstly one object created for c variable data 3000
with the address of 1858119023344

next with same data 3000 again one variable came so
it uses c variable address because of with the same data
(or)elements we can not create
two different immutable objects.'

"""



"""
##Example 2
here first address object will be deleted
and created new object with new address



Note1:- immutable objects doesn't allow to modify data (or) element of those objects.

because of that reason in the above example, to change x=8000 it deleted previous object
and created new object.

Note2:- we can do deletion in immutable objects.

"""








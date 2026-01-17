# Collection : Counter, namedtuple,ordereddict,defaultdicts,deque
from collections import Counter
a='aaaaaaaaaabbbbccc'
my_counter=Counter(a)
print(my_counter) # This is like a inbuilt hashmap
print(my_counter.keys()) # This will return the keys dict
print(my_counter.values()) #This will return the values to the keys
print(my_counter.most_common(2))# THis will return the most common rank number 2 and this function will return 
""".most_common(rank)- this will return a list with tuples inside [(),(),()]"""
print(my_counter.most_common(2)[0][0]) # this will print the first index or the key in side the tuple.

b=[[1,2,3],4,(2,3,4,5,6,7,8)]
# when we will use the counter for the above variable it will throw an error as lists are not hashable because they are mutable
print(my_counter.elements()) # This elements will return an iterator object
# Thus we need to convert it to an iterable
print(list(my_counter.elements())) # This will print each characters as individual elements in the lists.

from collections import namedtuple
# THis is an easy to craete and light weight object type similar to a struct.
point= namedtuple('point','x,y') # This will create a class named point with values x and y
pt=point(1,-4)
print(pt) # point(x=1,y=-1) will be the output
# we can also access the individual values
print(pt.x,pt.y)

from collections import OrderedDict
# Similar to dict but just ordered but this irrelavant now as form 3.7 normal dicts are also ordered
ordered_dict=OrderedDict()
ordered_dict['a']=1
ordered_dict['b']=2
ordered_dict['c']=3
ordered_dict['d']=4
print(ordered_dict) # SO this will be ordered dict
from collections import defaultdict
d=defaultdict(int)
# Similar to normal dict but will have a default value that we have entered
d['a']=1
d['b']=2
print(d) # This will return the value that we have entered
print(d['a']) # This will return the value that we have entered
print(d['c']) # AS this key doesnt exist- it will still not raise a key error but rather the default value of the type. that we have specified

from collections import deque
# This is a double ended queue that can be used to add or delete element from both the ends.
d=deque()
d.append(1)
d.append(2)
d.append(4) # This will add elements from the right side
d.appendleft(3) # This willa dd elements on the left side
d.pop() # remove the last element
d.popleft() # This will return and remove element from the left side
d.clear() # This will clear all the elements
d.extend([32,4,5,6,7]) # This will add all the elements at the right side
d.extendleft([1,2,3,4,5,6,7])# This will add all the element from the left side
d.rotate(1) # This will rotate all the element 1 places to the right
print(d)
d.rotate(2) # This will rotate all the elements to the right 2 places
d.rotate(-1) # This will rotate all the elements 1 places to the left
print(d)


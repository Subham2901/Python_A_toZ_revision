#Tuples collection data types ordered and immutable
# often used for objects that belong together
myTuple=("Max",28,"Boston") # it can store multiple data types together generally represented using first bracket
myTuple1="max",29,"Thomas" # In this case also it will take it as a Tuple
myTuple2=("Max",)# if you represent only one element it will not take in as a tuple so we need to add a , along with it
# We can also use the built in tuple function to create a tuple from an iterable for eg. a list
myTuple3=tuple("Hello")
print(myTuple3) # ordered
item = myTuple[0] # this will convert this string into and ordered Tuple
item_negative = myTuple[-1] # To print the last element using thenegative numvbers
print(item_negative)
# We cannot place the value of Tuples in place
#iterations in tuple
for i in myTuple:
    print(i)
# To check if something exisit in the tupple or not
if "Max" in myTuple:
    print("yes")
else:
    print("No the element doesnt exist")

# Other Tuple functions
print(len(myTuple)) # this will print the size of the function
a = (1,1,1,2,3,4,5,6,7,8,9,10)
print(a.count(1)) # Returns the total no of 1 present in the tuple a
print(a.index(1)) # returns the first index when the element 1 appear.
#Converting list into tupples and vice versa
myList = list(a)
print(myList)
# slicing with tuple
b=a[2:5] # This will store the elements starting from index 2 to index 4.
print(b)
#Unpacking of tuples
name,age,city=myTuple
print(name)
print(age)
print(city)
# We can also use the * operator which will assign multiple variables under the variable
i1,*i2,i3 = a
print(i1) # this will print the first element of the tuple a
print(i3) # This will print the last element of the Tuple
print(i2) # This will print the remaining element of the Tuple
#As python is immutable it can do some internal optimisation that makes it efficient to work with tuples.


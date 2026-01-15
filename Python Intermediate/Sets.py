# Sets are represented by curly braces as well
# They are ordered, mutable and doesnt allow duplicates
mySet={1,2,3,4,5,6,7,8}
print(mySet)
# We can also create sets using set function
mySet1=set([1,2,3,4,5,6,7,8])
print(mySet1)
# Adding element in Set
mySet1.add(1)
mySet.add(19)
mySet.add(22) # This function will add an element at the end of the function.
print(mySet) 
# Removing an element from the set
mySet.remove(3) 
print(mySet) # This will remove the element 3 from the set
# We can also remove using discard but in this case if the element we are trying to remove is not present in the set
# To empty our set
mySet1.discard(3) # This will not through any error.
print("The element is removed using the discard function",mySet1)

mySet1.clear() # This will remove all the elements from the set. 
print(mySet1) 

# Set is unordered 
s=set("hello")
print(s) # Thus it will arrange the "Hello" arbitarily.


print(mySet1.pop(),"Popping the first element ") # 
print(mySet1.pop(),"Popping the second element ")


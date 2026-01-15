# Collection data type,unordered and mutable
# exist as key value pairs
d= {"Name":"Subham","Age":26,"City":"Kolkata"}
print(d)
# We can also use dict function to create dictionary
d1=dict(Name="Emily",Age=26,City="Dartford")
print(d1)
value=d["Name"]
print(value) # This will print the value of the Name key from the dict d
# As dict is mutable 
# if you add a new key-value pair, to the existing dictionary then in that case it will get added to the existing dictionary
# Otherwise, if the key already exisit then in that case it will update the key value pair.
d["Email"]="abc@gmail.com"
print(d) # added the new email.
d["Email"]="cdf@gmail.com"
print(d) # updated the d.
# deleting the elements from the dict
del d["Email"]
print(d) # This has removed the "Email " Key value pair from the dict
print(d.pop("City")) # it will remove the Key-Value pair from the dict.
print(d.popitem()) # It will remove the last element of the dict.
# To check if the key exist in the dictionary
if "Name" in d:
    print(d["Name"])

try:
   if  "Name" in d:
    print(d["Name"])
except:
    print("THe key doenst exist in the dict")
# Looping through a dict

for key in d:
   print(key)
for key in d.keys():
   print(key)
for values in d.values():
   print(values)
for key,values in d.items():
   print(key,value)

# Copying a dict
d_c=d  # This will make both the variables point to the same memory location
# That means if one variable attempts to make changes to the dict when you will access the variable the other will
#Change it as well

# Deep Copy 
d_c= d.copy() # This will copy the entire dict to a new memory location. Therefore making changes into one doesnt impact the other

d_c=dict(d) # This will also deep copy the dict  completly
# Update method for dict
d= {"name":"Subham","age":26,"city":"Kolkata"}
d1=dict(Name="Emily",Age=26,City="Dartford")
print(d)
print(d1)
d.update(d1) # this method updates the d in place but returns none.
print(d)

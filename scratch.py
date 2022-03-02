import pandas as pd
print (pd.__version__)

# check type
print (type(1))

# snake case
name_of_var = 2

print ("my name is {}".format('Jim'))
print ("my name is {} my lucky number is {}".format('Jim','17'))
print ("my name is {x} my lucky number is {y}".format(x='Jim',y='17'))

# lists are arrays
list1 = [1,2,3]
list2 = ['a',2]
print (list1[1])
print (list1[-1])
list1.append(4)
list3 = [1,2,list1]
print(list3[2][1])

# dictionary
mydict = {'key1': 'value1', 'key2': 'Value2'}
print(mydict['key1'])

# 1 = true

# tuples tuples are imutable
t = (1,2,3)

# sets unordrd set of unique elements
{1,2,3}

print (list(range(1,5)))





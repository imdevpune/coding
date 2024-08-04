

from collections import OrderedDict, defaultdict



#https://leetcode.com/discuss/study-guide/2122306/Python-Cheat-Sheet-for-Leetcode
dict = {'a':1,'b':2,'c':3}

dict.keys() # returns list of keys of dictionary
dict.values() # returns list of values of dictionary
dict.get('a') # returns value for any corresponding key
dict.items() # returns [('a',1),('b',2),('c',3)]
dict.copy() # returns copy of the dictionary
# NOTE : items() Returns view object that will be updated with any future changes to dict
dict.pop(KEY) # pops key-value pair with that key
dict.popitem() # removes most recent pair added
dict.setDefault(KEY,DEFAULT_VALUE) # returns value of key, if key exists, else default value returned
# If the key exist, this parameter(DEFAULT_VALUE) has no effect.
# If the key does not exist, DEFAULT_VALUE becomes the key's value. 2nd argument's default is None.
dict.update({KEY:VALUE}) # inserts pair in dictionary if not present, if present, corresponding value is overriden (not key)
# defaultdict ensures that if any element is accessed that is not present in the dictionary
# it will be created and error will not be thrown (which happens in normal dictionary)
# Also, the new element created will be of argument type, for example in the below line
# an element of type 'list' will be made for a Key that does not exist
myDictionary = defaultdict(list) 


/** *************************************************** */


d = {'a': 1, 'b': 2, 'c':3}

print (d['a'])  # if key doesn't exist, raise KeyError exception
del d['c'] # if key doesn't exist, raise KeyError exception
#print(d['aaa']) # KeyError: 'aa'


#Iterate over Keys 
print("Keys are ")
for k in d.keys():
    print(k)

#Iterate over Values 
print("Values are ")
for v in d.values():
    print(v)
print(d.values())

#Iterate over key-values 
print("Key-Values are using items()")
for k,v in d.items():
    print(f"{k} : {v}")

#Iterate over key-values using enumerate 
print("Key-Values are using enumerate ")
for k,v in enumerate(d):
    print(f"{k} : {v}")

# get() function
print("use of get()")
print(d.get('a'))
print(d.get('b'))
print(d.get('c'))  #returns None if key doesn't exist

#Add new key-value in dictionary
d['c']=3
print(d)

# remove key-value in dict using pop()
print(f"removing element with value = {d.pop('c')}")
print(d)

# remove key-value in dict using popleft()
d['c']=3
print(f"removing last element {d.popitem()}")
print(d)

#remove all items in dict using clear()
d.clear()
print(d)

# Dict of List
# Converting List[List[int]] to dict : Adjancancy List : [[1,0],[0,1]]
print("\n\n *************** Dict of List ***************")
data=[[1,0],[0,1],[0,2]]
d={}
for pre in data:
    if pre[0] not in d.keys() :
        d[pre[0]]=[]
    d[pre[0]].append(pre[1])
print(d)


print("***** Dict of List using setDefault() *****")
d={}
for (k, v) in data:
    group = d.setdefault(k, []) # key might exist already
    group.append( v )
print(d)

print("***** Dict of List using defaultdict() *****")
d=defaultdict(list)
for k,v in data:
    d[k].append(v)
print(d)
print(d.items())

# List of Dict
print("\n\n *************** List of Dict  ***************")
d1={'name':'abhi','no':1}
print(d1)
list1=[]
list1.append(d1)
print(list1)

d2={'name':'zzzz','no':2}
list1.append(d2)
print(list1)

print(f"name in first dict = {list1[0]['name']} ")

# Dict of Dict 
print("\n\n *************** Dict of Dict  ***************")
d1={'name':'abhi','no':1,'gender':'male'}
d={1:d1}
print(d)

d2={'name':'zzz','no':2,'gender':'female'}
d[2]=d2
print(d)


# Sort Dict based on keys 
# https://www.askpython.com/python/dictionary/sort-a-dictionary-by-value-in-python
print("\n\n *************** Sort Dict based on keys using lambda ***************")

d = {'ravi': '10', 'rajnish': '9',
        'sanjeev': '15', 'yash': '2', 'suraj': '32','abhi':'22'}
#dict1 = OrderedDict(sorted(dict.items()))
dict1 = dict(sorted(d.items(), key=lambda item: item[0]))
#we have created a lambda function and passed the values of the dict as argument i.e. items[0]
print(d)
print(dict1)


# Sort Dict based on values
print("\n\n *************** Sort Dict based on values using lambda ***************")

#d = {'ravi': '10', 'rajnish': '9','sanjeev': '15', 'yash': '2', 'suraj': '32','abhi':'22'}
d = {'ravi': 10, 'rajnish': 9,
        'sanjeev': 15, 'yash': 2, 'suraj': 32,'abhi':22}
dict1 = dict(sorted(d.items(), key=lambda item: item[1]))
#we have created a lambda function and passed the values of the dict as argument i.e. items[1]
print(d)
print(dict1)


# Sort list of Dict based on some specific criteria
print("\n\n *************** Sort list of Dict based on some specific criteria ***************")
# https://www.geeksforgeeks.org/ways-sort-list-dictionaries-values-python-using-lambda-function/
list = [{"name": "Nandini", "age": 20},
       {"name": "Manjeet", "age": 20},
       {"name": "Nikhil", "age": 19}]

# using sorted and lambda to print list sorted by age
print(list)
print("The list printed sorting by age: ")
print(sorted(list, key=lambda i: i['age']))

# using sorted and lambda to print list sorted by both age and name. Notice that "Manjeet"
# now comes before "Nandini"
print("The list printed sorting by age and name: ")
print(sorted(list, key=lambda i: (i['age'], i['name'])))

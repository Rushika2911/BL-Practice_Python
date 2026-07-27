'''
#APPEND
number= [1,2,3,4,5]
number.append(9)
print(number)
'''

'''
#EXTEND
number=[1,2,3,4,5]
number.extend("extend")
number.extend([88,12])      #adds ele as diff diff ele not as single chunk list 
print(number)
'''

'''
#INSERT
num=[1,2,3,4,5]
num.insert(1,'hi')     #insert ele at a particular index
print(num)
'''

'''
#REMOVE
num=[1,2,3,4,5]
num.remove(2)  #removes the first occurance of the element
print(num)
'''

'''
#DEL
num=[3,43,523,64]
del num[3]      #deletes the ele of the particular index
print(num)
'''

'''
#POP
num=[23,523,45,67,7]
num.pop()        #removes the last ele of the list
num.pop(0)       # removes the ele at particular index
print(num)
'''

'''
#SORT
num=[53,142,75,886,97]
num.sort()
print(num)

color=['red','pink','violet','brown']
color.sort()                        sorts in alphabetical order
print(color)
'''

'''
#REVERSE
color=['red','pink','violet','brown']
color.reverse()
print(color)
'''

'''
#COUNT
number= [1,2,4,2,43,6,2,8]
print(number.count(2))          #counts the occureance of the ele in list
'''

'''
fruits=['apple','banana','orange','grapes']
print(fruits.index('orange'))               #tells the index of the ele

num= [10,20,30,20,40,50]
print(num.index(20,2))                 #searching starts from index 2 and the index of first occurance of 20 is printed
'''



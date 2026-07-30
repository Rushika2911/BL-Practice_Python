'''
LIST VS TUPLE
- both can store heterogeneous data
- supports indexing 
- allows slicing

Difference:
- list is muttable while tuple is immumable
- tuple is more memory efficient ie it takes less memory 
- tuple have slight advantage over list in terms of time efficiency

'''

import sys
import timeit 

tuple_num=(1,2,3,4,5,6,7,8,9,10)

list_num=[1,2,3,4,5,6,7,8,9,10]

tuple_size= sys.getsizeof(tuple_num)
print(f"size of tuple is:{tuple_size} bytes")

list_size= sys.getsizeof(list_num)
print(f"size of list is: {list_size}bytes")

tuple_creation_time= timeit.timeit(stmt=lambda: (1,2,3,4,5,6,7,8,9,10), number=1000000)
print(f"tuple creation time: {tuple_creation_time}")

list_creation_time=timeit.timeit(stmt=lambda:[1,2,3,4,5,6,7,8,9,10], number=1000000)
print(f"list creation list: {list_creation_time}")
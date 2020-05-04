from array import *
arr = array('i',{})                                       # this is for the forming a array by given values to by user.
n = int(input("enter the length of the array"))
for i in range(n):                                                 # range goes upto a given n no
    x= int(input("enter the next value"))
    arr.append(x)
print(arr)    


vals = int(input("enter the search no: "))                  # this for finding the given search index value of a given input no
k=0                                                            # given counter value; this is for generating index value
for e in arr:
    if e==vals:
        print(k)
        break 
    k+=1
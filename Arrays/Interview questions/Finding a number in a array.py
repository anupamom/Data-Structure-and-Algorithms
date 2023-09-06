# Finding a number in a array

import numpy as np

myArray = np.array([1,2,3,4,5,6,7,8,9])

def findNumber(array,number):
    for i in range (len(array)):
        if array[i] == number:
            print(i)

findNumber(myArray,7)
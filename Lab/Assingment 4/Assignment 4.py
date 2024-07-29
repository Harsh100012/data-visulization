# Lab 1

import numpy as n

# Question.1
#mylist=list(int(input('Enter List:')))
#arr=n.array(mylist)
arr=n.array([1,2,3,4,5])
print('Numpy Array:')
print(arr)


# Question.2
arr1=n.array([1,2,3,4,5])
print('First element::',arr1[0])
print('Last element::',arr1[len(arr1)-1])
print('Array after doubling each element::')
print(arr1*2)


# Question.3
arr2=n.zeros(10)
print('An array of 10 zeros::')
print(arr2)
arr3=n.zeros(10)+1
print('An array of 10 ones::')
print(arr3)
arr4=n.zeros(10)+5
print('An array of 10 fives::')
print(arr4)

# Question.4
arr5=n.arange(2,11).reshape(3,3)
print('Representing an 3x3 array::')
print(arr5)

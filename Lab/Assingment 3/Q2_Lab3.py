#Convert the below list into the numpy array then display the array 
# then display the first and last index and then multiply each element 
# by 2 and display the result.

my_list = [1,2,3,4,5]
import numpy as np
n_arr = np.array(my_list)
print(n_arr)

print(n_arr[0])
print(n_arr[-1])

print(n_arr*2)
print()
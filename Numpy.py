""" 
NumPy Module
---------------
https://numpy.org/

Numerical Python
Fundamental package for scientific computing
Advanced array-processing package
High-performance multidimensional array object
Efficient multi-dimentional

What are arrays in numpy?
-- Array in numpy is a table of elements
-- all of the same type
-- indexed by a tuple of positive integers
-- In numpy, no of dimensions of the array is called rank of the array
-- An array class in NumPy is called as ndarray
 """

import numpy as np

print("====== #Array Data types ======")

int = np.array([3,5,4,6,7,3])
print (int)
print(int.dtype)    # Integer

str = np.array(['Laasya','Lohini','Anu'])
print(str)
print(str.dtype)    # Strings

flt = np.array([1.5, 2.4, 6.8,9.0])
print(flt)
print(flt.dtype)    # Float

clx = np.array([2, 4.7, 3.5+6.8j])
print(clx)
print(clx.dtype)    # Complex type  ( upcast behaviour)

I = np.array([0,1,-1,0,-10,10], dtype=bool)
print(I)
print(I.dtype)

print("======== # shape - a tuple, contains the no of elements in each dimension ========")
print(int.shape)

print("====== Create 2D array - list of list ======")
x = np.array([
    [1,3],
    [5,7],
    [8,2]
])

print(x)
print(x.shape)

print("====== ndim - Array dimensions =======")
print(int.ndim)
print(x.ndim)

print("====== size - size of all elements =======")
print(int.size)
print(x.size)

print("====== dtype - data type of an array =======")
print(int.dtype)
print(x.dtype)
print(str.dtype)

print("====== nbytes - how big is our array is =======")
print(int.nbytes)
print(x.nbytes)
print(str.nbytes)

print(""" ============================
    Special functions that help us to create constant values
      np.zeros
      np.zeros((dimension,row,coloumns)) -- tuple
==================================
""")
Z = np.zeros((3,5,2))
print(Z)

print("======= np.ones ==========")
print(np.ones(15))

print(""" 
==================================
np.empty    - Empty array
np.fill     - fill an array
np.zeros_like   - fill the array with Zeros
np.ones_like    - fill the array with ones
np.full_like    - fill the array with given value
==================================
""")
f = np.empty((3,2))
print(f)
f.fill(7)
print(f)

p = np.array([
    [1,3],
    [5,7],
    [8,2]
])

print(np.zeros_like(p))
print(np.ones_like(p))
print(np.full_like(p, 5))

print(""" 
==================================
# Spaced values -> incremental or decremental values
# np.arange(start, end, step)   -- end values not included in the final array
==================================
""")

print(np.arange(10))    # step value
print(np.arange(5,10))  # start and step values
print(np.arange(100,0,-10)) # start, end and step value
print(np.arange(0,100,10)) # start, end and step value

print(""" 
==================================
# if you want to include end value too in the final array
# np.linspace(start, end, # of elements needed)   -- end values included in the final array
==================================
""")

print(np.linspace(5, 10, 20))   # start value 5, end value 10, no of elements 20
print(np.linspace(5, 10, 20, endpoint=False)) # don't show end value/point

print(""" 
==================================
# np.logspace(start, end, # of elements needed) - use algorithimic placing
# It used based on 10 base
# 1 = 10 to the power of 0
# 1000 = 10 to the power of 3
==================================
""")

print(np.logspace(0,3,15))  # default base value 10
print(np.logspace(0,3,15, base=2))  # change the base value to 2
print(np.logspace(0,3,15, base=2, endpoint=False)) # Exclude end value

print(""" 
==================================
Createa arrays from set diagnals
==================================
""")
print(np.identity(3))   # Create 3x3 matrix
print(np.identity(5))   # Create 5x5 matrix

print(np.eye(5, k=-2)) # shift the diagnals up or down -- here diagnal value shift to down -2
print(np.eye(5, k=1)) # shift the diagnals up or down -- here diagnal value shift to up 1

print(np.diag(np.array([3,3,3,3,3])))   # all elements on the diagnals to 3 with 5 elements
print(np.diag(np.full(5,3)))    # same result as above

print(np.diag(np.arange(1,11))) # elements from diagnals from 1 to 10
print(np.diag(np.arange(1,11), k=-3))
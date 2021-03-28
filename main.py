# Basic calculation using Numpy

import numpy as np

var1 = np.array([(2,4,6),(9,4,2),(1,3,5)])
var2 = np.array([(10,14,16),(19,14,12),(11,13,15)])
# Python is zero index
print(var1[0,1])
print(var1[0:,1])
print(var1.max())
print(var1.min())
print(var1.sum())

# two arrays opeartions
print("two arrays operation")
print("substraction", var2-var1)
print("addition", var1+var2)
print("Square root of array 1: ", np.sqrt(var1))
print("Exponential of array 1: ", np.exp(var1))
print("Log of array 1: ", np.log(var1))
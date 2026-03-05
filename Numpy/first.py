import numpy as np

## types of array

# a= np.array([1,2,3,4,5]);   # 1-D array
# b= np.array([[1,2,3,4],[5,6,7,8]]) # 2d array 
# c= np.array([[[1,2,3],[5,6,7],[8,9,0]]])   #3d array 

# print(c.ndim);   # to check the number of dimension

# d = np.array([1,2,3,], ndmin=5);   # higher dimensional array (any number of dimensions)
# print(d, d.ndim)

# # print(type(b));  # find the type of array
# print(c);


# Arange function in numpy
#numpy.arange(start, stop, step, dtype=None)


# a= np.arange(0,10);   # array from 0 to 9 
# b = np.arange(0,1,0.2,dtype=float);   # from 0 to 0.8 

# # filtering the sequence 
# c = np.arange(0,20);
# filter = c[c>10] # filter to print element greater than 10 
# print(filter);

# print(b);


# changing the shape of an array By reshaping we can add or remove dimensions or change number of elements in each dimension.



# a = np.arange(0,10).reshape(5,2) 
# newarr= a.reshape(2,5);
# print(a);
# print(newarr)



# Numpy zeros and ones
#numpy.zeros(shape, dtype = None, order = 'C') 


# a = np.zeros(3)  # creating array with all element as zero   
# b=np.zeros(10).reshape(2,5)
# print(a);
# print(b);


#numpy ones

# a=np.ones(4)   # creating an array with all element as one
# b=np.ones((3,3))  # creating an arrat of 3*3 with all elements as 1 
# print(a);     
# print(b);


# numpy linspace (llinear space)
#The numpy.linspace() function is used to generate an array of evenly spaced values between two specified numbers

# a=np.linspace(0,10,10,dtype=int)
# print(a);

# Explanation:
# 0 is the starting value of the sequence.
# 10 is the ending value, and it is included in the output.
# num=10 specifies that exactly 10 values should be generated.

## identity matrix (all elements in diogonal are 1 )

# a= np.identity(4);
# print(a);

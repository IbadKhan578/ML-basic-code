import numpy as np
# # numpy functions


# a= np.array([0,1,2,3,4,5,6,7,8,9]);
# print("Max value of the array:", a.max())   # function to find the max value of the array
# print("Min value of the array", a.min())   # function to find the min value of the array
# print("sum value of the array:", a.sum())   # function to find the sum value of the array
# print("prod value of the array:", a.prod())   # function to find the prodd value of the array
# print(" Mean of the array:", a.mean(axis=0))  #  1-> row , 0-> column (finding mean of the column )
# print ("median, the middle value after sorting, of the array is :", np.median(a))
# print("Standard deviation of the array: ", a.std());   # SD mean how spread the data is from the mean


# b = np.arange(12).reshape(4,3);
# c = np.arange(12,24).reshape(3,4);  # the prerequisite is that the column of firsst n row 
# #of second must have same number of element
# d = np.dot(b,c)     # matrix multiplication is also called dot product 
# print(d)

# print("Log of an array is:", np.log(a))
# print("Exponent of an array is:", np.exp(a));

# e = np.round(np.random.random((2,3))*100) # round() rounds a number to the nearest integer or decimal place.
#             # 0.5 or more → goes up
#             # less than 0.5 → goes down
# print(e)
# f = np.array([0.9,0.4,0.1,0.6])
# print("Round value is:", f.round())

# # floor() always goes down to the nearest integer, even if decimal is large.
# print("Floor value is:", np.floor(f));

# # ceil() always rounds a number up to the nearest integer, no matter what the decimal is.
# print("Ceil of the value:", np.ceil(f))



# # Slicing arrays

# # Slicing in python means taking elements from one given index to another given index.

# # We pass slice instead of index like this: [start:end].

# # We can also define the step, like this: [start:end:step].

# # If we don't pass start its considered 0

# # If we don't pass end its considered length of array in that dimension

# # If we don't pass step its considered 1

# print(a[0:3]);  # elements from o to 2 index excluding end index
# print(a[:5]);  # elements  from starting to index 5
# print(a[5:])  # starting from 5 to end 
# print(a[::2])    # step or jump of 2 from start to end 

# # slicing of 2d Array , we have to write row and column in the bracket 
# print("Array B: ", b)
# print("Slicing of 2d Array", b[2,2])   # 2nd row and 2nd column 


# # slicing of 3d array 
# k = np.array([[[1,2,3],[4,5,6]]])
# print("3D array is:", k)
# print("Printing 5 from this 3d array:", k[0,1,1])

# # Negative Slicing
# # Use the minus operator to refer to an index from the end:
# #  Slice from the index 3 from the end to index 1 from the end:

# print(a[-3:-1]) 



# iteration in 1D array

# arr1 = np.arange(12)
# for x in arr1:
#     print(x);


# # iteration in 2D array

# arr2 = np.array([[1,2,3,4],[5,6,7,8]]);
# for x in arr2:
#     print(x)

#  # iterating through each element of the array 

# for x in np.nditer(arr2):
#     print(x);


# # ravel function converts array of any dimension into one D 

# print("Array in 2D:", arr2)
# print ("Converting 2D array into one D:", arr2.ravel())  # convert n D array into one Dimension


#Stacking means joining arrays together to make a bigger array.
# m = np.arange(0,8).reshape(2,4);
# n = np.arange(8,16).reshape(2,4);
# print("Array M is:", m )
# print("Array N is:", n)

# print(np.hstack((m,n))) # stack horizontaly 
# print(np.vstack((m,n))) # stack vertically 



# # 1. np.split() → basic split
# # Split an array into equal parts
# # Works for 1D or multi-dimensional arrays

# print("horizontal splitting: ",np.hsplit(m,2))
# print("vertical  splitting: ",np.vsplit(m,2))



   






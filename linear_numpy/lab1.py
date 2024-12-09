import numpy as np
from numpy.ma.core import reshape

#Test
# test_array = np.array([1,2,3])
# print(test_array)
#
# # 1d array
# array_1d = np.array([0,23,15])
# print(array_1d)
#
# #Ranag array
# array_rang = np.arange(3)
# print(array_rang)
# array_rang2 = np.arange(5,160,2)
# print(array_rang2)

# #Spaced array
# array_spaced_arr = np.linspace(0,100,5)
# print(array_spaced_arr)

# Type changing
# lin_space_arr_int = np.linspace(0,100,5,dtype=int)
# print(lin_space_arr_int)
#
# arr_rang_float = np.arange(10,dtype= float)
# print(arr_rang_float)
#
# arr_ra_float = np.arange(1,50,10,dtype= float)
# print(arr_ra_float)
#
# char_arr = np.array(["Welcome to Math for ML!"])
# print(char_arr)
# print(char_arr.dtype)
#
# # Build an array of shape 3 filled with ones
# ones_arr = np.ones(3)
# print(ones_arr)
#
# # Build an array of shape 3 filled with zeroes
# zeroes_arr = np.zeros(3)
# print(zeroes_arr)
#
# # Uninitialized array
# empty_arr = np.empty(3)
# print(empty_arr)
#
# # Random array
# random_arr = np.random.rand(3)
# print(random_arr)

# 2D array
# two_d_arr = np.array([[1,2,3,],[3,5,6]])
# # print(two_d_arr)
# print(f"2D Dim {two_d_arr.ndim}") # Dimensions of the array
# print(f"2D Shape {two_d_arr.shape}") # Shape of the array
# print(f"2D Size {two_d_arr.size}") # Size of the array
#
# # Creating a 1D array
# one_dim_arr = np.array([1,2,3,4,5,6])
# print(f"1D Dim {one_dim_arr.ndim}") # Dimensions of the array
# print(f"1D Shape {one_dim_arr.shape}") # Shape of the array
# print(f"1D Size {one_dim_arr.size}") # Size of the array
# # Reshape it into a 2-D array
# reshaped_arr = np.reshape(one_dim_arr,(2,3))
# print(reshaped_arr)
# print(f"reshaped Dim {reshaped_arr.ndim}") # Dimensions of the array
# print(f"reshaped shape {reshaped_arr.shape}") # Shape of the array
# print(f"reshaped Size {reshaped_arr.size}") # Size of the array

# Create two arrays
# arr_1 = np.array([2,4,6])
# arr_2 = np.array([1,3,5])

# Perform math operations
# print("+:", arr_1 + arr_2)
# print("-:", arr_1 - arr_2)
# print("*:", arr_1 * arr_2)
# print("/:", arr_1 / arr_2)

# Converting miles to km
# miles = np.array([1,2,3,4])
# # km = miles * 1.6 # Multiplying each element by 1.6
# # print("Miles to Km:", km)
#
# # Selecting a specific element in the array
# print(arr_1[1]) # printing the second element "4" from the array
# print(arr_2[-1]) # Printing the last element "5" from the array
#
# print(arr_1[1:3]) # Print from the second to the last element
# print(arr_2[0:3]) # Print from the first element to the last element
# print(arr_2[:3]) # Print from the first element to the last element
# print(arr_1[0:]) # Print from the first element to the last

# 2-D Array
# two_dim_arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(two_dim_arr)
# # Slicing rows and columns
# print("First row:", two_dim_arr[0])         # First row
# print("First column:", two_dim_arr[:, 0])   # First column
# print("Middle block:\n", two_dim_arr[0:2, 1:3])  # Slice rows 0-1, columns 1-2

# # Create two arrays for stacking
# a = np.array([[1,1], [2,2]])
# b = np.array([[3,3],[4,4]])
# print(f"a:\n {a}")
# print(f"b:\n {b}")
# # Stacking the arrays vertically
# v_stack = np.vstack((a,b))
# print(v_stack)
#
# #  Stacking horizontally
# h_stack = np.hstack((a,b))
# print(h_stack)



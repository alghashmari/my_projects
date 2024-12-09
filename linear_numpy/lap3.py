import numpy as np

# A = np.array([
#     [4,-3,1],
#     [2,1,3],
#     [-1,2,-5]
# ],dtype=np.dtype(float))
# b = np.array([-10,0,17], dtype= np.dtype(float))
#
# print(f"matrix A:\n {A}")
# print(f"matrix b:\n {b}")
#
# print(f"matrix A shape: {np.shape(A)}")
# print(f"matrix b shape: {np.shape(b)}")
#
# x = np.linalg.solve(A,b)
# print(f"Solution: {x}")
#
# d = np.linalg.det(A)
# print(f"Determinant of matrix A:{d:.2f}")

# A_2= np.array([
#         [1, 1, 1],
#         [0, 1, -3],
#         [2, 1, 5]
#     ], dtype=np.dtype(float))
#
# b_2 = np.array([2, 1, 0], dtype=np.dtype(float))
#
# # print(np.linalg.solve(A_2, b_2))
#
# d_2 = np.linalg.det(A_2)
#
# print(f"Determinant of matrix A_2: {d_2:.2f}")

A = np.array([
    [1,3],
    [3,12]
], dtype= np.dtype(float))
B= np.linalg.solve(A)
print(B)
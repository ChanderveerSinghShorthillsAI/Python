# Creating a matrix using a nested list
A = [[1, 4, 5, 12], 
     [-5, 8, 9, 0],
     [-6, 7, 11, 19]]

# Printing the matrix
print("Matrix A:", A)

# Accessing elements
print("Second row:", A[1])  
print("Third element of second row:", A[1][2])  
print("Last element of first row:", A[0][-1])  

# Extracting a column (3rd column)
column = [row[2] for row in A]
print("3rd column:", column)

# Matrix Addition using nested lists
A1 = [[1, 2, 3], [4, 5, 6]]
B1 = [[7, 8, 9], [10, 11, 12]]

result_addition = [[A1[i][j] + B1[i][j] for j in range(len(A1[0]))] for i in range(len(A1))]
print("Matrix Addition Result:", result_addition)

# Matrix Transposition using nested lists
transpose = [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]
print("Transposed Matrix:", transpose)

import numpy as np

# Creating a NumPy array (Matrix)
A = np.array([[1, 4, 5, 12], 
              [-5, 8, 9, 0], 
              [-6, 7, 11, 19]])

print("NumPy Matrix A:\n", A)

# Asudo apt-get install python3-pipccessing Elements
print("A[0][0]:", A[0][0])  
print("A[1][2]:", A[1][2])  
print("A[-1][-1]:", A[-1][-1])  

# Accessing Rows
print("First Row:", A[0])
print("Last Row:", A[-1])

# Accessing Columns
print("First Column:", A[:, 0])
print("Fourth Column:", A[:, 3])

# Matrix Addition
A1 = np.array([[1, 2, 3], [4, 5, 6]])
B1 = np.array([[7, 8, 9], [10, 11, 12]])
C1 = A1 + B1  # Element-wise addition
print("Matrix Addition Result:\n", C1)

# Matrix Multiplication
A2 = np.array([[3, 6, 7], [5, -3, 0]])
B2 = np.array([[1, 1], [2, 1], [3, -3]])
C2 = np.dot(A2, B2)
print("Matrix Multiplication Result:\n", C2)

# Transpose of a Matrix
A_T = A.transpose()
print("Transposed Matrix:\n", A_T)

# Creating Special Matrices
zeros_matrix = np.zeros((2, 3))
ones_matrix = np.ones((1, 5), dtype=np.int32)
print("Zero Matrix:\n", zeros_matrix)
print("Ones Matrix:\n", ones_matrix)

# Using arange() and reshape()
B3 = np.arange(12).reshape(2, 6)
print("Matrix using arange:\n", B3)

# Slicing Matrices
print("First two rows and four columns:\n", A[:2, :4])
print("All rows, third column:\n", A[:, 2])
print("Last two columns:\n", A[:, -2:])


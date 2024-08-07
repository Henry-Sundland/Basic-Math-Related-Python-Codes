# Basic Math Related Python Codes
 Python codes that solve certain equations and the like

 Created these Python codes to use in other, more complex codes I wanna make. The codes in here mostly just solve certain equations, or find certain math objects. 


 Codes in here:

 1.) Gaussian Elimination Code
 2.) Eigenvalue and Eigenvector Finder Code





 ~ explanation of codes ~

 1.) Gaussian Elimination code allows the user to input a symmetric, n x n matrix A and a vector b, in order to solve the matrix equation Ax = b for the vector x. This code makes use of partial pivoting. Pivoting in Gaussian elimination is a technique used to enhance the numerical stability and accuracy of the method when solving systems of linear equations. It involves rearranging the rows and/or columns of the matrix to position the largest absolute value element in the pivot position before performing the elimination steps.

 2.) Eigenvalue and Eigenvector Finder Code allows the user to input a symmetric n x n matrix and then finds the eigenvalues and eigenvectors of that matrix. It first defines the matrix and finds its symbolic eigenvalues using SymPy. Then, it optionally cleans these eigenvalues by removing negligible imaginary parts. The cleaned eigenvalues are simplified to ensure compatibility with symbolic computations. Using these simplified eigenvalues, the code calculates the corresponding eigenvectors symbolically. Finally, the eigenvectors are converted to numerical form for more readable output, and both the eigenvalues and their corresponding eigenvectors are printed in a clear format.

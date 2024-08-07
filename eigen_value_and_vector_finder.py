import numpy as np
import sympy as sp


#works, but can't find eigenvectors for complex eigenvalues yet....figure out something to do about that

def find_eigenvalues(matrix):
    # Define the symbolic variable lambda
    lambda_var = sp.symbols('lambda')
    
    # Create the identity matrix of the same size as the input matrix
    I = sp.eye(matrix.shape[0])
    
    # Convert the input matrix to a SymPy matrix
    sympy_matrix = sp.Matrix(matrix)
    
    # Form the matrix A - lambda * I
    characteristic_matrix = sympy_matrix - lambda_var * I
    
    # Calculate the determinant of A - lambda * I
    characteristic_polynomial = characteristic_matrix.det()
    
    # Solve the characteristic polynomial for lambda
    eigenvalues = sp.solve(characteristic_polynomial, lambda_var) #sp.solve is a powerful function that cal solve many equations
    
    return eigenvalues


# this function checks to see if there is a negligible, imaginary component of the eigen value that arose due to precision errors in the numerical calculations
#sees if the ratio of the imaginary part to the real part is less than or equal to 10^-4
#if so, just takes the real part of the eigen value
def clean_complex_part(eigenvalues, threshold = 10**-4):
    
    cleaned_eigenvalues = []
    for eigenvalue in eigenvalues:
        real_part = sp.re(eigenvalue)
        imag_part = sp.im(eigenvalue)
        
        # this if statement is to avoid divisino by zero
        if real_part == 0:
            ratio = abs(imag_part)  # If real part is zero, consider the magnitude of the imaginary part
        else:
            ratio = abs(imag_part / real_part)
        
        if ratio <= threshold:
            # If imaginary part is negligible, append only the real part
            cleaned_eigenvalues.append(real_part)
        else:
            # If imaginary part is significant, append the complex eigenvalue
            # Uncomment the next line if you need to debug
            # print(f"Eigen value {eigenvalue} is complex!")
            
            cleaned_eigenvalues.append(eigenvalue)

    return cleaned_eigenvalues

def find_eigenvectors(matrix, eigenvalues):

    # Convert the input matrix to a SymPy matrix
    sympy_matrix = sp.Matrix(matrix)


    # sp.eye(sympy_matrix.shape[0]) makes an identity matrix of the same size as the sympy_matrix
    #.nullspace() method calculates the null space or the kernel of our matrix...i.e. the eigen vectors corresponding to the eigen value
    # Finds eigenvectors this loop does

    eigenvectors = {} #this creates a dictionary for the eigenvectors. relates the eigen value to the eigenvector
    for eigenvalue in eigenvalues:

        eigenvalue = sp.nsimplify(eigenvalue)
        eigenspace = sympy_matrix - eigenvalue*sp.eye(sympy_matrix.shape[0])
        null_space = eigenspace.nullspace()

        if null_space:
            eigenvectors[eigenvalue] = null_space
        else:
            print(f"Warning: No eigenvectors found for eigenvalue {eigenvalue}")

    return eigenvectors

def convert_to_numerical(eigenvectors):
    numerical_eigenvectors = {}
    for eigenvalue, vectors in eigenvectors.items():
        numerical_vectors = [vector.evalf() for vector in vectors]
        numerical_eigenvectors[eigenvalue.evalf()] = numerical_vectors
    return numerical_eigenvectors








# allow user to enter matrix here
cool_size = int(input("Enter the order of the matrix A in integer values: "))
A_matrix = np.zeros((cool_size, cool_size))
  
print("Enter the matrix values for A, row by row:")
for i in range(cool_size):
    row = list(map(float, input().split()))
    A_matrix[i] = row


eigenvalues = find_eigenvalues(A_matrix)
cleaned_eigenvalues = clean_complex_part(eigenvalues)

#print("Raw eigenvalues:", eigenvalues)
#print("Cleaned eigenvalues:", cleaned_eigenvalues)

eigenvectors = find_eigenvectors(A_matrix, cleaned_eigenvalues)
numerical_eigenvectors = convert_to_numerical(eigenvectors)
print(" ")
print("Note: if there are multiple eigenvectors for a given eigenvalue, ")
print("Then the eigenvalue has nonunitary multiplicity.")
print("--------------------------------------------------------")
# Find the eigenvalues

#print("Eigenvalues are these:", eigenvalues)
#print("Eigenvectors are thses:", eigenvectors)

#outputting eigenvalues and eigenvectors
for eigenvalue, vectors in numerical_eigenvectors.items():
    print(f"For Eigenvalue of {eigenvalue}")
    for vector in vectors:
        print(f"eigenvector is any scalar multiple of {vector}")
        print("\n")


print("---------------------------------------------------------")

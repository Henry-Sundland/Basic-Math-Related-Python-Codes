import numpy as np


def gaussElimination(a_matrix, b_matrix):

    
    n = len(b_matrix)
    m = n - 1
    i = 0
    j = i - 1
    x = np.zeros(n)
    


    #creating augmented matrix through concatenate function
    augmented_matrix = np.concatenate((a_matrix, b_matrix), axis = 1, dtype = float)
    print(f"the initial matrix is: {new_line}{augmented_matrix}")
    print("")
    print(f"now solving:")
    print("")

    #applying gaussian elimination w/pivoting
    while i<n:
        #partial pivoting
        for p in range(i + 1, n):
            if abs(augmented_matrix[i,1]) < abs(augmented_matrix[p,i]):
                augmented_matrix[[p,i]] = augmented_matrix[[i,p]]

        if augmented_matrix[i,i] == 0.0:
            print("uh oh, divided by zero")
            return
        
        for j in range(i + 1, n):
            scaling_factor = augmented_matrix[j][i]/augmented_matrix[i][i]
            augmented_matrix[j] = augmented_matrix[j] - (scaling_factor*augmented_matrix[i])
            #print(augmented_matrix) # If you wish to see each elimination step

        i = i + 1


    # back substituaion to solve for x-matrix
    x[m] = augmented_matrix[m][n] / augmented_matrix[m][m]

    for k in range(n - 2, -1, -1):
        x[k] = augmented_matrix[k][n]

        for j in range(k + 1, n):
            x[k] = x[k] - augmented_matrix[k][j]*x[j]

        x[k] = x[k]/augmented_matrix[k][k]


    #displaying solution
    print(f"here are the solution(s):")
    for answer in range(n):
        print(f"x{answer} is {x[answer]}")





#allow user to input their own matrix equation here, for it to solve it for them lol

# User input for matrix
cool_size = int(input("Enter the order of the matrix A in integer values: "))
A_matrix = np.zeros((cool_size, cool_size))
B_matrix = np.zeros((cool_size, 1))
    
print("Enter the matrix values for A, row by row:")
for i in range(cool_size):
    row = list(map(float, input().split()))
    A_matrix[i] = row

print("now please enter the values for the b vector, row by row:")
for i in range(cool_size):
    row = list(map(float, input().split()))
    B_matrix[i] = row

gaussElimination(A_matrix, B_matrix)
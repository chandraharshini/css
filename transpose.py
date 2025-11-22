def add_matrices(A, B): 
    """Add two matrices A and B.""" 
    if len(A) == 0 or len(B) == 0 or len(A) != len(B) or len(A[0]) !=len(B[0]):
        raise ValueError("Matrices must be of the same dimensions for addition.")
        return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))] 
def transpose_matrix(A): 
    """Transpose a matrix A.""" 
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))] 
 
def multiply_matrices(A, B): 
    """Multiply two matrices A and B.""" 
    if len(A[0]) != len(B): 
        raise ValueError("Number of columns in A must be equal to the number of rows in B.") 
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))] 
    for i in range(len(A)): 
        for j in range(len(B[0])): 
            for k in range(len(B)): 
                result[i][j] += A[i][k] * B[k][j] 
    return result 
 
def main(): 
    # Example matrices 
    A = [ [1, 2, 3], 
          [4, 5, 6], 
          [7, 8, 9] ] 
    B = [ [9, 8, 7], 
          [6, 5, 4], 
          [3, 2, 1] ] 
 
    print("Matrix A:") 
    for row in A: 
        print(row) 
 
    print("\nMatrix B:") 
    for row in B: 
        print(row) 
 
    # Add matrices 
    added_matrix = add_matrices(A, B) 
    print("\nAdded Matrix (A + B):") 
    for row in added_matrix: 
        print(row) 
 
    # Transpose matrix A 
    transposed_A = transpose_matrix(A) 
    print("\nTransposed Matrix A:") 
    for row in transposed_A: 
        print(row) 
 
    # Multiply matrices 
    multiplied_matrix = multiply_matrices(A, B) 
    print("\nMultiplied Matrix (A * B):") 
    for row in multiplied_matrix: 
        print(row) 
 
if __name__ == "__main__": 
    main() 


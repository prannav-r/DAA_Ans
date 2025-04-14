import numpy as np

def strassen_matrix_multiply(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    """
    Multiplies two square matrices A and B using Strassen’s divide and conquer method.
    Assumes the dimensions of A and B are n x n, where n is a power of 2.

    Args:
        A: The first square matrix (NumPy array).
        B: The second square matrix (NumPy array).

    Returns:
        The product of A and B as a NumPy array.
    """
    n = A.shape[0]

    # Base case: 1x1 matrix
    if n == 1:
        return A * B

    # Divide matrices into 4 submatrices (quarters)
    mid = n // 2
    A11, A12 = A[:mid, :mid], A[:mid, mid:]
    A21, A22 = A[mid:, :mid], A[mid:, mid:]
    B11, B12 = B[:mid, :mid], B[:mid, mid:]
    B21, B22 = B[mid:, :mid], B[mid:, mid:]

    # Strassen's 7 recursive multiplications
    M1 = strassen_matrix_multiply(A11 + A22, B11 + B22)
    M2 = strassen_matrix_multiply(A21 + A22, B11)
    M3 = strassen_matrix_multiply(A11, B12 - B22)
    M4 = strassen_matrix_multiply(A22, B21 - B11)
    M5 = strassen_matrix_multiply(A11 + A12, B22)
    M6 = strassen_matrix_multiply(A21 - A11, B11 + B12)
    M7 = strassen_matrix_multiply(A12 - A22, B21 + B22)

    # Combine results into submatrices of the result matrix
    C11 = M1 + M4 - M5 + M7
    C12 = M3 + M5
    C21 = M2 + M4
    C22 = M1 - M2 + M3 + M6

    # Combine 4 parts into one result matrix
    top = np.hstack((C11, C12))
    bottom = np.hstack((C21, C22))
    C = np.vstack((top, bottom))

    return C

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

C = strassen_matrix_multiply(A, B)
print(C)

import math

def matrix_chain_multiplication(dimensions: list[int]) -> tuple[int, list[tuple[int, int, int]]]:
    """
    Finds the minimum number of scalar multiplications needed to multiply a
    chain of matrices and the optimal parenthesization.

    Args:
    dimensions: A list of integers representing the dimensions of the
                matrices. If the matrices are A1, A2, ..., An, then
                dimensions will be [p0, p1, ..., pn], where Ai has dimensions
                p(i-1) x p(i).

    Returns:
    A tuple containing:
    - The minimum number of scalar multiplications (int).
    - A list of tuples representing the optimal split points (i, j, k)
      where Ai to Aj is split at Ak.
    """
    n = len(dimensions) - 1  # Number of matrices

    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    S = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    # Fill the dp table using bottom-up tabular method
    for l in range(2, n + 1):  # l is the chain length
        for i in range(1, n - l + 2):
            j = i + l - 1   
            dp[i][j] = math.inf
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + dimensions[i - 1] * dimensions[k] * dimensions[j]
                if cost < dp[i][j]:
                    dp[i][j] = cost
                    S[i][j] = k

    # Optional: Generate the split points as a list of (i, j, k)
    def collect_splits(i, j):
        if i >= j:
            return []
        k = S[i][j]
        return [(i, j, k)] + collect_splits(i, k) + collect_splits(k + 1, j)

    split_points = collect_splits(1, n)

    # Return the minimum multiplication cost and the split points
    return dp[1][n], split_points

dims = [2,1,3,4,1]
min_cost, splits = matrix_chain_multiplication(dims)
print("Minimum multiplications:", min_cost)
print("Split points:", splits)
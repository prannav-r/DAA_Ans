import numpy as np

def simplex_method(tableau: np.ndarray) -> tuple[float, dict[str, float]]:
    num_rows, num_cols = tableau.shape
    num_vars = num_cols - 1  # Last column is RHS

    while True:
        # Step 1: Find pivot column (most negative value in objective row)
        last_row = tableau[-1, :-1] # objective row without RHS
        if np.all(last_row >= 0):
            break  # Optimal solution found

        pivot_col = np.argmin(last_row)

        # Step 2: Find pivot row (smallest positive ratio of RHS to pivot column)
        ratios = []
        for i in range(num_rows - 1):  # Skip objective row
            if tableau[i][pivot_col] > 0:
                ratios.append(tableau[i][-1] / tableau[i][pivot_col])
            else:
                ratios.append(np.inf)

        pivot_row = np.argmin(ratios)
        if ratios[pivot_row] == np.inf:
            raise Exception("Unbounded solution")

        # Step 3: Pivot operation
        pivot_element = tableau[pivot_row][pivot_col]
        tableau[pivot_row] /= pivot_element  # Normalize pivot row

        for i in range(num_rows):
            if i != pivot_row:
                tableau[i] -= tableau[i][pivot_col] * tableau[pivot_row]

    # Extract solution
    solution = {}
    for col in range(num_vars):
        column = tableau[:, col]
        if list(column[:-1]).count(0) == num_rows - 2 and list(column[:-1]).count(1) == 1:
            row_index = list(column[:-1]).index(1)
            solution[f"x{col+1}"] = tableau[row_index][-1]
        else:
            solution[f"x{col+1}"] = 0.0

    max_value = tableau[-1, -1]
    return max_value, solution

tableau = np.array([
    [2, 1, 1, 0, 18],
    [2, 3, 0, 1, 42],
    [-3, -2, 0, 0, 0]
], dtype=float)

opt_val, variables = simplex_method(tableau)
print("Optimal Value:", opt_val)
print("Variable Values:", variables)


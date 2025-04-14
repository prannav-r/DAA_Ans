def solve(n):
    col = set()
    posdiag = set()
    negdiag = set()
    
    res = []
    # This will store the column positions of queens for each row
    queens = [-1] * n

    def backtrack(r):
        if r == n:
            # When a valid configuration is found, append the column positions
            res.append(queens[:])  # Make a copy of queens
            return

        for c in range(n):
            # Skip if the column or diagonals are already occupied
            if c in col or (r + c) in posdiag or (r - c) in negdiag:
                continue

            # Place the queen at (r, c)
            col.add(c)
            posdiag.add(r + c)
            negdiag.add(r - c)
            queens[r] = c

            # Recurse to place queens in the next row
            backtrack(r + 1)

            # Backtrack: remove the queen and reset the sets
            col.remove(c)
            posdiag.remove(r + c)
            negdiag.remove(r - c)
            queens[r] = -1

    backtrack(0)
    return res

# Example usage:
print(solve(3))

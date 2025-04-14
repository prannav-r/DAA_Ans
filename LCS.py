# Time complexity : O(m x n)
# Space complexity : O(m x n)

def longest_common_subsequence(str1, str2):
    """st
    Finds the longest common subsequence of two strings using dynamic
    programming (tabular method).

    Args:
    str1: The first string.
    str2: The second string.

    Returns:
    The longest common subsequence as a string.
    """
    n = len(str1)
    m = len(str2)

    # Initialize a 2D array (table) of size (n + 1) x (m + 1) with zeros
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    # Fill the dp table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Backtrack to find the LCS string
    i, j = n, m
    lcs = []
    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            lcs.append(str1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    # return ''.join(reversed(lcs))
    return lcs[::-1]

print(longest_common_subsequence("ABCB","BDC"))
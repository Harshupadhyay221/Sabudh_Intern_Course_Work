def lcs(S1, S2):
    m = len(S1)
    n = len(S2)
    
    # Create a 2D DP table initialized to 0
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
    
    # Fill dp table
    for i in range(1, m+1):
        for j in range(1, n+1):
            if S1[i-1] == S2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # The value at dp[m][n] will be the length of the LCS
    return dp[m][n]
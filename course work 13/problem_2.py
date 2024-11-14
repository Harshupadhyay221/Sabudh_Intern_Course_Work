
def findMinDiff(arr):
    # Calculate total sum of the array
    total_sum = sum(arr)
    n = len(arr)
    
    # Initialize the DP table (boolean values)
    # dp[i][j] will be true if there is a subset of the first i elements that has sum j
    dp = [[False for _ in range(total_sum + 1)] for _ in range(n + 1)]
    
    # There is always a subset with sum 0 (the empty subset)
    for i in range(n + 1):
        dp[i][0] = True

    # Fill the subset sum table
    for i in range(1, n + 1):
        for j in range(1, total_sum + 1):
            if arr[i - 1] <= j:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]
            else:
                dp[i][j] = dp[i - 1][j]

    # Find the largest j such that dp[n][j] is true where j is <= total_sum // 2
    # This will give the closest sum to total_sum / 2
    half_sum = total_sum // 2
    for j in range(half_sum, -1, -1):
        if dp[n][j] == True:
            subset1_sum = j
            break

    # Subset2 sum will be total_sum - subset1_sum
    subset2_sum = total_sum - subset1_sum

    # Return the minimum difference
    return abs(subset2_sum - subset1_sum)
# 7. largest subarray sum

# we use kdane algo for this 

def maxSubArray(nums):
    # Initialize current_sum and max_sum to the first element of the array
    current_sum = max_sum = nums[0]
    
    # Traverse through the array starting from the second element
    for num in nums[1:]:
        # Update current_sum by deciding whether to add the current element to the existing subarray
        # or to start a new subarray with the current element
        current_sum = max(num, current_sum + num)
        
        # Update max_sum if current_sum is larger
        max_sum = max(max_sum, current_sum)
    
    return max_sum

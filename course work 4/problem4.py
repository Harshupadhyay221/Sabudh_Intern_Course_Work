def trap_water(arr):
    # Edge Case handle
    if not arr:
        return 0

  
    n = len(arr)
    
    # use two pointers for this, one at the start and one at the end of the array
    left, right = 0, n - 1
    
    # Initialize maximum heights on both sides and total trapped water
    left_max, right_max = arr[left], arr[right]
    trapped_water = 0

    # Traverse the array 
    while left <= right:
        # Process the pointer with the smaller maximum height
        if left_max <= right_max:
            # If the current height is less than the maximum height on the left
            if arr[left] < left_max:
               
                trapped_water += left_max - arr[left]
            else:
              
                left_max = arr[left]
            
            left += 1
        else:
            # If the current height is less than the maximum height on the right
            if arr[right] < right_max:
                # Calculate trapped water at the current right position
                trapped_water += right_max - arr[right]
            else:
                
                right_max = arr[right]
            # Move the right pointer to the left
            right -= 1
    
   
    return trapped_water
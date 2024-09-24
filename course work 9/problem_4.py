# 4. find unique elements


def find_unique(nums):
    # Create a dictionary to count the frequency of each element
    freq_map = {}

    # Count the occurrences of each number in the array
    for num in nums:
        if num in freq_map:
            freq_map[num] += 1
        else:
            freq_map[num] = 1

    # Collect the elements that appear only once
    result = [num for num in freq_map if freq_map[num] == 1]

    return result

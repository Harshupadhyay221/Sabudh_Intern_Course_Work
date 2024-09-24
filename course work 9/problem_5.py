# 5. sparesevactor and dot product

class SparseVector:
    def __init__(self, nums):
        # Store non-zero elements and their indices in a dictionary
        self.non_zero_elements = {i: nums[i] for i in range(len(nums)) if nums[i] != 0}

    def dotProduct(self, vec):
        result = 0
        # Iterate over the non-zero elements of this vector
        for idx, val in self.non_zero_elements.items():
            # If the same index has a non-zero element in the other vector, multiply them
            if idx in vec.non_zero_elements:
                result += val * vec.non_zero_elements[idx]
        return result
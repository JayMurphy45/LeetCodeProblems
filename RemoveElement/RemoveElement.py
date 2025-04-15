from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # index is the last unique element
        # i is the current element
        index = 0
        # iterate through the array
        for i in nums:
            # if the current element is not equal to the value to be removed
            # set the next element to the current element
            # increment index by one
            if i != val:
                nums[index] = i
                index += 1
        return index


if __name__ == "__main__":
    solution = Solution()
    
    # Example input
    nums = [3, 2, 2, 3] #change
    val = 3 #change
    
    # Call the removeElement method
    length = solution.removeElement(nums, val)
    
    # Print the result
    print("Length of array after removing elements:", length)
    print("Array after removing elements:", nums[:length])
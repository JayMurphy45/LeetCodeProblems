from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # i and j are two pointers
        # i is the last unique element
        # j is the current element
        i,j=0,1
        # while j is less than the length of nums
        # and i is less than j
        while i<=j and j<len(nums):
            # if the current element is equal to the last unique element
            # increment j by one
            if nums[i]==nums[j]:
                j+=1
            # else if the current element is not equal to the last unique element
            # set the next element to the current element
            # increment i by one
            else:
                nums[i+1]=nums[j]
                i+=1
        # return the length of the array
        return i+1
    

# Example usage
if __name__ == "__main__":
    # Create an instance of the Solution class
    solution = Solution()
    
    # Example input
    nums = [1, 1, 2, 3, 3, 4, 4, 5]
    
    # Call the removeDuplicates method
    length = solution.removeDuplicates(nums)
    
    # Print the result
    print("Length of array after removing duplicates:", length)
    print("Array after removing duplicates:", nums[:length])
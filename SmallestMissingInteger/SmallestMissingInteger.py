from ast import List


class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        count = nums[0] # set the count to the first element in the list
        i = 0 # set the index to 0
        while i < len(nums):
            i += 1
            if nums[i]==nums[i-1]+1:
                count+= nums[i]
            else:
                break
        while True:
            if count not in nums:
                return count
            else:
                count+=1
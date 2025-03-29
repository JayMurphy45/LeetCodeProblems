from ast import List

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        count = nums[0] # set the count to the first element in the list
        i = 0 # set the index to 0
        while i < len(nums) - 1:
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


if __name__ == '__main__':
    s = Solution()

    x = [1, 2, 3, 4, 6, 7, 8, 9, 10]
    y = [1, 3, 4, 5, 6, 7, 8, 9, 10]
    z = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    print(s.missingInteger(x))
    print(s.missingInteger(y))
    print(s.missingInteger(z))

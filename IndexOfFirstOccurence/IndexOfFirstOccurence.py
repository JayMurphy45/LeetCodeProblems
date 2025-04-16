class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Check if needle is empty
        if not needle:
            return 0

        # Check if needle is longer than haystack
        if needle not in haystack:
            return -1

        # h is the index of the haystack
        # n is the index of the needle
        h = 0
        n = 0
        # iterate through the haystack
        while h < len(haystack):
            # if the current element of haystack is equal to the first element of needle
            if haystack[h] == needle[0]:
                # iterate through the needle
                # while n is less than the length of needle
                # and h+n is less than the length of haystack
                # and the current element of haystack is equal to the current element of needle
                # increment n by one
                while n < len(needle) and h + n < len(haystack) and haystack[h + n] == needle[n]:
                    n += 1

                # if n is equal to the length of needle
                if n == len(needle):
                    return h

            # increment h by one
            h += 1

        return -1
    
# Example usage
if __name__ == "__main__":
    # Create an instance of the Solution class
    solution = Solution()
    
    # Example input
    haystack = "hello" #change
    needle = "ll" #change
    
    # Call the strStr method
    index = solution.strStr(haystack, needle)
    
    # Print the result
    print("Index of first occurrence of needle in haystack:", index)
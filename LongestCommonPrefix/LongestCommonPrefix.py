class Solution(object):
    def longestCommonPrefix(self, strs):
        lcp=strs[0]
        for word in strs[1:]:
            minlen=min(len(lcp),len(word)) # get the minimum length of the strings
            i=0 # index to iterate through the characters of the strings
            res="" # result string to store the common prefix
            while(i<minlen):
                if lcp[i]==word[i]: # if the characters are the same
                    res+=lcp[i] # add the character to the result string
                    i+=1 # increment the index
                else:
                    break
            lcp=res
        return lcp
    
if __name__ == '__main__':
    s = Solution()
    
    x = ["flower","flow","flight"]
    y = ["dog","racecar","car"]
    
    print(s.longestCommonPrefix(x))
    print(s.longestCommonPrefix(y))
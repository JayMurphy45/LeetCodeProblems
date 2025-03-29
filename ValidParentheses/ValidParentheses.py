class Solution(object):
    def isValid(self, s):
        # define params and stack
        parentheses = {'(':')', '{':'}','[':']'}
        stack = []
        # iterate through the string
        for i in s:
            # check if the character is an opening bracket
            if i in parentheses: 
                stack.append(i)
            # else return false if the stack is empty or the closing bracket does not match the last opening bracket
            elif len(stack) == 0 or parentheses[stack.pop()] != i:
                return False
        return len(stack) == 0
    
if __name__ == '__main__':
    s = Solution()

    x = "()"
    y = "()[]{}"
    z = "(]"

    print(s.isValid(x)) # True
    print(s.isValid(y)) # True
    print(s.isValid(z)) # False
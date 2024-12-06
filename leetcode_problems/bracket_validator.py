class Solution(object):
    def isValid(self,s):
        stack = []
        brackets = {
            "(":")",
            "[":"]",
            "{":"}"
        }
        for char in s:
            if char in brackets:
                stack.append(char)
            else:
                last_element = stack.pop()
                if brackets[last_element] != char:
                    return False
                
        return len(stack) == 0
    
s = "([])"
solution = Solution()
print(solution.isValid(s))
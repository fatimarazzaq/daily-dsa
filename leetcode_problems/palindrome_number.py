class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        str_x = str(x)
        if str_x[::-1] == str_x:
            return True
        else:
            return False
        
    
s = Solution()
print(s.isPalindrome(123))
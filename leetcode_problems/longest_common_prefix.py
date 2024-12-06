class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        if not strs:
            return ""

        prefix = strs[0]

        for s in strs[1:]:
            while s.find(prefix)!=0:
                prefix = prefix[:-1]
                print(prefix)
                if not prefix:
                    return ""

        return prefix


strs = ["rater","racecar","racar"]

s= Solution()
print(s.longestCommonPrefix(strs))

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        """
        left = 0
        chars = set()
        n = len(s)
        maxLen = 0
        for right in range(1,n+1):
            c = s[right-1]
            while c in chars:
                _c = s[left]
                chars.remove(_c)
                left += 1
            chars.add(c)
            maxLen = max(len(chars), maxLen)
        return maxLen
            

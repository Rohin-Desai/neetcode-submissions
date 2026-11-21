class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        keep expanding right until a dup. 
        """
        n = len(s)
        ll = 0
        i = 0
        cs = set()
        for j in range(1,n+1):
            c = s[j-1]
            while c in cs:
                cs.remove(s[i])
                i += 1
            cs.add(c)
            ll = max(ll, j - i)
        return ll
        
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        solution by DRD
        using frequency array of length 26
        """
        if len(s) != len(t): return False
        cs = [0] * 26
        ct = [0] * 26
        for i in range(len(s)):
            cs[ord(s[i]) - ord('a')] += 1
            ct[ord(t[i]) - ord('a')] += 1
        return cs == ct

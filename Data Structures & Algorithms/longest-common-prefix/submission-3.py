class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        vertical scanning
        """
        n = len(strs)
        if n == 0: return ""
        f = strs[0]
        for i, ch in enumerate(f):
            for j in range(n):
                s = strs[j]
                if i >= len(s) or s[i] != ch:
                    return f[:i]
        return f[:len(f)]
            
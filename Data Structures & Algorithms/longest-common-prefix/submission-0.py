class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        if n == 0: return ""
        if n == 1: return strs[0]
        currentMaxPrefix = strs[0]
        for i in range(1, n):
            currentMaxPrefix = self.getMaxPrefix(currentMaxPrefix, strs[i])
        return currentMaxPrefix

    def getMaxPrefix(self, s1, s2):
        n = min(len(s1), len(s2))
        maxPrefix = []
        for k in range(n):
            if s1[k] == s2[k]:
                maxPrefix.append(s1[k])
            else:
                break
        return "".join(maxPrefix)
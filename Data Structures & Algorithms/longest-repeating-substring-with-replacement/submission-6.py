class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cntd = {}
        n = len(s)
        i = 0
        maxL = 0
        for j in range(1,n+1):
            c = s[j-1]
            cntd[c] = cntd.get(c, 0) + 1
            while (j - i) - max(cntd.values()) > k :
                cntd[s[i]] -= 1
                i += 1
            maxL = max(maxL, j - i)
        return maxL
    
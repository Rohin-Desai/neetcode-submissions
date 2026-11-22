class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cntd = {}
        n = len(s)
        i = 0
        repCount = 0 #replacement count. 
        #replacement count is the the number of size of window - maxCount
        maxL = 0
        for j in range(1,n+1):
            c = s[j-1]
            cntd[c] = cntd.get(c, 0) + 1
            while (j - i) - max(cntd.values()) > k :
                #self.sub(cntd,s[i])
                cntd[s[i]] -= 1
                i += 1
            maxL = max(maxL, j - i)
        return maxL


    def sub(self,d,c):
        if c in d:
            d[c] -= 1
            if d[c] == 0:
                del d[c]
    
    
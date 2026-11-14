class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        #count[s[0]] = 1
        n = len(s)
        l = 0
        maxL = 0
        for i in range(1, n+1):
            if s[i-1] in count:
                count[s[i-1]] += 1
            else:
                count[s[i-1]] = 1
            maxC, maxCnt = self.maxCount(count)
            while (i - l) - maxCnt > k: #i - l is window length
                count[s[l]] -= 1
                l += 1
                maxC, maxCnt = self.maxCount(count)
            maxL = max(maxL, i - l)
        return maxL

    def maxCount(self,d): #tuple of (string, count)
        mc = 0
        c = ""
        for key, value in d.items():
            if value >= mc:
                mc = value
                c = key
        return (c, mc)
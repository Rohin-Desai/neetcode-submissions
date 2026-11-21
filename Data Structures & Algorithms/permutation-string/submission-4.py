class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1s = {}
        for x in s1:
            s1s[x] = s1s.get(x,0) + 1
        n = len(s2)
        i = 0
        s2s = {} #chars in the window on s2 that are also in s1
        for j in range(1,n+1):
            c = s2[j-1]
            #self.add(s2s,c)
            s2s[c] = s2s.get(c,0) + 1
            if j - i == len(s1):
                if self.contains(s1s, s2s): return True
                self.sub(s2s,s2[i])
                i += 1
        return False


    def contains(self, s1s, s2s):
        for k,v in s1s.items():
            if k in s2s:
                if v != s2s[k]: return False
            else:
                return False
        return True

    def sub(self, d, e):
        if e in d:
            d[e] -= 1
            if d[e] == 0:
                del d[e]
        
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        """
        s1c = {}
        for k in s1:
            s1c[k] = s1c.get(k,0) + 1
        s1n = len(s1)
        s2n = len(s2)
        s2c = {}
        l = 0
        for i in range(1,s2n + 1):
            s2c[s2[i-1]] = s2c.get(s2[i-1],0) + 1
            if i - l == s1n : #Window size is big enough
                if s2c == s1c: return True
                c = s2[l]
                s2c[c] -= 1
                if s2c[c] == 0:
                    del s2c[c]
                l += 1
        return False



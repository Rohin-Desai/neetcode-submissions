class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        solution by DRD
        using frequency dictionary (vs sorting)
        """
        sf = self.getFreq(s)
        tf = self.getFreq(t)
        return sf == tf

        
    def getFreq(self, xs):
        d = {}
        for s in xs:
            if s in d:
                d[s] += 1
            else:
                d[s] = 1
        return d
        
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        group = []
        for s in strs:
            arr = self.getFreq(s)
            d.setdefault(arr,[]).append(s)
        return list(d.values())
        

    def getFreq(self,s):
        arr = [0]*26
        for x in s:
            i = ord(x) - ord("a")
            arr[i] += 1
        return tuple(arr)
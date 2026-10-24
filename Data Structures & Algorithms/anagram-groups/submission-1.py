class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        group = []
        for s in strs:
            arr = self.getFreq(s)
            d.setdefault(arr,[]).append(s)
        for key,value  in d.items():
            group.append(value)
        return group

    def getFreq(self,s):
        arr = [0]*26
        for x in s:
            i = ord(x) - ord("a")
            arr[i] += 1
        return tuple(arr)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        group = []
        for i in range(len(strs)):
            s = strs[i]
            arr = self.getFreq(s)
            if arr in d:
                d[arr].append(i)
            else:
                d[arr] = [i]
        for key,value  in d.items():
            anas = []
            for k in value:
                anas.append(strs[k])
            group.append(anas)
        return group

    def getFreq(self,s):
        arr = [0]*26
        for x in s:
            i = ord(x) - ord("a")
            arr[i] += 1
        return tuple(arr)
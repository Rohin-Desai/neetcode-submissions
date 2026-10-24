class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        """
        d = {}
        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1
        sn = sorted(d.items(), key=lambda item: item[1], reverse=True)
        v = []
        for i in range(0, k) :
            v.append(sn[i][0])
        return v
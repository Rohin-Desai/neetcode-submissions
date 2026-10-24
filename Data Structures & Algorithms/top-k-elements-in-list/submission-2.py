class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Use bucket sort
        First do frequency count using a dict n,freq pairs
        """
        f = {}
        buck = [[] for _ in range(len(nums) + 1)]
        for n in nums:
            if n in f:
                f[n] += 1
            else:
                f[n] = 1
        for a in f.items():
            n = a[0]
            freq = a[1]
            buck[freq].append(n)
        res = []
        j = len(buck) - 1
        while j >=1 and len(res) < k:
            bs = buck[j]
            for n in bs: #There could be several n with same frequency
                res.append(n)
                if len(res) == k:
                    break
            j -= 1
        return res
        


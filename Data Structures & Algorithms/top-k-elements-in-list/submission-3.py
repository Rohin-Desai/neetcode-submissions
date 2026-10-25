class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        6:03pm
        use bucketsort
        """
        buck = [[] for _ in range(len(nums) + 1)]
        f = {}
        res = []
        for n in nums:
            if n in f:
                f[n] += 1
            else:
                f[n] = 1
        for (n,freq) in f.items():
            buck[freq].append(n)
        for i in range(len(buck)):
            ns = buck[len(buck) - 1 - i]
            for n in ns:
                res.append(n)
                if len(res) == k:
                    return res
            

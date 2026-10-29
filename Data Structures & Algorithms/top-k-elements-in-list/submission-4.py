class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        use frequency bucket. 
        buck is len(nums) + 1
        We need dict
        9:50pm
        """
        d = {}#num/freq
        b = [[] for _ in range(len(nums) + 1)]
        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1
        for num,freq in d.items():
            b[freq].append(num)
        res = []
        for i in range(len(b)):
            z = len(b) - 1 - i
            arr = b[z]
            for a in arr:
                res.append(a)
                if len(res) == k:
                    return res

            
        
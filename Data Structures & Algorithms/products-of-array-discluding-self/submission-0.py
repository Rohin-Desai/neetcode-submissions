class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        8:37pm
        """
        prefix = [1 for _ in range(len(nums))]
        suffix = [1 for _ in range(len(nums))]
        prevp = 1
        prevs = 1
        res = []
        if len(res) == 1: return [nums[0]]
        for i in range(len(nums)):
            p = i
            s = len(nums) - 1 - i
            prefix[p] = prevp * nums[p]
            prevp = prefix[p]
            suffix[s] = prevs * nums[s]
            prevs = suffix[s]
        for k in range(len(nums)):
            prod = 1
            suff, pref = 1,1
            if k == 0:
                suff = suffix[k+1]
            elif k == len(nums) - 1:
                pref = prefix[k-1]
            else:
                suff = suffix[k+1]
                pref = prefix[k-1]
            prod = pref * suff
            res.append(prod)
        return res


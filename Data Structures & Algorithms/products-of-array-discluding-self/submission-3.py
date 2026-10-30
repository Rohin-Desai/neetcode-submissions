class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        based on Solution 1, but can i not treat len(nums) == 1 as
        a special case? 
        Well don't worry. We have:
        2 <= nums.length <= 100,000
        -30 <= nums[i] <= 30
        So the length will always be 2 or greater
        """
        n = len(nums)
        prefix = [1 for _ in range(n)]
        suffix = [1 for _ in range(n)]
        prevp = 1
        prevs = 1
        res = []
        #if len(res) == 1: return [nums[0]]
        for i in range(n):
            p = i
            s = n - 1 - i
            prefix[p] = prevp * nums[p]
            prevp = prefix[p]
            suffix[s] = prevs * nums[s]
            prevs = suffix[s]
        res.append(suffix[1])
        for k in range(1,n-1):
            suff = suffix[k+1]
            pref = prefix[k-1]
            prod = pref * suff
            res.append(prod)
        res.append(prefix[n-2])
        return res


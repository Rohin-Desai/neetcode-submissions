class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        max = 0
        for i  in range(len(nums)):
            n = nums[i]
            _max = 1
            if n-1 not in numsSet:
                j = 1
                while n + j in numsSet:
                    _max += 1
                    j += 1
            if _max > max:
                max = _max
        return max
        
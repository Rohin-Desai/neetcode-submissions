class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        """
        n = len(nums)
        l = 0
        r = 0
        sum = 0
        minL = float('inf')
        for r in range(1,len(nums)+1):
            sum += nums[r-1]           
            while sum >= target:
                if minL > r-l :
                    minL = r-l
                sum -= nums[l]
                l += 1
        if minL == float('inf'):
            return 0
        else:
            return minL

                

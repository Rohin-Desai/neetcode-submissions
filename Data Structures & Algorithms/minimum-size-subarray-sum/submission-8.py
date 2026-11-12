class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        let's assume l and r are fence between cells.
        l < r before entring while loop
        can we allow l <= r where the sum would be 0?
        """
        n = len(nums)
        l = 0
        r = 0
        #sum = nums[0]
        sum = 0
        minL = float('inf')
        while r <= n:
            if sum >= target:
                if minL > r - l:
                    minL = r - l
                sum -= nums[l]
                l += 1
            else: # sum < target
                r += 1
                if r > n: continue
                sum += nums[r-1]
        if minL == float('inf'):
            return 0
        else:
            return minL

                

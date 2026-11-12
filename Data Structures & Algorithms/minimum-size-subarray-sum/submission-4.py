class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        let's assume l and r are fence between cells.
        l < r before entring while loop
        """
        n = len(nums)
        l = 0
        r = 1
        sum = nums[0]
        minL = float('inf')
        while True:
            if sum >= target:
                if minL > r - l:
                    minL = r - l
                sum -= nums[l]
                l += 1
                if l >= r:
                    r += 1
                    if r > n: break
                    sum += nums[r-1]
            else: # sum < target
                r += 1
                if r > n: break
                sum += nums[r-1]
        if minL == float('inf'):
            return 0
        else:
            return minL

                

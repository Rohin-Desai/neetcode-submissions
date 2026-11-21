class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        currSum = 0
        minL = float('inf')
        for j in range(1,n + 1):
            #subarray here is [i,j)
            currSum += nums[j-1]
            while currSum >= target:
                minL = min(minL, j-i)
                currSum -= nums[i]
                i += 1
        if minL == float('inf'): return 0
        return minL
                
            
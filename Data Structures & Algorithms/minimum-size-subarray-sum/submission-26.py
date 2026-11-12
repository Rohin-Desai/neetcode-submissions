class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        prefix sum plus binary search
      
        """
        p = [0 for _ in range(len(nums)+1)]
        psum = 0
        minL = float('inf')
        for i in range(1,len(nums) + 1): #1 ... n
            psum += nums[i-1]
            p[i] = psum
            l = 0
            k = i #not inclusive
            while l < k:
                mid = l + (k - l)//2
                if p[mid] > p[i] - target:
                    k = mid
                else:
                    l = mid + 1
            if l == 0:
                pass
            else:
                 minL = min(minL, i - (l-1))
        if minL == float('inf'):
            return 0
        else:
            return minL

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        7:42pm 7:49pm 
        """
        res = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i-1] == nums[i]:
                continue #i == 0 is goes through. After that go to very first
            j = i+1
            k = len(nums) - 1
            while (j < k):
                t = nums[i] + nums[j] + nums[k]
                if t < 0:
                    j += 1
                elif t > 0:
                    k -= 1
                else: 
                    res.append([ nums[i], nums[j], nums[k]])
                    j += 1
                    #k -= 1
                    while j < k and nums[j-1] == nums[j]:
                        j += 1
        return res

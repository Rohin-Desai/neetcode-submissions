class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        10/20/2026
        Solve the 2sum problem for each index. 
        """
        value = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -1 * nums[i]
            #Do 2sum to find target (skip i)
            j=i+1
            k=len(nums)-1
            while j < k:
                if nums[j] + nums[k] < target:
                    j += 1
                elif nums[j] + nums[k] > target:
                    k -= 1
                else: #we have found target
                    t = [nums[i],nums[j],nums[k]]
                    value.append(t)
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
        return value


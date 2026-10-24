class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        10/20/2026
        Solve the 2sum problem for each index. 
        """
        rv = set([])
        nums.sort()
        for i in range(len(nums)):
            target = -1 * nums[i]
            #Do 2sum to find target (skip i)
            j=0
            k=len(nums)-1
            while j < k:
                if j == i:
                    j += 1
                    continue
                if k == i:
                    k -= 1
                    continue
                if nums[j] + nums[k] < target:
                    j += 1
                elif nums[j] + nums[k] > target:
                    k -= 1
                else: #we have found target
                    t = [nums[i],nums[j],nums[k]]
                    t.sort()
                    rv.add(tuple(t))
                    j += 1
                    k -= 1
                    continue
        returnValue = []
        for r in rv:
            returnValue.append(list(r))
        return returnValue


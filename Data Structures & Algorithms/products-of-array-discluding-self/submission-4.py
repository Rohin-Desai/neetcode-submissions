class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        9:52pm
        """
        res = []
        prev = 1
        for n in nums:
            res.append(n*prev)
            prev = n*prev
        res[len(nums) - 1] = res[len(nums) - 2]
        #Now res is the prefix array
        suffProd = nums[len(nums)-1]
        for i in range(len(nums)-2,0,-1):
            res[i] = res[i-1] * suffProd
            suffProd = nums[i] * suffProd
        res[0] = suffProd
        return res 
        
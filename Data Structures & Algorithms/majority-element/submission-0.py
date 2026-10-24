class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        moore voting algol as I recal.
        solution by DRD 
        """
        candidate = nums[0]
        vote = 1
        for i in range(1,len(nums)):
            if vote == 0:
                candidate = nums[i]
            if candidate == nums[i]:
                vote += 1
            else: 
                vote -= 1
        return candidate

        
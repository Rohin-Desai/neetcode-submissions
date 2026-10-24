class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        currNum = 0

        for i in range(len(nums)):
            currNum = nums[i]
            for j in range(i + 1, len(nums)):
                if nums[j] == currNum:
                    return True
        return False 
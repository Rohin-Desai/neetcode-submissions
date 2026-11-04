class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        8:05pm
        """
        n = len(nums)
        if n == 1: return 1
        i = 1 #fencecut to the left
        j = 1 #fencecut again. Between i and j we have duplicates we don't care about. The left of i we have our array we want to return (basically, return i, which is the number of elements to the left. That's why fencecuts are cool)
        while (j < len(nums)):
            if nums[j] != nums[i-1]: #not a duplicate
                nums[i] = nums[j]
                j += 1
                i += 1 #everything to the left is our array. 
            else: #It's a duplicate so ignore
                j += 1
        return i

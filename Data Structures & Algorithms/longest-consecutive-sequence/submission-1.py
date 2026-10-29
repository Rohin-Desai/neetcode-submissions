class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        use a set and iterate until 
        9:23pm
        """
        numSet = set(nums)
        maxLen = 0
        for n in numSet:
            if n - 1 not in numSet:
                k = n + 1
                length = 1
                while k in numSet:
                    length += 1
                    k += 1
                if length > maxLen:
                    maxLen = length
        return maxLen
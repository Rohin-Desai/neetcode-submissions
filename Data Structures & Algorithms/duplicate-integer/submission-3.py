class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        solution by DRD
        """
        d = {}
        for n in nums:
            if n in d:
                return True
            else:
                d[n] = 0
        return False
        
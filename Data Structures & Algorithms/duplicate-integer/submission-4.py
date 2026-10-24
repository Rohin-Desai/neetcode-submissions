class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        solution by DRD
        use hash set instead of dict
        """
        s = set()
        for n in nums:
            if n in s:
                return True
            else:
                s.add(n)
        return False
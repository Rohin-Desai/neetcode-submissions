class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        solution by DRD
        use sorting.
        """
        ss = "".join(sorted(s))
        st = "".join(sorted(t))
        return ss == st
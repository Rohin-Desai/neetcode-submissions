class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        rewrite using isalnum
        6:10pm
        """
        i = 0
        j = len(s) - 1
        while (i <= j):
            si = s[i].lower()
            sj = s[j].lower()
            if not si.isalnum():
                i += 1
                continue
            if not sj.isalnum():
                j -= 1
                continue
            if si != sj:
                return False
            i += 1
            j -= 1
        return True

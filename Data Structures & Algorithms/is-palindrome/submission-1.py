class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        5:37pm -  5:51pm
        """
        i = 0
        j = len(s) - 1
        while i <= j:
            si = s[i].lower()
            sj = s[j].lower()
            if not (( ord(si) >= ord('a') and ord(si) <= ord('z') ) or (ord(si) >= ord('0') and ord(si) <= ord('9'))):
                i += 1
                continue
            if not (( ord(sj) >= ord('a') and ord(sj) <= ord('z') ) or (ord(sj) >= ord('0') and ord(sj) <= ord('9'))):
                j -= 1
                continue
            if si != sj:
                return False
            i += 1
            j -= 1
        return True

        
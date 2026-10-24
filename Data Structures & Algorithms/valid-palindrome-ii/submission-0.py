class Solution:
    
    def validPalindrome(self, s: str) -> bool:
        self.skipped = False
        """
        solution by DRD 10/18/2026
        note, pointer i and j at begin and end
        if s[j] != s[i] we have to do both branches
        1) decrement j and then continue from there to see if palindrome
        2) increment i and then  continue from there to see if palindrome
        We can only do this skipping once so we need a boolean to check.
        """
        i, j = 0, len(s)-1
        return self._validPalindrome(s,i,j)
        
    def _validPalindrome(self, s: str, i, j):
        while (i <= j):
            si = s[i]
            sj = s[j]
            if si == sj:
                i += 1
                j -= 1
                continue
            else: #si != sj
                if self.skipped == True:
                    return False #we already skipped. If we have to again, this is not palindrome
                self.skipped = True #we can only skip once.
                return self._validPalindrome(s,i+1,j) or self._validPalindrome(s,i,j-1)
        return True #If we got here, return true. 


        
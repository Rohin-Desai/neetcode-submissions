class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_dict = {}
        for c in t:
            t_dict[c] = t_dict.get(c,0) + 1
        n = len(s)
        s_dict = {}
        l = 0 #left fence
        min_range = None
        print("n is " + str(n))
        for i in range(1,n+1):
            #print("i is " + str(i))
            if s[i-1] in t_dict:
                s_dict[s[i-1]] = s_dict.get(s[i-1],0) + 1
            while self.isValid(t_dict, s_dict):
                #print("is valid + " + str((l,i)))
                if min_range is None or min_range[1] - min_range[0] > i - l:
                    min_range = (l,i)                
                if s[l] in t_dict:
                    s_dict[s[l]] -= 1
                    if s_dict[s[l]] == 0:
                        del s_dict[s[l]]
                l += 1 #Note after this and the while exits, it window will be invalid
                #print("l = " + str(l))

        if min_range is None: return ""
        return s[min_range[0]:min_range[1]]


    def isValid(self, t_dict, s_dict):
        for key, value in t_dict.items():
            if key in s_dict and s_dict[key] >= value:
                continue
            else:
                return False
        return True

class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        c = "#"
        for s in strs:
            sn = len(s)
            s = str(sn) + "#" + s
            encoded += s
        return encoded


    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0  
        sn = ""          
        while i < len(s):
            if s[i] != "#":
                sn = sn + s[i]
                i += 1
            else: 
                n = int(sn)
                _s = s[i+1:i+n+1]
                strs.append(_s)
                i = i + n + 1 #Jump right after
                sn = ""
        return strs
            


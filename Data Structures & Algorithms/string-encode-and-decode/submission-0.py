class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        c = "#"
        for s in strs:
            sn = len(s)
            s = str(sn) + "#" + s
            print("-- s is " + s)
            encoded += s
        return encoded.strip()


    def decode(self, s: str) -> List[str]:
        print("string is " + s)
        strs = []
        i = 0  
        sn = ""          
        while i < len(s):
            if s[i] != "#":
                print("1 sn is " + sn)
                sn = sn + s[i]
                print("2 sn is " + sn)
                i += 1
            else: 
                n = int(sn)
                _s = s[i+1:i+n+1]
                print("_s is " + _s)
                strs.append(_s)
                i = i + n + 1 #Jump right after
                sn = ""
        return strs
            


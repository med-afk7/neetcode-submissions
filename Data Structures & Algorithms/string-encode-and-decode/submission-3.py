class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in strs:
            s += i
            s+='@@'
        return s 

    def decode(self, s: str) -> List[str]:
     if len(s) == 0 : 
        return []
     new = s[:-2]
     a = new.rsplit('@@')
             
     return a
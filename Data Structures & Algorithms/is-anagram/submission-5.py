class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        temp = t

        if len(s) != len(t):
            return False

        for x in s  :
            if x not in temp :
                return False
            temp = temp.replace(x , "" , 1)
        
        return True
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        temp = nums.copy()
        
        for x in nums :
            real =  nums.count(x)
            if real >1 :
                return True
    
        return False
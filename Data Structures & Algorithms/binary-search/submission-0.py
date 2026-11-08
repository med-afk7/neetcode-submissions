class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l = 0
        r = len(nums) -1 
        mid = math.floor(r/2)

        while l <= r :
            if nums[mid] > target:
                r = mid-1
                mid = math.floor((r+l)/2)

            elif nums[mid] < target:
                l = mid +1
                mid = math.floor((r+l)/2)
            else :
                return mid
        return -1
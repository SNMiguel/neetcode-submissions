class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        g = False
        for i in nums:
            if nums.count(i) > 1:
                g = True
        return g
            
         
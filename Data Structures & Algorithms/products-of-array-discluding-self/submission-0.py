class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_r = [1] * len(nums)
        r_r = [1] * len(nums)
        for i in range(len(nums)):
            if i != 0:
                l_r[i] = l_r[i-1] * nums[i-1]
                r_r[(i+1) * (-1)] = r_r[i * (-1)] * nums[i * (-1)]
        
        return [l * r for l, r in zip(l_r, r_r)]
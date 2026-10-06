class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # s_nums = sorted(nums)
        # left = 0
        # right = len(nums) - 1

        # res = []
        # while left < right:
        #     for n in (s_nums[left + 1 : right]):
        #         if (s_nums[left] + s_nums[right] + n) == 0 and ([s_nums[left], n, s_nums[right]]) not in res:
        #             res.append([s_nums[left], n, s_nums[right]])
            
        #     if (s_nums[left] + s_nums[right]) > 0:
        #         right -= 1
        #     else: # (s_nums[left] + s_nums[right]) < 0:
        #         left += 1
        
        # return res

        nums.sort()
        res = []

        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                n_sum = num + nums[l] + nums[r]
                if n_sum > 0:
                    r -= 1
                elif n_sum < 0:
                    l += 1
                else:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
            
        return res
            
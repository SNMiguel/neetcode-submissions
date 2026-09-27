class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, val in enumerate(nums):
            if (target - val) not in seen:
                seen[val] = i
            else:
                return [seen[target - val], i]

        return 0
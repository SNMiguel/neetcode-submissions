class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s_nums = sorted(list(set(nums)))
        temp = []
        slow = 0
        fast = 0
        while fast < len(s_nums)-1:
            # if s_nums[fast] == s_nums[::-1]:
            #     temp.append(len(s_nums[slow:fast]))
            #     break

            if s_nums[fast] + 1 == s_nums[fast + 1]:
                fast += 1
            else:
                temp.append(len(s_nums[slow:fast + 1]))
                fast += 1
                slow = fast
        temp.append(len(s_nums[slow:fast + 1]))
        
        return max(temp)

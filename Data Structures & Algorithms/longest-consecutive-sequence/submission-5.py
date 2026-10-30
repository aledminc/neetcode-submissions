class Solution:
    def countStreak(self, i, nums):
        count = 1
        while nums[i+1] == nums[i] + 1:
            count += 1
            i += 1
            if i == len(nums) - 1:
                break
        return count
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elif len(nums) == 1:
            return 1
        nums = list(set(nums))
        nums.sort()
        streaks = []
        for i in range(len(nums) - 1):
            if nums[i-1] != nums[i] - 1 and nums[i+1] == nums[i] + 1:
                streaks.append(self.countStreak(i, nums))
        if streaks:    
            return max(streaks)
        else:
            return 1

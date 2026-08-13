class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        combs, seen = [], []
        nums = sorted(nums)
        for i in range(len(nums) - 2):
            if nums[i] in seen:
                continue
            else:
                seen.append(nums[i])
            j, k = i + 1, len(nums) - 1
            while j != k and k > j:
                if nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                elif nums[i] + nums[j] + nums[k] == 0:
                    combs.append([nums[i],nums[j],nums[k]])
                    j += 1
                    k -= 1
        return list({tuple(sorted(row)) for row in combs})
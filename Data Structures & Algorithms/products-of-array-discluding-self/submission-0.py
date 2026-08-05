import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        for i in range(len(nums)):
            hold = nums[:i] + nums[i+1:]
            out.append(math.prod(hold))
        return out
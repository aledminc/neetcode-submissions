class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r, cur = 0, len(nums) - 1, int((len(nums)-1)/2)
        while l < r:
            cur = int((r+l)/2)
            print(f"right {r}, left {l}, cur {cur}")
            if nums[cur] == target:
                return cur
            elif nums[cur] < target:
                l = cur + 1
            elif nums[cur] > target:
                r = cur -1
        if nums[l] == target: 
            return l
        if nums[r] == target:
            return r
        return -1
        
            
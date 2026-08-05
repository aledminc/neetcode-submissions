class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        holder = set([])
        for i in nums:
            if i in holder:
                return True
            else:
                holder.add(i)
        return False
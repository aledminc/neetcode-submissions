class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hold = {}
        for i in nums:
            if i in hold:
                hold[i] += 1
            else:
                hold[i] = 1

        sorted_keys = sorted(hold.keys(), key=lambda x: hold[x], reverse=True)
        top_k = sorted_keys[:k]
        
        return top_k
import math
class Solution:

    def viable(self, h, piles, k):
        hours = 0
        for i in piles:
            hours += math.ceil(i/k)
        if hours <= h:
            return True
        else: 
            return False

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        while left < right:
            mid = (left + right)//2
            if self.viable(h, piles, mid):
                right = mid
            else:
                left = mid + 1
        return left
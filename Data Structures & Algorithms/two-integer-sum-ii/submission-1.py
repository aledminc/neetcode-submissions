class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            loop = numbers[i+1:]
            print(loop)
            for j in range(len(loop)):
                print(i,j)
                if numbers[i] + loop[j] == target:
                    return [i+1,j+i+2]

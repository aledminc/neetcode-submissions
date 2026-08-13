class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack, answer = [], [0]*(len(temperatures))
        for i in range(len(temperatures)):
            if not stack:
                stack.append((temperatures[i], i))
                continue
            while temperatures[i] > stack[-1][0]:
                    answer[stack[-1][1]] = i - stack[-1][1]
                    stack.pop()
                    if not stack:
                        break
            stack.append((temperatures[i], i))
        return answer
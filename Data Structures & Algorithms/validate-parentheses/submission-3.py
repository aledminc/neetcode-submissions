class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False
        stack = [s[0]]
        s = s[1:]
        i=0
        while i < len(s):
            if not stack:
                stack.append(s[i])
                i+=1
            print(i, s[i], stack)
            if (s[i] == ")" and stack[-1] == "(") or (s[i] == "}" and stack[-1] == "{") or (s[i] == "]" and stack[-1] == "["):
                stack.pop()
                i+=1
            else:
                stack.append(s[i])
                i+=1
        if len(stack) > 0:
            return False
        else:
            return True


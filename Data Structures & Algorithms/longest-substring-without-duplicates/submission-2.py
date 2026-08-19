class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        r, cur, longest = 0, [], 0
        while r < len(s):
            if s[r] in cur:
                cur = cur[cur.index(s[r]) + 1:]
                cur.append(s[r])
            else:
                cur.append(s[r])
                if len(cur) > longest:
                    longest = len(cur)
            r += 1
        return longest


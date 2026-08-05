class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hold = {}
        for word in strs:
            base = "".join(sorted(word))
            if base in hold:
                hold[base].append(word)
            else:
                hold[base] = [word]
        final = []
        for key in hold:
            final.append(hold[key])
        return final

            
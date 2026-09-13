class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = ""
        for n, c in enumerate(s):
            new = c

            for char in s[n + 1:]:
                if char not in new:
                    new += char
                else:
                    break

            if len(new) > len(longest):
                longest = new

        return len(longest)
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        end = len(s) - 1
        while end >= 0 and s[end] == " ":
            end -= 1

        last_length = 0
        for i in range(end + 1):
            last_length += 1

            if s[i] == " ":
                last_length = 0

        return last_length
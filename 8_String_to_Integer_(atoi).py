class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        min32 = -2**31
        max32 = 2**31 - 1
        new_string = "0"
        negative = 1

        if not s:
            return 0

        if s[0] == "-":
            negative = -1
            s = s[1:]
        elif s[0] == "+":
            s = s[1:]

        for char in s:

            if not char.isdigit():
                new_string = "0" + new_string
                break

            if char.isdigit():
                new_string = new_string + char
            

        answer = int(new_string) * negative

        if answer < min32:
            return min32
        elif answer > max32:
            return max32

        return answer
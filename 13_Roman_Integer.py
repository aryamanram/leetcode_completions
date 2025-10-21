class Solution:
    def romanToInt(self, s: str) -> int:
        symbol_values = {"I":1, "V":5, "X":10,"L":50, "C":100, "D":500, "M":1000}
        value = 0
        i = 0

        while i < len(s):
            if i + 1 < len(s) and symbol_values[s[i + 1]] > symbol_values[s[i]]:
                value += symbol_values[s[i + 1]] - symbol_values[s[i]]
                i += 2
            else:
                value += symbol_values[s[i]]
                i += 1

        return value
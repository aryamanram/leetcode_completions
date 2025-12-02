class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        L, R = 2, x // 2

        while L <= R:
            mid = L + (R - L) // 2
            if (mid * mid) > x:
                R = mid - 1
            elif (mid * mid) < x:
                L = mid + 1
            else:
                return mid

        return R
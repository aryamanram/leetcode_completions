class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        remain = total % p

        if remain == 0:
            return 0

        res = len(nums)
        curSum = 0
        remainToIndex = {
            0: -1
        }

        for i, n in enumerate(nums):
            curSum = (curSum + n) % p
            prefix = (curSum - remain + p) % p
            if prefix in remainToIndex:
                length = i - remainToIndex[prefix]
                res = min(res, length)
            remainToIndex[curSum] = i

        return -1 if res == len(nums) else res
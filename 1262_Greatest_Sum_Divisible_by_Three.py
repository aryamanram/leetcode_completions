class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        maxSum = 0

        smal_one_rem = float('inf')
        smal_two_rem = float('inf')
        for num in nums:
            maxSum += num
            if num % 3 == 1:
                smal_two_rem = min(smal_two_rem, num + smal_one_rem)
                smal_one_rem = min(smal_one_rem, num)
            if num % 3 == 2:
                smal_one_rem = min(smal_one_rem, num + smal_two_rem)
                smal_two_rem = min(smal_two_rem, num)

        if maxSum % 3 == 0:
            return maxSum
        if maxSum % 3 == 1:
            return maxSum - smal_one_rem
        if maxSum % 3 == 2:
            return maxSum - smal_two_rem
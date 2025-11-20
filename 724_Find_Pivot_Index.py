class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # prefixList = []
        # total = 0

        # for num in nums:
        #     total += num
        #     prefixList.append(total)

        # for i in range(len(nums)):
        #     if prefixList[i - 1] == (prefixList[-1] - nums[i] - prefixList[i - 1]):
        #         return i
        
        # return -1

        total = sum(nums)

        leftSum = 0
        for i in range(len(nums)):
            rightSum = total - nums[i] - leftSum
            if leftSum == rightSum:
                return i
            leftSum += nums[i]
        return -1
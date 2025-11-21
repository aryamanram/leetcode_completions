class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        elementAmount = {}

        for num in nums:
            if num not in elementAmount:
                elementAmount[num] = 1
            else:
                elementAmount[num] += 1

        limit = len(nums) / 2

        for element in elementAmount:
            if elementAmount[element] >= limit:
                return element
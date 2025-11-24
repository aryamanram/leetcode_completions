class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        answer = []
        prefixSum = 0

        for num in nums:
            prefixSum = ((prefixSum << 1) + num) % 5
            answer.append(prefixSum % 5 == 0)

        return answer
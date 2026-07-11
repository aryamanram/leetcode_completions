class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        output = []

        if not nums:
            return output

        ranges = [[nums[0]]]
        place = 0

        for i in range(1, len(nums)):
            if nums[i - 1] + 1 == nums[i]:
                ranges[place].append(nums[i])
            else:
                ranges.append([nums[i]])
                place += 1

        for summary in ranges:
            if len(summary) > 1:
                output.append(f"{summary[0]}->{summary[-1]}")
            else:
                output.append(f"{summary[0]}")

        return output

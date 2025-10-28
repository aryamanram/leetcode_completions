class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        
        max_count = 0

        for num in nums:
            if num - 1 in nums:
                pass
            else:
                count = 1
                n = num
                while n + 1 in nums :
                    count += 1
                    n += 1

                max_count = max(max_count, count)
    
        return max_count
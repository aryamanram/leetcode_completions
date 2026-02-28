class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # for i, num1 in enumerate(nums):
        #     for num2 in nums[i + 1:]:
        #         if num1 == num2:
        #             return num1
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow
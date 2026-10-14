class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = nums[0]
        max_sum = nums[0]
        for num in nums[1:]:
            cur_sum += num
            if num > cur_sum:
                cur_sum = num
            max_sum = max(cur_sum, max_sum)
        return max_sum
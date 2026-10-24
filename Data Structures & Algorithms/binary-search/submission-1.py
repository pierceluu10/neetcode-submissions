class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        i = r // 2
        while nums[i] != target:
            if l >= r:
                return -1
            if nums[i] > target:
                r = i - 1
                i = (l + r) // 2
            else:
                l = i + 1
                i = (l + r) // 2
        return i

                
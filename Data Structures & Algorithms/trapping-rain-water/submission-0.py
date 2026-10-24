class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l = 0
        r = len(height) - 1
        l_max = 0
        r_max = 0
        water = 0
        while l < r:
            l_max = max(l_max, height[l])
            r_max = max(r_max, height[r])
            if l_max >= height[l]:
                water += l_max - height[l]
            if r_max >= height[r]:
                water += r_max - height[r]
            if l_max >= r_max:
                r -= 1
            else:
                l += 1
        return water
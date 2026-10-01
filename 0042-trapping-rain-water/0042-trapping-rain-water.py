class Solution:
    def trap(self, height: List[int]) -> int:

        # 1. Create left_max
        left_max = [0] * len(height)
        left_max[0] = height[0]

        for i in range(1, len(height)):
            left_max[i] = max(left_max[i - 1], height[i])


        # 2. Create right_max
        right_max = [0] * len(height)
        right_max[-1] = height[-1]

        for i in range(len(height) - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])


        # 3. Calculate water
        total = 0

        for i in range(len(height)):
            water = min(left_max[i], right_max[i]) - height[i]
            total += water

        return total
class Solution:
    def maxArea(self, height: List[int]) -> int:
        right = len(height) - 1
        left = 0
        heighest = 0

        while right > left:
            height_left = height[left]
            height_right = height[right]
            distance = (right - left) * min(height_left, height_right)
            if heighest < distance:
                heighest = distance

            if height_right < height_left:
                right -=1
            else:
                left +=1

        return heighest
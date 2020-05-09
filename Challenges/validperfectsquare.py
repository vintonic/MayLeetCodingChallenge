class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True
        left = 2 
        right = num
        while left <= right:
            mid = (left+right) // 2
            midSqr = mid * mid
            if midSqr == num:
                return True
            elif midSqr > num:
                right = mid - 1
            else:
                left = mid + 1
        return False

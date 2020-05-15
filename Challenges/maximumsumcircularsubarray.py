class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        k = self.Kadane(A)
        
        CS = 0
        for i in range(len(A)):
            CS += A[i]
            A[i] = -A[i]
        CS = CS + self.Kadane(A)
        
        if CS > k and CS != 0:
            return CS
        else:
            return k
        
    def Kadane(self, nums):
        cur_sum, max_sum = nums[0], nums[0] 
        for n in nums[1:]:
            cur_sum = max(n, cur_sum + n)
            max_sum = max(cur_sum, max_sum)
        return max_sum

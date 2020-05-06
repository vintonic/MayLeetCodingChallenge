class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''
        Solution approach: assuming that the majority element 
        always exists in the array, we can simply sort the array
        and return the element in the middle of it.
        The python build-in sort() function has time complexity
        O(n log n) (it's a kind of merge sort) so the total time
        complexity of the solution is then O(n log n). 
        '''

        nums.sort()
        
        return nums[len(nums)//2]
        

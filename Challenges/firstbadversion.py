class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # Solution approach: custom iterative binary search. 
        
        # Left index 
        l = 1 
        # Right index 
        r = n

        while l < r: 
            
            # Mid between left and right index
            mid = (l + r) // 2

            # If mid index is 'bad', ignore all indexes after it (they will be 'bad' too)
            if isBadVersion(mid): 
                r = mid

            # If mid index is 'ok', ignore it and all indexes before (they will be 'ok' too)
            else: 
                l = mid + 1

        # At this point l == r == 'the first bad version'
        return l

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        
        '''
        Solution approach: use a list to store the jewels 
        and to quickly check if a stone is a jewel.
        The data structure used in Python List implementation 
        is Hashing, so common operations like insertion or 
        traversal can be performed in O(1) on average.
        So the total time complexity is O(len(S)).
        '''
        
        jewels_list = set(J)
        jewels_count = 0
        
        for stone in S:
            if stone in jewels_list:
                jewels_count = jewels_count + 1
                
        return jewels_count

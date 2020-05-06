class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        '''
        Solution approach: use a set to store all the repeated 
        letters found iterating over the string.
        This solution proved to be faster than 89% of the other 
        solutions submitted on Leetcode.
        In fact, the average time complexity is almost linear.
        '''
            
        repeated_letters = set()
        
        for i in range(len(s)):
            
            if s[i] not in repeated_letters:
                repetition_found = 0
                
                for j in range (i+1, len(s)):
                    if s[i] == s[j]:
                        repeated_letters.add(s[i])
                        repetition_found = 1
                        break
                        
                if(repetition_found == 0):
                    return i
                
        return -1

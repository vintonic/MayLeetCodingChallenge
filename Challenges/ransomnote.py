class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        '''
        Solution approach: use dictionary to store magazine 
        letters count and then iterate over ransomNote letters 
        to check if all of them are stored in the dict.
        Time complexity: O(n), where n is the lenght of ransomNote
        '''
        
        if len(ransomNote) > len(magazine):
            return False
        
        dict = {}
        
        for letter in magazine:
            if letter in dict:
                dict[letter] = dict[letter] + 1
            else:
                dict[letter] = 1
        
        for letter in ransomNote:
            if letter not in dict:
                return False
            if dict[letter] == 0:
                return False
            dict[letter] = dict[letter] - 1
        return True

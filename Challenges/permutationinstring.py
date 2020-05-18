class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_lenght = len(s1)
        s1_counter = Counter(s1)
        window_counter = Counter()
        
        for i, c in enumerate(s2):
            window_counter[c] += 1
            
            if i >= s1_lenght:
                element_from_left = s2[i - s1_lenght]
                
                if window_counter[element_from_left] == 1:
                    del window_counter[element_from_left]
                else:
                    window_counter[element_from_left] -= 1
            
            if window_counter == s1_counter:
                return True
            
        return False

class Solution:
    def findComplement(self, num: int) -> int:
        '''
        Solution approach: complement bit by bit the num 
        by doing xor operation between the num itself and 
        a bitmask with only 1 bit "high", iterating from the 
        least significant bit to the most significant bit.
        '''
        
        '''
         temp var is only used to check num 'binary lenght',
         so that the while loop does math.ceil(log2(num+1)) cycles 
         (the exact number of binary digits representing the num)
        '''
        temp = num
        bitmask = 1
        while temp:
            # XOR
            num = num ^ bitmask
            # Left shift
            bitmask = bitmask << 1
            # Right shift
            temp = temp >> 1
        return num

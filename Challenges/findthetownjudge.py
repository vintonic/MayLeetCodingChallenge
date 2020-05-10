class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        
        '''
        1.  Create an array of Size N + 1 to represent each person.
            arr[i] represents trust score of i th person
            and arr[i] = number of persons trusts him - number of persons he trusts.
        2.  Now, traverse through given array.
            a , b = a believes b
            so, increment trusts of b => arr[b]++
            decrement belives of a => arr[a]--
        3.  At last traverse through each person, if anyone found with N - 1 trusts, then return his index.
        4.  if not found, return -1
        '''
        
        if len(trust) < N - 1:
            return -1
        
        trust_score = [0] * (N+1)
        
        for (a, b) in trust:
            trust_score[a] -= 1
            trust_score[b] += 1
            
        for i in range(1, len(trust_score)):
            if trust_score[i] == N-1:
                return i
            
        return -1

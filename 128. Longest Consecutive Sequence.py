class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)

        sol = 0
        for n in numSet:
            if(n-1 not in numSet):
                cSol = 1
                while(n+1 in numSet):
                    cSol += 1
                    n += 1
                
                if(cSol > sol):
                    sol = cSol

        return sol
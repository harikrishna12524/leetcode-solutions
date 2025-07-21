class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)

        sol = 0
        while(len(numSet) > 0):
            temp = 0
            curNum = numSet.pop()
            numSet.add(curNum)

            cSol = self.findCon(curNum, numSet)
            if(cSol > sol):
                sol = cSol

        return sol

    def findCon(self, cNum, nSet):
        if(cNum not in nSet):
            return 0

        nSet.remove(cNum)
        sol1 = self.findCon(cNum - 1, nSet) + self.findCon(cNum + 1, nSet) + 1
        return sol1
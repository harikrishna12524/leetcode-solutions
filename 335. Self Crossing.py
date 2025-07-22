class Solution:
    def isSelfCrossing(self, distance: List[int]) -> bool:
        n = len(distance) 
        if(n < 4): 
            return False
        
        gOut = True
        for i in range(2, n):
            if(gOut and distance[i] <= distance[i-2]):
                gOut = False
                if(i > 3 and distance[i] >= distance[i-2] - distance[i-4] or i == 3 and distance[i] == distance[i-2]):
                    distance[i-1] -= distance[i-3]
            elif(not gOut):
                if(distance[i] >= distance[i-2]):
                    return True

        return False
        
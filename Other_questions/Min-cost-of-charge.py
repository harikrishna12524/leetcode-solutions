def getMinCost(charges):

    max_v = charges[0]
    need = []
    for i in range(0, len(charges)):
        if(charges[i] > max_v):
            max_v = charges[i]

        need.append(max_v - charges[i])

    sol = 0
    for i in range(1, len(need)):
        if(need[i] > need[i-1]):
            sol += need[i] - need[i-1]
    
    # print(need)
    # print(sol)
    return sol

assert getMinCost([5,1,1,1,5]) == 4
assert getMinCost([3,2,1]) == 2
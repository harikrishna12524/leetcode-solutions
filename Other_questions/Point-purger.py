def getMaxPoints(rewards):

    rewards.sort()

    sol = 0
    j = 0
    for i in range(len(rewards)-1, -1, -1):
        if(rewards[i] <= j):
            break
        sol += (rewards[i] - j)
        j+=1

    print(sol)
    return sol

assert getMaxPoints([5,2,2,3,1]) == 7
assert getMaxPoints([]) == 0
assert getMaxPoints([1,1,1,1,1,1]) == 1
assert getMaxPoints([1,2,3,4,5]) == 9
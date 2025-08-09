def getSurvivingProcess(robots):
    if(not len(robots)):
        return []

    combinedElements = {}
    '''
    1 : { 1, [0], 0}
    6 : { 6, [1], 0}
    2 : { 2, [2, 4], 0}
    7 : { 7, [3], 0}
    '''
    
    for i in range(len(robots)):
        r = robots[i]
        if(r not in combinedElements):
            combinedElements[r] = {
                "val" : r,
                "indices" : [],
                "pS" : 0
            }
        combinedElements[r]["indices"].append(i)
    
    elems = list(combinedElements.values())

    elems.sort(key = lambda ele: ele["val"])

    # [[1, 1] ,[2, 5] , [6, 11], [7, 18]]
    elems[0]["pS"] = elems[0]["val"] * len(elems[0]["indices"])
    for i in range(1, len(elems)):
        elems[i]["pS"] = (elems[i]["val"] * len(elems[i]["indices"])) + elems[i-1]["pS"]

    
    sol = []
    sol.extend(elems[-1]["indices"])
    i = len(elems) - 2
    while(i > -1 and elems[i]["pS"] >= elems[i+1]["val"]):
        sol.extend(elems[i]["indices"])
        i-=1

    return list(map(lambda n: n+1, sol))
    # return sol


# print(getSurvivingProcess([1,6,2,7,2]))
# Basic examples
assert sorted(getSurvivingProcess([1, 6, 2, 7, 2])) == [2, 4]
assert sorted(getSurvivingProcess([1, 1])) == [1, 2]
assert sorted(getSurvivingProcess([])) == []

# Increasing sequence
assert sorted(getSurvivingProcess([1, 2, 3, 4])) == [2, 3, 4]

# Decreasing sequence
assert sorted(getSurvivingProcess([10, 8, 6, 4])) == [1, 2, 3]

# All equal
assert sorted(getSurvivingProcess([3, 3, 3, 3])) == [1, 2, 3, 4]

# Two largest equal
assert sorted(getSurvivingProcess([5, 7, 7, 1])) == [2, 3]

# Large leader only
assert sorted(getSurvivingProcess([100, 1, 1, 1, 1])) == [1]

# Duplicates in the middle
assert sorted(getSurvivingProcess([1, 2, 8, 4, 7, 6, 3, 5])) == [2, 3, 4, 5, 6, 7, 8]
assert sorted(getSurvivingProcess([1, 2, 8, 4, 7, 5, 3, 5])) == [2, 3, 4, 5, 6, 7, 8]

# Single element
assert sorted(getSurvivingProcess([42])) == [1]

# Zeroes (if valid for your problem)
assert sorted(getSurvivingProcess([0, 0, 1])) == [3]

# Case with min value appearing multiple times
assert sorted(getSurvivingProcess([2, 2, 5, 10])) == [4]

# Case with min value appearing multiple times
assert sorted(getSurvivingProcess([1, 5, 5, 10, 10])) == [2,3,4,5]

print("All tests passed.")

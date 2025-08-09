def getMaxServer(servers):
    countMap = {}
    for k in servers:
        if k not in countMap:
            countMap[k] = {
                "val" : k,
                "count" : 0
            }
        countMap[k]["count"] += 1

    srted = list(countMap.keys())
    srted.sort()

    solarr = []
    sol = 0
    act_sol = 0
    for k in srted:
        if(not len(solarr) or (solarr[-1]["val"] + 1 == k and (len(solarr) < 2 or solarr[-1]["count"] > 1))):
            solarr.append(countMap[k])
            sol += countMap[k]["count"]
        else:
            act_sol = max( sol , act_sol )
            if(solarr[-1]["val"] + 1 != k):
                solarr = [countMap[k]]
                sol = countMap[k]["count"]
            else:
                sol = countMap[k]["count"] + solarr[-1]["count"]
                solarr = [solarr[-1], countMap[k]]

    print()   
    print(act_sol)
    return act_sol


assert getMaxServer([4,3,5,1,2,2,1]) == 5
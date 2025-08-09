def getMinFlipAndSegments(bs):

    # bs = 1110011000
    focus_arr = [] # [1, -1, -1, -1, 0]
    flips = 0 # 3
    for i in range(0, len(bs), 2):
        if(bs[i] != bs[i+1]):
            focus_arr.append(-1)
            flips += 1
        else:
            focus_arr.append(int(bs[i]))

    segms = 1 # 2
    lo = -1 # 1
    for k in focus_arr:
        if(k != -1 and k != lo):
            if(lo != -1):
                segms += 1
            lo = k

    print("Flips : " + str(flips) + " Segments : " + str(segms))
    return [flips, segms]


assert getMinFlipAndSegments("1110011000") == [3, 2]
assert getMinFlipAndSegments("1111111111") == [0, 1]
assert getMinFlipAndSegments("1100110011") == [0, 5]
assert getMinFlipAndSegments("1100110011") == [0, 5]
def getVariable(password):

    subsc = (len(password) * (len(password)-1)) // 2


    palssc = 0
    for i in range(0, len(password)-1):

        for sp in [[i-1, i+1], [i, i+1]]:
            j = sp[0]
            k = sp[1]
            while(j >= 0 and k < len(password) and password[j] == password[k]):
                palssc +=1
                j -= 1
                k += 1

    # print(subsc - palssc)
    return subsc - palssc


assert getVariable("abc") == 3
assert getVariable("aba") == 2
assert getVariable("aaaaa") == 0
assert getVariable("") == 0
assert getVariable("abacbc") == 13

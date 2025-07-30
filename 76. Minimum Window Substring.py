class Solution:
    def minWindow(self, s: str, t: str) -> str:

        tTbl = {}
        for k in t:
            if(k not in tTbl):
                tTbl[k] = 0
            tTbl[k] += 1

        isValid = { "sol" : False } 
        def modify(tbl1, char, isAdd):
            if(char not in tTbl):
                return
            if(isAdd):
                if(char not in tbl1):
                    tbl1[char] = 0
                tbl1[char] += 1
            else:
                if(char in tbl1):
                    tbl1[char] -= 1

            # print("char : " + char + " tbl1 : " + str(tbl1) + " tTbl : " + str(tTbl))
            if(tbl1[char] < tTbl[char]):
                isValid["sol"] = False
                # print("Here 1")
                return

            for k in tTbl:
                if(k not in tbl1 or tbl1[k] < tTbl[k]):
                    isValid["sol"] = False
                    # print("Here 2")
                    return
            # print("Here 3")
            isValid["sol"] = True

        i = 0
        j = 0
        sTbl = {}
        modify(sTbl, s[j], True)
        sol = ""
        while(j < len(s) and i < len(s)):
            # print("isValid : " + str(isValid["sol"]) + " string : " + s[i : j+1] + " map : " + str(sTbl) )
            if(isValid["sol"]):
                if(sol == "" or len(sol) > j-i + 1):
                    sol = s[i : j+1]
                # if(s[i] in sTbl):
                #     sTbl[s[i]] -= 1
                modify(sTbl, s[i], False)
                i += 1
            else:
                j += 1
                if(j >= len(s)):
                    break
                if(s[j] not in tTbl):
                    continue
                # if(s[j] not in sTbl):
                #     sTbl[s[j]] = 0
                # sTbl[s[j]] += 1
                modify(sTbl, s[j], True)
        
        return sol
        
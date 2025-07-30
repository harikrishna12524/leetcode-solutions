class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        wordMap = {}
        for word in words:
            wordMap[word] = wordMap.get(word, 0) + 1
        
        need = len(wordMap)
        uL = len(words[0])  
        mTL = len(words) * uL

        sol = []
        for i in range(uL):
            have = 0
            haveMap = {}
            strPos = i
            for j in range(i, len(s), uL):
                # Add a condition whether length is okay for solution
                word = s[j: j+uL]
                if(word not in wordMap):
                    strPos = j+uL
                    have = 0
                    haveMap = {}
                    continue
                
                haveMap[word] = haveMap.get(word, 0) + 1
                # print("Here for word :  "+ word + ".Have Map :" + str(haveMap))
                if(haveMap[word] == wordMap[word]):
                    have+=1
                elif(haveMap[word] > wordMap[word]):
                    while(haveMap[word] > wordMap[word]):
                        strWord = s[strPos : strPos + uL]
                        if(haveMap[strWord] == wordMap[strWord]):
                            have-=1
                        haveMap[strWord] -= 1
                        strPos = strPos + uL

                if(have == need):
                    sol.append(strPos)
                    strWord = s[strPos : strPos + uL]
                    have-=1
                    haveMap[strWord] -= 1
                    strPos = strPos + uL
        
        return sol
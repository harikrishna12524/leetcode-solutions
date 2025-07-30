class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        wordMap = {}
        for word in words:
            wordMap[word] = wordMap.get(word, 0) + 1
        
        need = len(wordMap)
        uL = len(words[0])  
        mTL = len(words) * uL

        sol = []
        for i in range(len(s)-mTL + 1):

            have = 0
            locWordMap = {}
            curPos = i
            while(curPos + uL <= len(s)):
                substr = s[curPos : curPos + uL]
                if(substr not in wordMap):
                    break
                
                locWordMap[substr] = locWordMap.get(substr,0) + 1
                if(locWordMap[substr] == wordMap[substr]):
                    have += 1
                elif(locWordMap[substr] > wordMap[substr]):
                    break

                if(have == need):
                    sol.append(i)
                    break

                curPos += uL
        
        return sol
# Last updated: 10/21/2025, 2:03:40 PM
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {"2":["a","b","c"],'3':["d","e","f"],'4':["g","h","i"],'5':["j","k","l"],'6':["m","n","o"],'7':["p","q","r","s"],'8':["t","u","v"],'9':["w","x","y","z"]}
        aList = dic.get(digits[0])
        bList = []
        for x in digits[1:]:
            for y in aList:
                for each in dic.get(x):
                    bList.append(y+each)
            aList = bList
            bList = []            
        return aList
                    
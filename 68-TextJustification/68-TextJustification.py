# Last updated: 10/21/2025, 2:03:29 PM
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        aList = []
        rList = []
        t=""
        for x in words:
            if len(t) + len(x) > maxWidth:
                aList.append(t.strip())
                t=x + " "
            else:
                t += x + " "
        aList.append(t.strip())
        print(aList)
        for x in aList:
            t, y = "", x.split(" ")
            spaces = maxWidth-len(x)
            if len(y) == 1 or len(rList) == len(aList)-1:
                x+= " "*spaces
                t=x
            else:
                spaceBetween = (spaces +len(y)-1)//(len(y)-1)
                spaceRemainder = (spaces+len(y)-1)%(len(y)-1)
                for z in y:
                    t += z + " " * spaceBetween
                    if spaceRemainder > 0:
                        t += " "
                        spaceRemainder -= 1
                t = t.strip()
            rList.append(t)
        print(rList)
        return rList
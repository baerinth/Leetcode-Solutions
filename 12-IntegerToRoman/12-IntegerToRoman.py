# Last updated: 10/21/2025, 2:03:44 PM
class Solution:
    def intToRoman(self, num: int) -> str:
        numbers = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        romans = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        output = ""

        while num > 0:
            while num - numbers[0] >= 0:
                num -= numbers[0]
                output += romans[0]
            numbers.pop(0)
            romans.pop(0)
        return output
                
class Solution:
    def intToRoman(self, num: int) -> str:
        roman_numerals = [
            [1000, 'M'],
            [900, 'CM'],
            [500, 'D'],
            [400, 'CD'],
            [100, 'C'],
            [90, 'XC'],
            [50, 'L'],
            [40, 'XL'],
            [10, 'X'],
            [9, 'IX'],
            [5, 'V'],
            [4, 'IV'],
            [1, 'I']
        ]
            
        roman = ""
        while num > 0:
            for number, symbol in roman_numerals:
                if num >= number:
                    num -= number
                    roman += symbol
                    break
        
        return roman
    
    # num = 1994
    # roman = ""
    
    # num = 994
    # roman = 'M'
    
    # num = 94
    # roman = 'MCM'
    
    # num = 4
    # roman = 'MCMXC'
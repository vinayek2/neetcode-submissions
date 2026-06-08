class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string = ""
        for i in range(len(digits)):
            string += str(digits[i])
        value = (int(string) + 1 )
        lister = []
        while value != 0:
            integer = value%10
            lister.append(integer)
            value //= 10 
        
        return lister[::-1]
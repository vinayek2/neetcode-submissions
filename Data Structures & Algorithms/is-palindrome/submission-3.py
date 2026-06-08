class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_string = ""
        s = s.lower()
        for i in range(len(s)):
            characters = str(s[i])
            if((characters.isalpha()) | (characters.isnumeric())):
                new_string += s[i]
                print(new_string)
                
        return new_string[::-1] == new_string
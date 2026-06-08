class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for element in strs:
            string += element +"/"
        return string 

    def decode(self, s: str) -> List[str]:
        main_list = s.split('/')
        main_list.pop()

        return main_list 

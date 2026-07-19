def remove_fourth_character(word: str) -> str:
    word = word[0:3] + word[4:len(word)] if len(word) > 4 else word 
    return word 
    pass


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))

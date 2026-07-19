def concatenate(s1: str, s2: str) -> str:
    tog = s1 + s2 if (len(s1 + s2)) <= 10 else "Too long!"
    return tog
    pass




# do not modify below this line
print(concatenate("He", "llo"))
print(concatenate("Hello ", "world!"))
print(concatenate("Length", "of10"))

from typing import List

def read_integers() -> List[int]:
    line = input("")
    str_list = line.split(",")
    str_list = [int(i) for i in str_list]

    return str_list
    pass

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())

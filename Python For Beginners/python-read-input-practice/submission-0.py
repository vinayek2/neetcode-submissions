def add_two_numbers() -> int:
    line = input("")
    lister = line.split(",")
    lister = [int(i) for i in lister]
    return sum(lister)
    pass



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())

number_list = []

while True:
    number = int(input("Enter a number, to end enter -1: "))
    if number < 0:
        break
    number_list.append(number)

print(number_list)
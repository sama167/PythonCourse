def cal_eco_index(fam)->float:
    ind = fam[4]/fam[2]
    return ind

def sort_by_eco_index(proccessed_fam):
    return proccessed_fam[2]


data = [("Hamed", 39, 3, 1, 550, "tehran"),
        ("Sara",  41, 2, 1, 370, "tehran"),       
        ("Paria", 23, 3, 1, 600, "karaj"),       
        ("Ahmad", 29, 2, 0, 810, "qazvin"),       
        ("Matin", 35, 4, 2, 430, "tehran"),       
        ("Sina", 29, 3, 2, 190, "qazvin"),       
        ("Hooman", 33, 4, 2, 450, "tehran"),       
        ("Mehdi", 43, 5, 3, 520, "tehran"),       
        ("Mehran", 46, 4, 2, 490, "karaj"),
        ("Javad", 42, 4, 2, 640, "tehran")]


data_copy = []

for family in data:
    index = cal_eco_index(family)
    name = family[0]
    income = family[4]
    size = family[2]
    data_copy.append((name, income, index, size))

data_copy.sort(key=sort_by_eco_index)

for new_t in data_copy:
    print(new_t)

print("the poorest family is ", data_copy[0])
print("the richest family is ", data_copy[-1])


buget=1000

for fami in data_copy:
    size = fami[2] * 50
    print("------------------------------------")
    if buget-size >= 0:
        print(size , " toman to ", fami[0])
        buget = buget-size
        print("ramining bugdet", buget)
    else:
        print(f"Cannot give {size} to {fami[0]}. Remaining budget is {buget}....")
        break



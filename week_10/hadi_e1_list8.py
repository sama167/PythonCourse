def each_person(fami):
    return fami[2]

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



buget=1000

for fami in data:
    each = fami[2] * 50
    print("------------------------------------")
    if buget-each >= 0:
        print(each , " toman to ", fami[0])
        print("ramining bugdet", buget)
        buget = buget-each
    else:
        print(f"Cannot give {each} to {fami[0]}. Remaining budget is {buget}....")
        break


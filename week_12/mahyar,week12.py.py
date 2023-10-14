data = [{"name":"ali","math": 13.5, "science":18, "physicall_education":17, "Art":10, "farsi": 14 },
        {"name":"mamad","math":13, "farsi":19, "science":18, "physicall_education":16,"Art": 19},
        {"name":"hassan","math":19, "farsi":18.5, "science":16, "physicall_education":15.5, "Art":18},
        {"name":"farank","math":12, "farsi":19,"science": 14.5, "physicall_education":16.5,"Art": 18},
        {"name":"sarah","science": 18.5, "math":17, "farsi":17,"physicall_education": 14, "Art":19.5}]
all_avg=[]
for grade in data:
    sum = grade["math"] + grade["farsi"] + grade["science"] 
    avg = sum / 3
    print(avg,grade["name"])
    all_avg.append(avg)
all_avg.sort()
print(all_avg)
print("the best avg",all_avg[-1],grade["name"])
print("the wort avg",all_avg[0], grade["name"])

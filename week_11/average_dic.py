def sort_best_grade(student)->float:
    return sorted(student.values(), reverse=True)

data = [{"math": 13.5, "science":18, "physicall_education":17, "Art":10, "farsi": 14 },
        {"math":13, "farsi":19, "science":18, "physicall_education":16,"Art": 19},
        {"math":19, "farsi":18.5, "science":16, "physicall_education":15.5, "Art":18},
        {"math":12, "farsi":19,"science": 14.5, "physicall_education":16.5,"Art": 18},
        {"science": 18.5, "math":17, "farsi":17,"physicall_education": 14, "Art":19.5}]


for grade in data:
    sum = grade["math"] + grade["farsi"] + grade["science"] + grade["physicall_education"] + grade["Art"]
    avg = sum / 5
    print(avg)

for grade in data:
    print(grade.values())
    print(sort_best_grade(grade)[0])
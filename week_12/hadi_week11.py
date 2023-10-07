data = [{"math": 13.5, "science":18, "physicall_education":17, "Art":10, "farsi": 14 },
        {"math":13, "farsi":19, "science":18, "physicall_education":16,"Art": 19},
        {"math":19, "farsi":18.5, "science":16, "physicall_education":15.5, "Art":18},
        {"math":12, "farsi":19,"science": 14.5, "physicall_education":16.5,"Art": 18},
        {"science": 18.5, "math":17, "farsi":17,"physicall_education": 14, "Art":19.5}]

sum = 0
sum1 = 0
sum2 = 0
for best_grade in data:
    sum = sum + best_grade["math"] 
    sum1= sum1 + best_grade["farsi"]
    sum2= sum2 + best_grade["science"]
print("math avg for the whole class", sum/len(data))
print("farsi avg for the whole class",sum1/len(data))
print("science avg for the whole class",sum2/len(data))
all_sums = [sum,sum1,sum2]
all_sums.sort()
print(all_sums)


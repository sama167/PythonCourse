# write a program to calculate each student's average of three subjects (math, farsi and science),
#  then sort the average and print the worst and best average in the output.

def my_sort(member):
    return member["average"]

data = [{"name":"ali","math": 13.5, "science":18, "physicall_education":17, "Art":10, "farsi": 14 },
        {"name":"mamad","math":13, "farsi":19, "science":18, "physicall_education":16,"Art": 19},
        {"name":"hassan","math":19, "farsi":18.5, "science":16, "physicall_education":15.5, "Art":18},
        {"name":"farank","math":12, "farsi":19,"science": 14.5, "physicall_education":16.5,"Art": 18},
        {"name":"sarah","science": 18.5, "math":17, "farsi":17,"physicall_education": 14, "Art":19.5}]

all_avg = []

for student in data:
    sum = student["math"] + student["farsi"] + student["science"]
    avg = sum/3
    name = student["name"]
    print(student["name"], " has avg ", avg)
    all_avg.append({"average": avg, "username": name})

print(all_avg)

all_avg.sort(key=my_sort)
print(all_avg)
print("best avg ", all_avg[-1])
print("worst avg ", all_avg[0])
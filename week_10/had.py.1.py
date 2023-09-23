

def mon(y):
  return y["family size"]



data1=[({"name":"Hamed","age": 39, "family size":3, "number of childern":1,"income": 550,"city": "tehran"}),
       ({"name":"Sara", "age": 41,"family size": 2,"number of childern": 1,"income": 370, "city":"tehran"}),       
       ({"name":"Paria","age": 23,"family size": 3,"number of childern": 1, "income":600, "city":"karaj"}),       
        ({"name":"Ahmad", "age":29,"family size": 2,"number of childern": 0,"income": 810,"city": "qazvin"}),       
        ({"name":"Matin","age": 35,"family size": 4,"number of childern": 2, "income":430,"city": "tehran"}),       
        ({"name":"Sina", "age":29, "family size":3,"number of childern": 2, "income":190, "city":"qazvin"}),       
        ({"name":"Hooman","age": 33, "family size":4, "number of childern":2, "income":450,"city": "tehran"}),       
        ({"name":"Mehdi","age": 43,"family size": 5,"number of childern": 3, "income":520,"city": "tehran"}),       
        ({"name":"Mehran", "age":46,"family size": 4, "number of childern":2, "income":490,"city": "karaj"}),
        ({"name":"Javad","age": 42,"family size": 4,"number of childern": 2, "income":640,"city": "tehran"})]



a=data1.sort(key=mon)
# print(data1)
data2=[100,100,150,150,150,200,50,0,0,]
data3=data1+data2
print(data3)
for x in data3:
  print(x)
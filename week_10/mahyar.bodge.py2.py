
import time

def mon(y):
  return y["income"]

list=[({"name":"Hamed","age": 39, "family size":3, "number of childern":1,"income": 200,"city":"tehran"}),
      
     ({"name":"Sara", "age": 41,"family size": 2,"number of childern": 1,"income": 150, "city":"tehran"}), 

       ({"name":"Paria","age": 23,"family size": 3,"number of childern": 1, "income": 200, "city":"karaj"}),  

        ({"name":"Ahmad", "age":29,"family size": 2,"number of childern": 0,"income": 100,"city":"qazvin"}),
         
        ({"name":"Matin","age": 35,"family size": 4,"number of childern": 2, "income":300,"city": "tehran"}),
        
        ({"name":"Sina", "age":29, "family size":3,"number of childern": 2, "income":250, "city":"qazvin"}),   

        ({"name":"Hooman","age": 33, "family size":4, "number of childern":2, "income":300,"city": "tehran"}),  

        ({"name":"Mehdi","age": 43,"family size": 5,"number of childern": 3, "income":400,"city": "tehran"}),   

        ({"name":"Mehran", "age":46,"family size": 4, "number of childern":2, "income":300,"city": "karaj"}),

        ({"name":"Javad","age": 42,"family size": 4,"number of childern": 2, "income":300,"city": "tehran"})]



list.sort(key=mon)
print(list)


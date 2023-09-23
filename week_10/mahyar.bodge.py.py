import time
def mon(y):
    return y[0] #income

           
#            #name,age,family size,num of kid, city
# my_list = [ ("hamed",39,3, 1, "income":200,"tehran"),
           
#             ("sara" ,41 , 2 , 1, "income":150 ,"tehran"),

#             ("Paria", 23,3,1, "income":200,"karaj"),  

#             ("Ahmad",:29, 2, 0,"income":100,"qazvin"),
         
#             ("Matin",35, 4, 2, "income":300, "tehran"),
        
#             ("Sina", :29, 3, 2, "income":250, "qazvin"),   

#             ("Hooman", 33, 4, 2, "income":300, "tehran"),  

#             ("Mehdi", 43, 5, 3, "income":400, "tehran"),   

#             ("Mehran",46,4, 2, "income":300,"karaj"),

#             ("Javad",42 ,4, 2,"income":300,"tehran") ]

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
time.sleep
data.sort(key=mon)
print(data)
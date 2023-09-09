mylist = []
my_dict = {}


#1 16 mylist = [16]
#1 10 mylist = [16, 10, 74]

# ['10']
# [10]

while True:
  a=input("enter number")
  b=int(a)
  
  if b <= 0:
      print("you lost")
      break
  

  mylist.append(b)
  print(mylist)

s = 0
for f in mylist:
   s = s + f

print(f"sum is {s}")


my_list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
print(len(my_list))
for number in  my_list :
    if number % 4==0:
        my_list.remove(number)

print(my_list)
print(len(my_list))

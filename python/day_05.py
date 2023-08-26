# fruits = ["Apple","Peach","Pear"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " Pie")

#---------------------------------------------------------------------------------
# total = 0
# for number in range(1,101):
#     # print(number)
#     total+= number
# print(total)

#-----------------------------------------------------------------------------------
total = 0
for number in range (0,101,2):
    total+=number
print(total)
# or
total_2 = 0
for number in range (1,101):
    if number % 2 == 0:
        total_2 +=number
print(total)
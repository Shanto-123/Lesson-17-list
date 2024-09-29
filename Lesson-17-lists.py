grocery_list =['bread','potatoes','rice','milk']
grocery_list[1]='oill'
print(grocery_list)
print(grocery_list[-1])
print(grocery_list[2])
print(grocery_list[1:2])


price = [5,10,15,4]
max = price[0]
for value in price:
    if value>max:
        max = value
print(max)

# Task 1: working with Strings
food = 'burgers'
print(food[0:3])
print(food[-3:-1])
first_last = food[0] + food[-1]
food_list = food.split()
print(food_list)
joined_food = ' '.join(food_list)
print(joined_food)
# Task 2: Working with Lists
number_list = [1, 7675647456, 32,-5, 0, 234,]
number_list.append(67)
# print(number_list)
number_list.insert(3,1000)
# print(number_list)
number_list.pop(-5)
print(number_list)
number_list.remove(7675647456)
print(number_list)

# task 3: Dictionaries (key : value)
books = {'Dr Seuss' :'How the Grinch Stole Christmas!','William  Shakespere':'Romeo and Juliet'}
keys_list = ('Dr Seuss','William Shakespere')
print(keys_list)
values = ('How the Grinch stole Christmas!','Romeo and Juliet')
print(values)
get = ('Romeo and Juliet')
print(get)
pop = ('How the Grinch stole Christmas')
print(pop)
del('Dr Seuss')

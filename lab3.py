# Task 1: working with Strings
food = 'burgers'
print(food[0:3])
print(food[-3:])
first_last = food[0] + food[-1]
food_list = food.split()
print(food_list)
joined_food = ' '.join(food_list)
print(joined_food)
# Task 2: Working with Lists
number_list = [1, 7675647456, 32, -5, 0, 234]
number_list.append(67)
# print(number_list)
number_list.insert(3,1000)
# print(number_list)
number_list.pop()
print(number_list)
number_list.remove(7675647456)
print(number_list)
print(number_list[0:3])
print(number_list[-3:]) 
# Task 3: Dictionaries (key : value)
books = {'Dr Seuss' :'How the Grinch Stole Christmas!','William  Shakespere':'Romeo and Juliet','Stan Lee' :'Marvel Comics', 'Hidenori Kusaka': 'Pokemon Adventures'}
keys_list = ('Dr Seuss','William Shakespere')
print(keys_list)
values = ('How the Grinch stole Christmas!','Romeo and Juliet','Marvel Comics','Pokemon Adventures')
print(values)
get = ('Romeo and Juliet')
get = ('Marvel Comics')
print(get)
pop = ('How the Grinch stole Christmas')
pop = ('Pokemon Adventures')
print(pop)
del books['Dr Seuss']


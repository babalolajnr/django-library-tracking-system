import random
rand_list = [random.randint(1, 100) for _ in range(10)]
print(rand_list)

list_comprehension_below_10 = [num for num in rand_list if num < 10]
print(list_comprehension_below_10)

list_comprehension_above_10 = [num for num in rand_list if num > 10]
print(list_comprehension_above_10)

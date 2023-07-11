def filter_integers_for(my_list):
    result = []
    for item in my_list:
        if isinstance(item, int):
            result.append(item)
    return result

# Пример использования
my_list = [1, 2, '3', 4, 'name', 10, 33, 'Python']
filtered_list = filter_integers_for(my_list)
print(filtered_list)



def filter_integers_comprehension(list):
    return [item for item in list if isinstance(item, int)]


# Пример использования
my_list = [1, 2, '3', 4, 'name', 10, 33, 'Python']
filtered_list = filter_integers_comprehension(my_list)
print(filtered_list)


def filter_integers_filter(my_list):
    return list(filter(lambda x: isinstance(x, int), my_list))


# Пример использования
my_list = [1, 2, '3', 4, 'name', 10, 33, 'Python']
filtered_list = filter_integers_filter(my_list)
print(filtered_list)
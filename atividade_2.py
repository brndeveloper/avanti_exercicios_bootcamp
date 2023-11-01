def one_in_two(list1, list2):
    one_in_two_list = []
    for element_1 in list1:
        if element_1 not in list2 and element_1 not in one_in_two_list:
            one_in_two_list.append(element_1)
    if len(one_in_two_list) == 0:
        return 'As listas não '
    return f'Lista com elementos diferentes: {one_in_two_list}'

print(one_in_two([3, 5, 6, 1, 2, 3], [2, 1, 8, 6, 5, 9, 3]))
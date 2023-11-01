def one_in_two(list1, list2):
    one_in_two_list = []
    for element_1 in list1:
        if element_1 not in list2 and element_1 not in one_in_two_list:
            one_in_two_list.append(element_1)
    return f'Lista com elementos diferentes: {one_in_two_list}'

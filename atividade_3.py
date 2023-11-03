def second_biggest_number(list_number):
    last_number = 0
    second_number_big = 0
    for number in list_number:
        if number > last_number:
            second_number_big = last_number
            last_number = number
    return second_number_big  

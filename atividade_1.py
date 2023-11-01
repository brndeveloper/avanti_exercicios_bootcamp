def prime_numbers(list_numbers):
    prime_numbers_list = []
    for number in list_numbers:
        counter = 0
        for num in range(1, (number + 1)):
            if number % num == 0:
                counter += 1
        if counter == 2:
            prime_numbers_list.append(number)
    if len(prime_numbers_list) == 0:
        return 'Não há números primos na lista.'
    return f'Números primos: {prime_numbers_list}'

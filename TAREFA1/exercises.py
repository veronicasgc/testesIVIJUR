def numbers_list():
    numbers = [18, 37, 65, 82, 48, 72, 53]
    new_list = [number * 2 for number in numbers if number % 2 == 0]
    
    print(new_list)

numbers_list()



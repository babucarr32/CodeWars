def expanded_form(num):
    newNum = []

    for index, number in enumerate(str(num)[::-1]):
        if number != '0':
            newNum.append(number + ('0' * index))
    return '+ '.join(newNum[::-1])
print(expanded_form(512))
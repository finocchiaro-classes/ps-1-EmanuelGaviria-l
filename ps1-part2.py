def number_fun(a, b):
    print(f'You entered {a} and {b}')
    print(f'{a} + {b} = {a + b}')
    print(f'{a} * {b} = {a * b}')
    print(f'{a} ** {b} = {a ** b}')
    print(f'{a} % {b} = {a % b}')

firstnum = int(input('Please enter an integer number between 10 and 100: '))
if firstnum < 10 or firstnum > 100:
    print('The number has to be in the range of 10 to 100')
else:
    secondnum = int(input('Please enter an integer number that is less than 4: '))
    if secondnum >= 4:
        print('The number has to be less than 4')
    else:
        number_fun(firstnum, secondnum)

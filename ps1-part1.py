firstnum = int(input('Please enter a whole number between 10 and 100: '))
if firstnum < 10 or firstnum > 100:
    print('The number has to be in the range of 10 to 100')
else:
    secondnum = int(input('Please enter a whole number that is less than 4: '))
    if secondnum > 4:
        print('The number has to be less than 4')
    else:
        print(f'You entered {firstnum} and {secondnum}')
        print(f'{firstnum} + {secondnum} = {firstnum + secondnum}')
        print(f'{firstnum} * {secondnum} = {firstnum * secondnum}')
        print(f'{firstnum} ** {secondnum} = {firstnum ** secondnum}')
        print(f'{firstnum} % {secondnum} = {firstnum % secondnum}')
        

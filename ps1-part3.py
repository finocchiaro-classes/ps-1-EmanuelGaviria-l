def heart_rate(age,goal):
    max_HR = 220 - age
    print(f'Your max heart rate is: {max_HR}')
    
    if goal.upper() == 'S':
        s1 = max_HR * 0.8
        s2 = max_HR * 1.0
        print(f'Your target heart rate range from {s1} to {s2}')
        
    elif goal.upper() == 'E':
        e1 = max_HR * 0.6
        e2 = max_HR * 0.8
        print(f'Your target heart rate range from {e1} to {e2}')
        
    else:
        print('Only enter S for speed or E for endurance as your goal.')
        
    return(age, goal)

user_age = int(input('Please enter your age: '))
user_goal = input('Enter S if your goal is speed, or E if endurance: ')

heart_rate(user_age, user_goal)


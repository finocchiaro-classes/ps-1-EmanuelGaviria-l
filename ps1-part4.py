prior_arrests = int(input('Please enter the number of prior arrests: '))
local_ordinance = input('Is there any prior arrests for local ordinance?(Y/N): ')
age_at_release = int(input('What is the age of the individual at realese time?: '))

recidivism_score = 0

if prior_arrests >= 2:
    recidivism_score+=1
if prior_arrests >= 5:
    recidivism_score+=1
if local_ordinance.upper() == 'Y':
    recidivism_score+=1
if age_at_release >= 18 and age_at_release <= 24:
    recidivism_score+=1
if age_at_release >= 40:
    recidivism_score = recidivism_score - 1

print(f'The recidivism risk score is: {recidivism_score}')


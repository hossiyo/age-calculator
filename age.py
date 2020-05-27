a=float(input('How old are you? (number please):  '))
                
age_in_days= a * 365
age_in_months= a * 12



while a <= 0 :
    print('please enter a number grater than 0 ')
    a=float(input('How old are you? (number please):  '))


else:
    print('You have lived for', age_in_months, 'months ')

    print('and')

    print('You have lived for', age_in_days, 'days')










a=input('How old are you? (number please):  ')

while(1):
    try:
        age=float(a)
        age_in_days= age * 365
        age_in_months= age * 12
        print('\nYou have lived for', round (age_in_months), 'months ')

        print('and')

        print('You have lived for', round(age_in_days), 'days\n')
        break
        
    except ValueError:
        print ("please give me a number")
        a=input('How old are you? (number please):  ')


        
    



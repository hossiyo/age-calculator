#here you give your age
a=input('How old are you? (number please):  ')

#calculater
while(1):
    try:
        age=float(a)                                                       #     converts it to float
        age_in_days= age * 365
        age_in_months= age * 12
        print('\nYou have lived for', round (age_in_months), 'months ')    #     prints the results

        print('and')                                                       #     prints the results

        print('You have lived for', round(age_in_days), 'days\n')          #     prints the results
        break
        
    except ValueError:                                                     #     exception if you enter string
        print ("please give me a number")
        a=input('How old are you? (number please):  ')




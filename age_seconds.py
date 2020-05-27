def age_seconds():
    age=int(input('Enter your age:'))
    print("You have lived {} seconds!!!".format(age*365*24*60*60))
# age_seconds()
def age_program():
    seconds_or_years=input('Give me seconds (s) or yeasrs (y)?:')
    if seconds_or_years == 's':
        user_value=input('Enter no of seconds you have lived for:')
        print('you have lived for {} years'.format(int(user_value)/60/60/24/365))
    elif seconds_or_years =='y':
        user_value=input("Enter the number of years you've lived for: ")
        print("yu have lived for {} seconds".format(int(user_value)*365*24*60*60))
age_program()

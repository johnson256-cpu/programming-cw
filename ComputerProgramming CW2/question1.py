
#QUESTION PART A the program calculates and informs you your birth year basing on the age
try:#testing for errors
    print("welcome\n am praxy your day's guide".center(1))
    name=input('\nENTER YOUR NAME please: ') #inserting user input
    print(f'hello {name.upper()},thats a lovely name and quite different\n') #greating the user with a given name as per the input
    age,current_year=int(input('lets know your age AGE please:')),2024 #multiple variable initialisation
    birth_year=current_year-age # obtaining users birth year
    if birth_year<2000: 
        print('mmmmmm a melenial baby \n   o   o\n     -\n   \___/')
    elif birth_year<2015:
        print('wow, so your are a Gen z ,\nthis is interesting, lets move on')
    else:
        print('your the ALFAs\n i wonder how that(life)')
    print('btw your birth year is: ', birth_year) # result of the user birth year 
    number=int(input(f'\n {name.upper()} can we know your favourite number: ')) #entering user input that is an integer
    if (number%2)==0: # incace what the user inputs is divisible by 2 and has no remender 
        print('your favourite number is an even number') # then the input is an even integer
        #nested if checking where the number lies basing on 10   
        if number<10:
            print('and quite basic as its below 10')
        elif number==10:
            print('and quite unsual as its the lucky digit 10')
        else:
            print('and obvious that its above 10')
    else:
        print('your favourite number is an odd number') #otherwise its an odd integer
        if number<10:
            print('and quite basic as its below 10')
        elif number==10:
            print('and quite unsual as its the lucky digit 10')
        else:
            print('and obvious that its above 10')
except ValueError:#incase an input is not an interger
    print('value input is not a number') # the output incase of an error



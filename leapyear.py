a=int(input('Enter the year: ' ))
if a%4==0:
    if a%400==0:
        print 'The given year is not leap year'
    else:
        print 'The given year is a leap year'
else:
    print 'The given year is a leap year'

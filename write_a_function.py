'''
Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.

Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. It is only necessary to complete the is_leap function.
'''
def is_leap(year):
    active=False
    if year%4==0 and year%100!=0:
        active=True
    elif year%400==0 :
        active=True
    elif year%100==0:
        active=False
    return active


year = int(input())
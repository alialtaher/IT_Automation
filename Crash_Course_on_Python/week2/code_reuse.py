#Ready to try it yourself? See if you can reduce the code duplication in this script.
#In this code, 
# identify the repeated pattern and replace it with a function called month_days, 
# that receives the name of the month and the number of days in that month as parameters. 
# Adapt the rest of the code so that the result is the same. 
# Confirm your results by making a function call with the correct parameters for both months listed.
# REPLACE THIS STARTER CODE WITH YOUR FUNCTION
from calendar import month


def month_days(month,days_in):
    print(str(month)+" has " + str(days_in) + " days.")
#june_days = 30
#july_days = 31
#print("July has " + str(july_days) + " days.")
month_days("june",30)
month_days("july",31)

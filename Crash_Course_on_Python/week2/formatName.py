# Complete the body of the format_name function.
# This function receives the first_name and last_name parameters
# and then returns a properly formatted string.
# Specifically:

# If both the last_name and the first_name parameters are supplied,
# the function should return like so:
# print(format_name("Ella", "Fitzgerald"))
# Name: Fitzgerald, Ella
# If only one name parameter is supplied (either the first name or the last name) , the function should return like so:
# print(format_name("Adele", ""))
# Name: Adele
# or
# print(format_name("", "Einstein"))
# Name: Einstein
# Finally, if both names are blank, the function should return the empty string:
# print(format_name("", ""))

def format_name(first_name, last_name):
    if(len(first_name)>0 and len(last_name)):
        return(last_name+", "+first_name)
    elif(len(first_name)>0 and len(last_name)<1):
        return(first_name)
    elif(len(first_name)<1 and len(last_name)>0):
        return(last_name)
    else:
        return("")
	
print(format_name("Ernest", "Hemingway"))
print(format_name("", "Madonna"))
print(format_name("Voltaire", ""))
print(format_name("", ""))

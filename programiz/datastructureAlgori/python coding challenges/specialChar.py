# Complete the function below

# define a function
def character_counter(string):

    # initialize the counter variable
    counter = 0

    # loop through the string
    for character in string:

        # if the character is not alphabet, not digit and not space, then increment the counter
        if not character.isalpha() and not character.isdigit() and not character.isspace():
            counter += 1

    # return the counter
    return counter


# call the function
string = input()
result = character_counter(string)
print(result)
 
 
 
 

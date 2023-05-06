# replace ___ with your code

# define a function that counts the capital letters in a string
def count_capitals(string):

    # initialize a counter
    capital_counter = 0

    # loop through the string
    for character in string:

        # take the ASCII value of the character and
        # check if it is a capital letter
        if ord(character) >= 65 and ord(character) <= 90:
            capital_counter += 1 

    # print the counter
    print(capital_counter)


# call the function
count_capitals('The Sun emits UV light')
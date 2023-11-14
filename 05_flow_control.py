# Flow control is a method of determining if the information
# provided in your code can be ran against "true", "false", "if", "or", "and" logic
# or boolean logic. Is it a weekday (yes/no) is the sky blue(yes/no)
# these are simple expressions that control what the next steps
# are that your system or code will take.  If yes then do this, if
# no then do this instead.

# Relational operators are use to compare to items and return a true / false
# response. 

# This == is a comparison to determine if the two compared items are equal. 

print(1 == 2)

# You will get a False in your terminal because 1 is not equal to 2

# This != is not equals too and is used to determine if the items are not equal.

print(1 != 2)

# You will get a True in your terminal because 1 is not not equal to 2. 

# because python is case sensitive make sure the items you are comparing are the same type
# and can be compared.  

print('7' == 7)

# this will return false because the str 7 is not equal to the int 7.

# There are multiple ways to assign boolean logic to variables. you can simply assign
# True or False to a variable or have your variable 

true_var = True 
false_var = False

# These variables dont process information or compare they are simply True or False statements. 

# You can add boolean logic to variables and have it store the results of True or False

bool_one = 8 != 10
bool_two = 5 + 5 != 20
bool_three = 10 * 10 == 100

# Now if you print() these values you will see True / False statements. 

print(bool_one)
print(bool_two)
print(bool_three)


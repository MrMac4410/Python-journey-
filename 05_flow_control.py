# Flow control is a method of determining if the information
# provided in your code can be ran against "true", "false", "if", "or", "and", "not" 
# "else" logic or boolean logic. Is it a weekday (yes/no) is the sky blue(yes/no)
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

print("\n")

# Now if you print() these values you will see True / False statements. 

print(bool_one)
print(bool_two)
print(bool_three)

print("\n")

# All three of these when printed will display the results of the
# statements in each variable. 


# If statements are conditional expressions that take code and evaluates it to determine
# a value to check if its True or False. Lets do a simple if statement to determine if a
# user should be able to log into a computer.

user_var = "Mac"

if user_var == "Mac":
    print("You are authorized to log into this computer")
    
x_var = 20
y_var = 30

if x_var == y_var:
    print("These numbers are the same.")

# Notice the : at the end of the if statement, this tells the computer
# what to process after the if statement if the conditions are True. 

# Other relational operators are > greater than,  >= greater than or equal to
# < less than, or <= less than or equal too. 

age = 15

if age >= 18:
    print("No parental control required")

print("\n")
    
if age < 18:
    print("Parental Permission Required!")

print("\n")

if age >= 15:
    print("Authorized for PG13 Movies.")

print("\n")


# the if statements will take the age variable and use the relational
# operator to determine if it is True or False.  Base on the results it will follow
# the steps and print or not print the corresponding statements. 


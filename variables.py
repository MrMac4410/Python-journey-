# Variables are containers that hold informaiton,  you can assign
# numbers or intigers as well as strings to a variable.
# then call the variable instead of re-typing the same thing over
# and over again.  

first_string_var = "Hello, World!"
first_integer_var = 2

# When you add a string to a variable then make sure you use qoutes.
# intigers and nubmers do not need qoutes. use the print() to call 
# the varable to the terminal. 

print(first_string_var)
print(first_integer_var)

# You should see Hello, World! and the number 2 in your terminal.  
# Variables can be simple one lines or multi lines of text, arrays,
# or intigers.  

# to add multi line of text from a qoute or story from something you read
# you will use the triple qoute function

first_multi_string_var = """
The good news about comptuers is 
that they do what you tell them to.
The bad news is that they do what 
you tell them too. 
'Ted Nelson'
"""

# Now if i print() first_multi_string_var it will send the qoute
# and match the formating as best as it can.  

print(first_multi_string_var)


# Notice in all these variable examples i do not use qoutes to call
# the variable as they are not requried.  you simply type the variable
# name into the print() brackets. 

# Concatenate is a method used to combine multple things together.
# like strings or integers. 
# you can use concatenate to add multple strings together to form
# a sentence.  
# 
# Lets use the game Mad Libs as an example. We wil use concatenante
# as well as the input() function to gather words for the mad lib. 
# input() is a method used to interacte with a user/s.  when you add
# input() it will prompt the user to type in a response.  We will take
# these responses and add them to variables.  After we have gathered
# all ther requried inputs we will combine them into a sentence. 

name_var = input("What is your name?: ")
place_var = input("Name a place: ")
noun_var = input("Give a Noun: ")

# Now that we have all of our inputs, we are going to concatenante them all
# together to form a sentence and complete the mad lib. 
# to do this we are going to use the + symbol to add each variable from
# the users input to the mad_lib variable. 

mad_lib_var1 = "Please excuse " + name_var + " they are authorized to be at the " + place_var + " instead of the " + noun_var

# Take special note of the spacing before and after each sentence.
# if you do not add a space then your inputs and words will be combined
# when you print() mad_lib.  You can add spaces as shown above, or you can add
# them seperatly by concatenating blank space i.e.

mad_lib_var2 = "Please excuse" + " " + name_var + " " + "they are authorized to be at the" + " " + place_var + " " + "instead of the" + " " + noun_var
# This method seems very tedious to me so I choose to add spaces before
# or after my strings.  

print(mad_lib_var1)
print(mad_lib_var2)

# Both var1 and var2 are the same when sent to the terminal even though var2 contains
# more code.
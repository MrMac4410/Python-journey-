# So I learned some basics about variables and using the print function.
# now I am going to go over how to update a variable using the += function

# Since we just finished with the simple maths portion I will use some
# simple math functions here to show how to update a varible when using
# int's. 

# I think using a shopping list is a good example if adding item costs
# to a variable and haveing to total added along the way.  

# First create a emply variable with a cost of 0. 

total_price = 0

# Lets add some items to our shopping cart. 

melon = 3.50
cerial = 4.00
yogurt = 2.50
milk = 5.00

# Each one of these items represents their own variable but
# we want to combine them to a single variable to show the total cost

total_price += melon + cerial + yogurt + milk

print("\n")

print(total_price)

print("\n")

# Using the += method I can see that my total cost for the four items
# is 15.00 even.  But im not done shopping and forgot to get some 
# other items. 

toothpaste = 2.75
pit_stick = 3.25
shampoo = 4.00

total_price += toothpaste + pit_stick + shampoo

print(total_price)

print("\n")

# Because I am updating the variable it does not discard the existing
# contents of the variable, but using the += is telling python to take
# whatever I specify next and combine it.  when i use the + it
# applies simple addition to the variable.  

# Now lets apply a tax and head to checkout. 

tax_var = 3

total_price = total_price + tax_var % total_price
total_price_str = str(total_price)

print("Total: " + total_price_str)

print("\n")


# The total price for the items in my cart and tax came to a 
# total of 28.00 $


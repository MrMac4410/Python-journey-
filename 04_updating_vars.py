# So I learned some basics about variables and using the print function.
# now I am going to go over how to update a variable using the += function

# Since we just finished with the simple maths portion I will use some
# simple math functions here to show how to update a variable when using
# int's. 

# I think using a shopping list is a good example if adding item costs
# to a variable and having to total added along the way.  

# First create a empty variable with a cost of 0. 

total_price = 0

# Lets add some items to our shopping cart. 

melon = 3.50
cereal = 4.00
yogurt = 2.50
milk = 5.00

# Each one of these items represents their own variable but
# we want to combine them to a single variable to show the total cost

total_price += melon + cereal + yogurt + milk

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

# Updating variables can be done with more then just Int's.  you can
# also update str's in a variable as well. Instead of just having the
# cost of the items, I need an itemized receipt with descriptions of
# each items.  I am going to shorten this shopping list and not type
# descriptions for everything.


watermelon_des = """
Watermelon is grown in favorable climates from 
tropical to temperate regions worldwide for its large edible fruit,
which is a berry with a hard rind and no internal divisions, 
and is botanically called a pepo. The sweet, juicy flesh is 
usually deep red to pink, with many black seeds, although seedless 
varieties exist.
"""
watermelon_cost = 4.00

toothpaste_des = """
Toothpaste is a paste or gel dentifrice with complex composition
used with a toothbrush to clean and maintain the esthetics and 
health of teeth. Synthetic surfactants, mostly SLS, are 
incorporated as detergent/foaming agents in a concentration 
of 0.5%–2% [249]
"""
toothpaste_cost = 3.00

# Since I am using an itemized receipt I am going to use a new item_cost_var
# and add both the items des with their descriptions and a final total at the end. 


# We have to remember to change the int's to str's if we are going to
# add them to a variable with other str's. 

itemized_receipt_total = 0.0
itemized_receipt_total += watermelon_cost + toothpaste_cost
itemized_receipt_total_pre_tax = watermelon_cost + toothpaste_cost
itemized_tax = .4
itemized_receipt_tax = itemized_receipt_total * itemized_tax
itemized_receipt_total = itemized_receipt_total + itemized_receipt_tax




watermelon_str_var = str(watermelon_cost)
toothpaste_str_var = str(toothpaste_cost)
itemized_receipt_total_pre_tax_str_var = str(itemized_receipt_total_pre_tax)
itemized_receipt_tax_str_var = str(itemized_receipt_tax)
itemized_receipt_total_str_var = str(itemized_receipt_total)


# Lets add all this together in one itemized receipt and try to
# make it look presentable. I just discovered that \ at the end of your code lets you continue the code on the new line. 
itemized_receipt = ""
itemized_receipt += "Itemized receipt" \
    + "\n" + watermelon_des + "\n"\
        + "Watermelon Price: " + watermelon_str_var + "\n" \
            + toothpaste_des + "\n"\
                + "Toothpaste Price: " + toothpaste_str_var + "\n" + "\n" \
                   + "Amount:" + itemized_receipt_total_pre_tax_str_var + "\n" \
                        + "Tax:   " + itemized_receipt_tax_str_var + "\n" \
                            + "Total: " + itemized_receipt_total_str_var

print(itemized_receipt)
print("\n")


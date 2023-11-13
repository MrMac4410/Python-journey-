# Python and comptuers in general are capable of performing simple
# and complex math functions. We can use integers and float numbers
# combined with variables to add subtract and other various mathmatical
# algorythms.

# An integer is any whole number like 50, 20, or 1

int_var = 1

# A float integer is any number that has a decimal 
# like 1.0, 34.02 or 4.3

int_float_var = 2.4

# You can use varaiables to perform simple math by adding them together.

combined_var = int_var + int_float_var

# then print the result

# I like to use the "\n" function to create new lines essentially its
# like hitting the enter key and going down one line. 
# its helps me organize and seperate each function thats being called
# as well as making the results more readable for me to understand.

print("\n")

print("Total:")
print(combined_var) 

print("\n")

# This will show the result of 1 + 2.4 = 3.4.  

# You can use variables and simple math to calculate percentages using
# python's Modulo % operator. Lets calcualte a discount off a sale
# at a local store.

order_num_1 = 100
order_discount = 13

# Now we have to calculate the discount by using modulo % with order 1
# to determin how much to take off the total price.
 
calculate_discount = order_discount % order_num_1

# Now we take the calculated discount and subtract it from the order 1
# amount and this will give you the customers total. 

cust_total = order_num_1 - calculate_discount

print("\n")

print("Original cost:")
print(order_num_1)
print("Total Discount:")
print(calculate_discount)
print("Cost After Discount:")
print(cust_total)

print("\n")

# You will notice I did not add the variable to the print to keep
# everything on one line.  That's because Python will not allow you to
# concatenate an integer into a string i.e. print("Original cost: order_num_1").
# This will come back with an error stating you can only concatenate
# str (not "int") to str.
# The only way to do this is to change the int to a string variable
# before concatenating and printing it at the end.

order_num_1_str = str(order_num_1)
calculate_discount_str = str(calculate_discount)
cust_total_str = str(cust_total)

# Now that I have trasformed the int's to str's i can print the totals
# on the same line with each other. I beleive this is primarily used
# to make reading and formating easier to understand and process. 

print("\n")

print("Original Cost: " + order_num_1_str)
print("Total Discount: " + calculate_discount_str)
print("Cost After Discount: " + cust_total_str)

print("\n")

# Now each total is presented after the : on the same line.
# you can mess with the spacing if you want to make it look cleaner
# for things like recepits where its nice to have the totals in the same
# row

print("\n")

print("Original Cost:       " + order_num_1_str)
print("Total Discount:      " + calculate_discount_str)
print("Cost After Discount: " + cust_total_str)

print("\n")

# You can use the "\n" new line function to add "enters" in the print() fuction
# just make sure you concatenate with the + "\n" + where you want your "enter" to go.


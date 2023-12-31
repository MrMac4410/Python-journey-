# Lists in programming are a collection of data and one of many built-in data structures.
# that allow programmers to work with data in sequential order.

blank_list = []

# Lists can be blank and later populated with data by specifying the list var and empty []

# Lists can contain both str, int, float or boolean data. 

int_list = [61, 82, 90, 66]
str_list = ["Tom", "Tim", "Carl", "Donut"]
int_str_list = ["Tome", 61, "Tim", 82, "Carl", 90, "Donut", 66]


# Appending a list follows the same principals from previously covered append functions.
# using the .append() function will add the information in () to the end of a list. 

append_example = ["Donut didn't like the name Donut Holes"]
append_example.append("for her fan club")

# when you print append_example it will now include the .append() info at the end of the sentence. 
 
#append_example.remove(-1)
print(append_example)
# set is a un ordered collection of unique elements and it is mutable
# Mutable means:- we can change the elements inside the sets after creating

# Creating a set
# my_set = {'value1','value2','value3'}
# print(my_set)


# Example1:- Normal set
fruits = {"Apple","Banana","Mango","Orange","Guava"}
print(fruits)

# Set With Duplicates
fruits = {"Apple","Banana","Mango","Orange","Guava","Apple","Banana"}
print(fruits)

# Empty set Creation
# Wrong Way:-
empty_set = {}

# Correct Way Using keyword called set()
new_set = set()
print(type(new_set))

# Accessing Set items:
# Wrong Way
"""basket = {"Apple","Banana","Mango","Orange","Guava"}
print(basket[0])"""  #TyprError -> Because Set has no positions and unordered

# Correct way : Using Loops:-
"""basket = {"Apple","Banana","Mango","Orange","Guava"}
for fruits in basket:
    print(fruits)"""



# another Way using in operator
"""basket = {"Apple","Banana","Mango","Orange","Guava"}
print("Apple" in basket)
print("apple" in basket)""" # False Because Python is case Sensitive




# Set Methods:
# Add:- ADDs One element
# Syntax = s.add()

colors = {'red',"Yellow","Green"}
colors.add("orange")
print(colors)
colors.add("orange")
# update:- updates add multiple items to the set
colors.update(["green","orange"])
print(colors)

# Remove










































































































































































































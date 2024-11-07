# Using the dict constructor :-
tuple_data1 = (("a", 1), ("b", 2), ("c", 3))

# Convert tuple to dictionary using dict()
dictionary_data1 = dict(tuple_data1)

print(dictionary_data1)

#----------------------------------------------------------------#

# Using dictionary comprehension :-
tuple_data2 = (("d", 4), ("e", 5), ("f", 6))

# Convert tuple to dictionary using dictionary comprehension
dictionary_data2 = {key:value for key,value in tuple_data2}

print(dictionary_data2)
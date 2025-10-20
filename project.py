# Sample dictionary
test_dict = {'a': 2, 'b': 3, 'c': 2, 'd': 4, 'e': 2}

# Value to check frequency of
check_val = 2

# Count frequency of the value
frequency = list(test_dict.values()).count(check_val)

# Display result
print("The frequency of value", check_val, "is:", frequency)
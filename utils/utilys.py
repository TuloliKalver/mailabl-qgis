import random
import string

# Function to generate a random string
def random_string(length=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

# Generate dummy data
false_items_c = [random_string() for _ in range(3)]
true_items_C = [random_string() for _ in range(3)]
false_values = [random.randint(1, 100) for _ in range(3)]
Row_indexes_and_cadastralUnits_properties = [
    {'index': random.randint(1, 10), 'number': random_string()} for _ in range(3)
]

# Print generated data
print("false_items_c:", false_items_c)
print("true_items_C:", true_items_C)
print("false_values:", false_values)
print("Row_indexes_and_cadastralUnits_properties:", Row_indexes_and_cadastralUnits_properties)

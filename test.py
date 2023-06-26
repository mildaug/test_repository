import json

# Prompt user for input
user_input = input("Enter your data: ")

# Store input in a dictionary
data = {"input": user_input}

# Write dictionary to JSON file
with open('output_data.json', 'w') as f:
    json.dump(data, f)
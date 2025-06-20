import json

# Write to file
new_data = {}
with open("data.json", "r") as file:
    data = json.load(file)
    for i in data:
        new_data[i] = data[i]

amount = float(input("Enter Amount : "))
new_data["received"] = amount

print(new_data)
person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"] #value is a list
person["pets"] = {"dog": "Fido", "cat": "Sox"} #value is another a dictionary

#print(person)

# print out the name of the second child
#first way using variable
# list_of_children = person['children']
# print(list_of_children[1])

#second way without variable
print(person["children"][1])


# print out the name of the cat
#first way with variable
# dict_of_pets = person['pets']
# print(dict_of_pets['cat'])

#second way without variable
print(person["pets"]['cat'])


# use a loop to print out the names of each child
for child in person['children']:
    print(child)



# use a loop to print out the pets in the following format:
# The type of pet is: dog and the name of the pet is: Fido

for pet,name in person["pets"].items():
    print(f"The type of pet is: {pet} and the name of the pet is: {name}")

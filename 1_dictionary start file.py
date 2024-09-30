import random

phonebook = {'Chris':'555−1111',
             'Katie':'555−2222',
             'Joanne':'555−3333'}



print()
print('*****  start section 1 - print dictionary ********')
print()

print(phonebook)

print(len(phonebook))

mydict = {} #creates empty dictionary
print(mydict)

mydict = dict(m=8, n=9) #also creates dictionary with key m value m and key n value 9
print(mydict)

mylist = [1,2,3,4]
print(type(mylist))

print(type(phonebook)) #type tells you what type of object it is

print()
print('*****  end section 1 ********')
print()




print()
print('*****  start section 2 - search dictionary ********')
print()

name = 'Chris'

if name in phonebook:
    phone = phonebook[name]
    print(phone)
else:
    print(f"{name} is not in the phonebook")


# phone = phonebook['Chris']
# print(phone)
#print(phonebook['Chris']) dont need variable





print()
print('*****  end section 2 ********')
print()





print()
print('*****  start section 3 - edit/append dictionary ********')
print()

print(phonebook)
phonebook['Joe'] = '555-0123' #since it doesn't exist in the dictionary, it will add it to the dictionary
phonebook['Chris'] = '555-4444' #when it exists in the dictionary, it will update it in the dictionary
print(phonebook)


print()
print('*****  end section 3 ********')
print()




print()
print('*****  start section 4 - delete/remove from dictionary ********')
print()

print(phonebook)
del phonebook['Chris'] #only works if it exists in the dictionary
print(phonebook)


print()
print('*****  end section 4 ********')
print()






print()
print('*****  start section 5 - iterate through keys, values, items ********')
print()

for key in phonebook:
    print(f"The name is {key} and the phone number is {phonebook[key]}")

for value in phonebook.values():
    print(f"The phone number is {value}")

for item in phonebook.items(): #returns a tuple
    print(item)

for k,v in phonebook.items(): 
    print(f"The name is {k} and the phone number is {v}")




print()
print('*****  end section 5 ********')
print()




print()
print('*****  start section 6 - using get and clear ********')
print()

phone = phonebook.get('Chris')
print(phone)


phonebook.clear()
print(phonebook)

print()
print('*****  end section 6 ********')
print()



print()
print('*****  start section 7 - using pop method ********')
print()

phone = phonebook.pop('Chris', 'not found')
print(phone)
print(phonebook)



print()
print('*****  end section 7 ********')
print()



print()
print('*****  start section 8 - using popitem ********')
print()


# a = phonebook.popitem()
# print(a)
# print(phonebook)



print()
print('*****  end section 8 ********')
print()


print()
print('*****  start section 9 - using random and converting to list ********')
print()

list_of_keys = list(phonebook)
print(list_of_keys)
random_key = random.choice(list_of_keys)
print(random_key)
phone = phonebook[random_key]
print(phone)

phone = phonebook[random.choice(list(phonebook))]
print(phone)


print()
print('*****  end section 9 ********')
print()







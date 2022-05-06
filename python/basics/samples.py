name = 'TEST'
age = 27

print(f'My name is  {name}')
print(f'I am  {age} years old')

print(name[0:3])

print(len(name))

print('python is awesome'.capitalize())

print('python is awesome'.upper())


print('PYTHON IS AWESOME'.islower())
print('PYTHON IS AWESOME'.isupper())

print('python is awesome'.replace('python', 'freeCodeCamp'))

print(' '.join(['python', 'is', 'awesome']))

print('python is awesome'.split(' '))


a = 10
b = 5

print(a//b) 

vowels = ['a', 'e']

vowels.append('i')
vowels.extend(['o', 'u'])

print(vowels)

vowels = ['a', 'i', 'o', 'u']

vowels.insert(1, 'e')

print(vowels)


vowels = ['a', 'e', 'i', 'o', 'u']

popped_item = vowels.pop()

print(popped_item)
print(vowels)


alpha = ['a','b']
alpha.append('c')
print(alpha)

for letter in alpha:
    print(letter.upper())



sentence = 'the quick brown fox jumped over the lazy dog'

record = {}

for letter in sentence:
    if letter in record:
        record[letter] += 1
    else:
        record[letter] = 1

print(record)


test = {}

test['abc'] = 1

print(test)
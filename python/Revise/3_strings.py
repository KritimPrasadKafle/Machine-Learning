food = 'samosa'
print(food[2])

print(food[-1])

print(food[0:2])

print(food[:2])

print(food[-3:-1])

print(food[-3:])

print(len(food))

myfood = 'samosa, jalebi'
print(myfood)

print("z" in myfood)

print("biryani" in myfood)

# myfood[0] = 'x'

print(myfood.replace('samosa', 'biryani'))
myfoodchanged = myfood.replace('samosa', 'hello')
print(myfoodchanged)

print(myfood.upper())
print(myfood.lower())

print(dir(myfood))

s = '145'
print(s.isdigit())

print('145z'.isdigit())

print(myfood.index('jalebi'))
print(myfood)

states = 7
text = "total states in Nepal:"
# print(text + states)

print(text+str(states))

texting = "let's learn python"
print(texting)

dialogue = "How many people were there? \
           sir so many"
print(dialogue)

dialogue = '''How many people were there? 
           sir so many'''
print(dialogue)

s = 'hey\nbro'
print(s)

e = 'hey\tbro'
print(e)

first = 'Paras'
last = 'Khadka'
print('The best cricket player:', first + ' ' + last)

print(f'The best cricket player {first} {last}')
message = "Booby's World"

message1 = 'Booby\'s World'  

print(message)
print(message1)

print(len(message))

print(len(message1))

#Accessing
print(message1[0])
print(message[4])

# Slicing
print(message[0:5])

print(message[:5])

print(message[:6])

#Method
print(message.lower())

print(message.count('o'))
print(message.count('Booby'))

print(message.find("Booby's"))

print(message.find('l'))


newmessage = message.replace('World', 'Universe')
print(newmessage)

greeting = 'Hello'
name = 'Michael'

message = greeting + ', ' + name + '. Welcome!'

message = '{}, {}. Welcome!'.format(greeting, name)

message = f'{greeting}, {name.upper()}. Welcome!'

print(message)

print(dir(name))

check = "fsdjkjkdsf    "

check1 = check.strip()
print(len(check1))
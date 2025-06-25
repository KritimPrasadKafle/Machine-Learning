import random

value = random.random()

value = random.uniform(1,10)

value = random.randint(1,6)

greetings = ['Hello', 'Hi', 'Hey', 'Howdy', 'Hola']
value = random.choice(greetings)

colors = ['Red', 'Black', 'Green']
results = random.choices(colors, k=10)
print(value)
print(results)

deck = list(range(1,53))

random.shuffle(deck)
hand = random.sample(deck, k=5)
print(hand)
print(deck)
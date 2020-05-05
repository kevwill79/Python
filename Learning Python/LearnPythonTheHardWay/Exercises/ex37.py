#Practice with Sets

basket = ['apple', 'orange', 'apple', 'pear', 'orange']
fruit = set(basket)
print(fruit)
print('orange' in fruit)
print('crabgrass' in fruit)

a = set('abracadabra')
b = set('alacazam')
print(a)
print(b)
print(a - b)
print(a | b)


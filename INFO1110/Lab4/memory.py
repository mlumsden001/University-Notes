spam = ['frosty', 'chocolate', 'milkshakes']
ham = [spam, ['glazed', 'raspberry', 'donuts']]

print(ham[0])
print(ham[0][1])

spam[1] = 'strawberry'
print(ham[0])
print(ham[0][1])

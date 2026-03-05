x = 33
y = 'apples'
z = "In the basket there are %d %s" % (x, y)

# %d e digit %s e string
print(z)


x = 'apples'
y = 'lemons'
z = "In the basket are {} and {}".format(x, y)

print(z)

price = 22.50
quantity = 5
total = 'The total cost is ${:.2f} for {} items.'.format(price * quantity, quantity)

print(total)
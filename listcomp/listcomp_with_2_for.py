colors = ['black', 'white']
sizes = ['S', 'M', 'L']

tshirts_1 = [(color, size) for color in colors
                           for size in sizes]

tshirts_2 = [(color, size) for size in sizes
                           for color in colors]

tshirts_3 = tuple(ord(size) for size in sizes)

print(tshirts_1)
print(tshirts_2)
print(tshirts_3)

print(*('size: {}, color: {}\n'.format(s, c) for c in colors for s in sizes))

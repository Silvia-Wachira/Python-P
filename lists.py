# supplies = ['crayons', 'pencils', 'paper', 'Kleenex', 'eraser']
# print(supplies)

# supplies.append('markers')
# print(supplies)

# supplies.remove('crayons')
# print(supplies)

# supplies.sort()
# print(supplies)

# supplies.sort(key=str.lower)
# print(supplies)

colors = ['red', 'orange', 'blue', 'pink']

alphabetical = sorted(colors)
print(colors)
print(alphabetical)

alphabetical = sorted(colors,reverse=True)
print(alphabetical)

reversedColors = reversed(colors)
reversedAlpha = reversed(alphabetical)

print(reversedColors)
print(reversedAlpha)

print(list(reversedColors))
print(list(reversedAlpha))

# pond = dict(
# depth= 10,
# area='210 square feet',
# fish=['Mary', 'Bob', 'Billy']
# )

# # print(pond)

# alligator = dict([
#     ('lifespan', 54),
#     ('length', 3.6),
#     ('lifespan', 54),
#     ('species', ['American alligator, Chinese alligator']),
#     ('funfact', "As an alligator's teeth are down, they are replaced."
#                 + "An alligator can go through 3,000 teeth in a life time"),
# ])
# print(alligator)


# keys = ['name', 'home-runs', 'strikeout', 'rbi']
# values = ['Babe Ruth', '7214', 1330, 2214]
# player = dict(zip(keys, values))
# print(dir(player))

spam = {'color': 'red', 'age': 42}
for v in spam.values ():
    print(v)

for k in spam.keys():
    print(k)


for k, v in spam.items():
    print('Key: ' + k + ' Value: ' + str(v))
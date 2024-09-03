# posts = [
#     {"title": "All Aout Lists", "tags": ("fun", "informative", "lists")},
#     {"title": "Tuple Troule", "tags": ("fun", "tuples")},
#     {"title": "Sparkling Sets", "tags": ("informative", "numers")},
# ]

# allTags = []
# for i in range(len(posts)):
#     print(posts[i] ["tags"])
#     allTags.extend(posts[i] ["tags"])

# print(allTags)
# allTags = list(set(allTags))
# allTags.sort()
# print(set(allTags)) 

newFruits = {"fig", "lemon", "cherry"}
print(newFruits)
for x in newFruits:
    print(x)

print("banana" in newFruits)
newFruits.add("orange")
print(newFruits)
newFruits.update(["mango", "grapes"])
print(newFruits)
print(len(newFruits))
newFruits.remove("fig")
print(newFruits)

x = newFruits.pop()
print(x)
print(newFruits)

newFruits.clear()
print(newFruits)

del newFruits
print(newFruits)

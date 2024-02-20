posts = [
    {"title": "All Aout Lists", "tags": ("fun", "informative", "lists")},
    {"title": "Tuple Troule", "tags": ("fun", "tuples")},
    {"title": "Sparkling Sets", "tags": ("informative", "numers")},
]

allTags = []
for i in range(len(posts)):
    print(posts[i] ["tags"])
    allTags.extend(posts[i] ["tags"])

print(allTags)
allTags = list(set(allTags))
allTags.sort()
print(set(allTags)) 
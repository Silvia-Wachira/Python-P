keys = ["age", "name","height"]
values = [32, "Corina", 1.4]

# d = {}
# for i in range(len(keys)):
#     d[keys[i].title()] = values[i]

d = { key: value for key, value in zip(keys, values)}

print(d)
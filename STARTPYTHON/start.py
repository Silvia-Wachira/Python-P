# print("Hello, World!")

# store_lambda = lambda x,y : x * y
# print(store_lambda(10,11))

# store_args = lambda x,y,z : x + y + z
# print(store_args(7,8,9))

def new_multiplied(k):
    return lambda x : x * k

new_double = new_multiplied(2)
new_triple = new_multiplied(3)

print(new_double(12))
print(new_triple(12))
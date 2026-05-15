def add_items(items, new_item):
    items.append(new_item)

names = ["Ivan", "Ivan"]
add_items(names, "Ivan")
print(names)

def add_one(x):
    x = x+1
    return x

n = 10
add_one(n)
print(n)

n = add_one(n)
print(n)

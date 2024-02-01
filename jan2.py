products = [
    ("Apple", 9),
    ("Mango", 12),
    ("Berry", 13)
]

# print(list(map(lambda item: item[1], products)))
filtered = [product for product in products if product[1] >= 10]
print(filtered)
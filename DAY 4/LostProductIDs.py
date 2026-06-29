product_IDs = input("Enter the product_IDs : ").split()
all_ids = set(product_IDs)
duplicates = set()

# find duplicates
for id in product_IDs:
    if product_IDs.count(id)>1:
        duplicates.add(id)

lost_ids = all_ids - duplicates
print("lost Product IDs :", lost_ids )        

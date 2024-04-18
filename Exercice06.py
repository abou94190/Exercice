def out_of_stock_products(database):
    # Filter out the out of stock products
    out_of_stock = [(prod_id, info) for prod_id, info in database.items() if info['quantity'] == 0]

    # Sort the out of stock products by price (descending) and then by ID (ascending)
    sorted_out_of_stock = sorted(out_of_stock, key=lambda x: (-x[1]['price'], x[0]))

    # Generate the list of out of stock products
    return sorted_out_of_stock

# Example product database
product_database = {
    1: {'name': 'Product A', 'price': 50, 'quantity': 0},
    2: {'name': 'Product B', 'price': 30, 'quantity': 5},
    3: {'name': 'Product C', 'price': 50, 'quantity': 0},
    4: {'name': 'Product D', 'price': 50, 'quantity': 0},
    5: {'name': 'Product E', 'price': 40, 'quantity': 30}
}

# Get the list of out of stock products sorted by price
out_of_stock_sorted = out_of_stock_products(product_database)

# Print the list of out of stock products
print("Out of stock products sorted by price (from most expensive to least expensive):")
for prod_id, info in out_of_stock_sorted:
    print(f"Product ID: {prod_id}, Name: {info['name']}, Price: ${info['price']}, Quantity: {info['quantity']}")

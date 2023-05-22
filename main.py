

# Product catalog
products = {
    "Product A": 20,
    "Product B": 40,
    "Product C": 50
}

# Discount rules
discount_rules = {
    "flat_10_discount": 10,
    "bulk_5_discount": 0.05,
    "bulk_10_discount": 0.1,
    "tiered_50_discount": 0.5
}

# Fees
gift_wrap_fee = 1
shipping_fee_per_package = 5
units_per_package = 10

# Function to calculate the discount amount based on the rules
def calculate_discount(quantity, rule):
    if rule == "flat_10_discount":
        return min(10, quantity)
    elif rule == "bulk_5_discount":
        return 0
    elif rule == "bulk_10_discount":
        return 0
    elif rule == "tiered_50_discount":
        return 0
    else:
        return 0

# Function to calculate the total price of a product
def calculate_product_total(quantity, price, is_gift_wrapped):
    gift_wrap_total = gift_wrap_fee * quantity if is_gift_wrapped else 0
    product_total = quantity * price + gift_wrap_total
    return product_total

# Function to calculate the subtotal
def calculate_subtotal(products_quantity):
    subtotal = 0
    for product, quantity in products_quantity.items():
        price = products[product]
        subtotal += calculate_product_total(quantity, price, False)
    return subtotal

# Function to calculate the discount
def calculate_discount_amount(products_quantity, subtotal):
    max_discount = 0
    discount_rule = None
    for product, quantity in products_quantity.items():
        price = products[product]
        for rule, rule_value in discount_rules.items():
            if rule == "bulk_5_discount" and quantity > 10:
                discount = quantity * price * rule_value
                if discount > max_discount:
                    max_discount = discount
                    discount_rule = rule
            elif rule == "bulk_10_discount" and sum(products_quantity.values()) > 20:
                discount = subtotal * rule_value
                if discount > max_discount:
                    max_discount = discount
                    discount_rule = rule
            elif rule == "tiered_50_discount" and quantity > 15 and sum(products_quantity.values()) > 30:
                discounted_quantity = quantity - 15
                discount = discounted_quantity * price * rule_value
                if discount > max_discount:
                    max_discount = discount
                    discount_rule = rule

    return discount_rule, max_discount

# Function to calculate the shipping fee
def calculate_shipping_fee(products_quantity):
    total_units = sum(products_quantity.values())
    total_packages = total_units // units_per_package
    remaining_units = total_units % units_per_package
    shipping_fee = total_packages * shipping_fee_per_package
    if remaining_units > 0:
        shipping_fee += shipping_fee_per_package
    return shipping_fee

# Function to calculate the total amount
def calculate_total(products_quantity, subtotal, discount_amount, shipping_fee):
    total = subtotal - discount_amount + shipping_fee
    return total

products_quantity = {}

for product in products:
    quantity = int(input(f"Enter the quantity of {product}: "))
    is_gift_wrapped = input(f"Is {product} wrapped as a gift? (yes/no): ").lower() == "yes"
    products_quantity[product] = quantity

subtotal = calculate_subtotal(products_quantity)
discount_rule, discount_amount = calculate_discount_amount(products_quantity, subtotal)
shipping_fee = calculate_shipping_fee(products_quantity)
total = calculate_total(products_quantity, subtotal, discount_amount, shipping_fee)

# Displaying the output
print("Product Details:")
for product, quantity in products_quantity.items():
    price = products[product]
    total_price = calculate_product_total(quantity, price, True)
    print(f"{product}: Quantity: {quantity}, Total: ${total_price}")

print(f"\nSubtotal: ${subtotal}")

if discount_rule is not None:
    print(f"Discount Applied: {discount_rule}, Amount: ${discount_amount}")
else:
    print("No discount applied.")

print(f"Shipping Fee: ${shipping_fee}")
print(f"Total: ${total}")

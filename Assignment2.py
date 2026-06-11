print("=" * 50)
print("     E-COMMERCE SYSTEM")
print("=" * 50)

# ------------------------
# LOGIN SYSTEM
# ------------------------

users = {
    "admin": {"password": "admin123", "role": "Admin"},
    "customer": {"password": "cust123", "role": "Customer"},
    "cashier": {"password": "cash123", "role": "Cashier"}
}

username = input("Enter username: ")
password = input("Enter password: ")

if username in users and users[username]["password"] == password:

    role = users[username]["role"]

    print("\nLogin Successful!")
    print(f"Welcome {username}")
    print(f"Role: {role}")

    # Access levels
    if role == "Admin":
        print("Access Level: Full Access")
    elif role == "Cashier":
        print("Access Level: Sales and Billing")
    else:
        print("Access Level: Customer Services")

    print("\n--- PRODUCT CHECKOUT ---")

    # ------------------------
    # INPUTS
    # ------------------------

    subtotal = float(input("Enter subtotal: "))

    location = input(
        "Enter location (Uganda/Kenya/Tanzania): "
    ).lower()

    coupon = input("Enter coupon code: ").upper()

    # ------------------------
    # TAX RATE BY LOCATION
    # ------------------------

    if location == "uganda":
        tax_rate = 0.18

    elif location == "kenya":
        tax_rate = 0.16

    elif location == "tanzania":
        tax_rate = 0.15

    else:
        tax_rate = 0.10
        print("Unknown location. Default tax applied.")

    # ------------------------
    # DISCOUNT BASED ON SUBTOTAL
    # ------------------------

    if subtotal >= 1000:
        discount_rate = 0.20

    elif subtotal >= 500:
        discount_rate = 0.10

    elif subtotal >= 200:
        discount_rate = 0.05

    else:
        discount_rate = 0

    # ------------------------
    # COUPON VALIDATION
    # ------------------------

    coupon_discount = 0

    if coupon == "SAVE10":
        coupon_discount = 0.10

    elif coupon == "SAVE20":
        coupon_discount = 0.20

    elif coupon == "":
        coupon_discount = 0

    else:
        print("Invalid Coupon Code!")

    # ------------------------
    # CALCULATIONS
    # ------------------------

    subtotal_discount = subtotal * discount_rate

    amount_after_discount = subtotal - subtotal_discount

    coupon_amount = amount_after_discount * coupon_discount

    amount_after_coupon = amount_after_discount - coupon_amount

    tax_amount = amount_after_coupon * tax_rate

    final_price = amount_after_coupon + tax_amount

    # ------------------------
    # RECEIPT
    # ------------------------

    print("\n" + "=" * 50)
    print("              RECEIPT")
    print("=" * 50)

    print(f"User:                    {username}")
    print(f"Role:                    {role}")
    print(f"Subtotal:                ${subtotal:.2f}")
    print(f"Location:                {location.title()}")
    print(f"Tax Rate:                {tax_rate*100:.0f}%")
    print(f"Subtotal Discount:       ${subtotal_discount:.2f}")
    print(f"Coupon Discount:         ${coupon_amount:.2f}")
    print(f"Tax Amount:              ${tax_amount:.2f}")
    print("-" * 50)
    print(f"Final Price:             ${final_price:.2f}")

else:
    print("Invalid username or password!")
import csv
import random

first_names = [
    "John", "Sarah", "Mike", "Jane",
    "David", "Mary", "Tom", "Grace"
]

cities = [
    "New York",
    "Boston",
    "Chicago",
    "Los Angeles",
    "Dallas"
]

with open("users.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(
        ["Name", "Email", "Age", "City", "Purchase_Amount"]
    )

    for i in range(1000):
        name = random.choice(first_names) + str(i)

        email = f"{name.lower()}@gmail.com"

        age = random.randint(18, 70)

        city = random.choice(cities)

        purchase = round(
            random.uniform(10, 500),
            2
        )

        writer.writerow(
            [name, email, age, city, purchase]
        )

print("1000 users generated.")
import random

countries = [
    "Brazil",
    "Portugal",
    "France",
    "England",
    "Spain",
    "Germany"
]

while True:

    print("\n==============================")
    print("   WORLD CUP 2026 PREDICTOR")
    print("==============================")
    print("1. Predict Winner")
    print("2. View Countries")
    print("3. Exit")

    choice = input("Choose option: ")

    if not choice.isdigit():
        print("Please enter a number.")
        continue

    if choice == "3":
        print("Exiting program...")
        break

    if choice == "2":
        print("\nParticipating Countries:")

        for country in countries:
            print(f"- {country}")

        continue

    if choice == "1":

        winner = ""
        highest_score = 0

        print("\nCountry Strength Scores")
        print("-----------------------")

        for country in countries:

            score = random.randint(80, 100)

            print(f"{country}: {score}")

            if score > highest_score:
                highest_score = score
                winner = country

            else:
                pass

        print("\nPrediction Result")
        print("------------------")
        print(f"Predicted World Cup Winner: {winner}")
        print(f"Strength Score: {highest_score}")

    else:
        print("Invalid option. Please choose 1, 2, or 3.")
        continue
# Project 3: Richter Scale; calculate eearthquake energy based on magnitude and display the results in a table format
# alongside real world examples.
# 10/2/2026
# Kingsley Wickstrom


def earthquakecat(magnitude):
# What category of earthquake is it based on the magnitude
    if magnitude < 2.0:
        return "Micro"
    elif magnitude < 3.0:
        return "Minor"
    elif magnitude < 4.0:
        return "Light"
    elif magnitude < 5.0:
        return "Moderate"
    elif magnitude < 6.0:
        return "Strong"
    elif magnitude < 7.0:
        return "Major"
    elif magnitude < 8.0:
        return "Great"
    else:
        return "Extreme"


def energyrel(magnitude):
#Calculate approximate energy released in joules from the Richter magnitude
    return 10 ** (4.4 + 1.5 * magnitude)


def main():
    print("Richter Scale Earthquake Calculator")

    try:
        magnitude = float(input("Enter the earthquake magnitude: "))
    except ValueError: # integer error handling for invalid input
        print("Please enter a valid number.")
        return

    if magnitude < 0:
        print("Magnitude cannot be negative.")
        return

    energy = energyrel(magnitude)
    category = earthquakecat(magnitude)

    print(f"\nEarthquake magnitude: {magnitude}")
    print(f"Earthquake category: {category}")
    print(f"Approximate energy released: {energy:,.2f} joules")

main()

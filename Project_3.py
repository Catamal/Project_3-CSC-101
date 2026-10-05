# Project 3 Richter Scale: calculate eearthquake energy based on magnitude and display the results in a table format
# alongside real world examples.
# 10/2/2026
# Kingsley Wickstrom


def energy_rel(magnitude):
# calculate approximate energy released in joules from the Richter magnitude.
    return 10 ** (4.8 + 1.5 * magnitude)


def main():
    try:
        magnitude = float(input("Enter the earthquake magnitude: "))
    except ValueError: # integer error handling for invalid input
        print("Please enter a valid number.")
        return

    if magnitude < 0:
        print("Magnitude cannot be negative.")
        return

    energy = energy_rel(magnitude)
    tnt = energy / 4_184_000_000  # 1 metric ton of TNT = 4.184e9 joules
    krakatoa = tnt / 10_000_000
    hiroshima = tnt / 100_000

    print(f"The earthquake's magnitude on the Richter scale: {magnitude}")
    print(f"A {magnitude:.4f} magnitude earthquake releases {energy:,.4f} joules of") # :.nf is the number of decimal places to display
    print("energy.")
    print(f"This is equivalent to {tnt:.4f} metric tons of exploded TNT.")
    print(f"This is equivalent to {krakatoa:.4f} Krakatoa eruptions and {hiroshima:.4f}")
    print("Hiroshima bombs")

main()
# Copyright 2025 Mikhail Ibrahim
# Date: Apr 6, 2025
# Description: A Python program that determines if a given year is a leap year,
# based on the leap year rules of divisibility by 4, 100, and 400.


def main():
    # Ask the user to input a year
    try:
        year = int(input("Enter a year: "))

        # Check if the year is divisible by 4
        if year % 4 == 0:
            # Check if the year is divisible by 100
            if year % 100 == 0:
                # Check if the year is divisible by 400
                if year % 400 == 0:
                    print(f"{year} is a leap year.")
                else:
                    print(f"{year} is not a leap year.")
            else:
                print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")

    except ValueError:
        print("Invalid input. Please enter a valid year.")


# Call the main function
if __name__ == "__main__":
    main()

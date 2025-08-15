fruits = {
    'apple': 10,
    'orange': 20,
    'banana': 30
}

while True:
    try:
        key = input("Enter a fruit name to lookup (Ctrl+C to exit): ").strip().lower()
        fruit = fruits[key]
    except KeyError:
        print(f"Error! '{key}' does not exist.")
    except KeyboardInterrupt:
        print("\nProgram stopped by user.")
        break
    else:
        print(f"The price of '{key}' is {fruit}.")
    finally:
        print("Ready for the next query...\n")

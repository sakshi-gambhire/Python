import requests

# Predefined list of supported currencies
CURRENCIES = {
    "USD": "United States Dollar",
    "EUR": "Euro",
    "INR": "Indian Rupee",
    "JPY": "Japanese Yen",
    "GBP": "British Pound",
    "AUD": "Australian Dollar",
    "CAD": "Canadian Dollar",
    "CHF": "Swiss Franc",
    "CNY": "Chinese Yuan",
    "SGD": "Singapore Dollar"
}

API_URL = "https://api.exchangerate-api.com/v4/latest/{}"

def fetch_exchange_rate(source_currency):
    """
    Fetch exchange rates for the given source currency from the API.

    Args:
        source_currency (str): The base currency code.

    Returns:
        dict: A dictionary of exchange rates.
    """
    try:
        response = requests.get(API_URL.format(source_currency))
        response.raise_for_status()
        data = response.json()
        return data['rates']
    except requests.exceptions.RequestException as e:
        print(f"Error fetching exchange rates: {e}")
        return None

def convert_currency(amount, rate):
    """
    Convert the amount using the given exchange rate.

    Args:
        amount (float): The amount to convert.
        rate (float): The exchange rate.

    Returns:
        float: The converted amount.
    """
    return amount * rate

def display_currencies():
    """
    Display the list of supported currencies.
    """
    print("\nSupported currencies:")
    for code, name in CURRENCIES.items():
        print(f"{code}: {name}")

def get_user_choice(prompt, valid_choices):
    """
    Prompt the user for a valid choice from the given options.

    Args:
        prompt (str): The input prompt message.
        valid_choices (list): A list of valid choices.

    Returns:
        str: The user's choice.
    """
    choice = input(prompt).upper()
    while choice not in valid_choices:
        print("Invalid choice. Please select from the list.")
        choice = input(prompt).upper()
    return choice

def main():
    """
    Main function to run the Currency Converter program.
    """
    print("💱 Welcome to the Currency Converter 💱")

    while True:
        display_currencies()

        source = get_user_choice("\nEnter source currency code: ", CURRENCIES.keys())
        target = get_user_choice("Enter target currency code: ", CURRENCIES.keys())

        try:
            amount = float(input(f"Enter amount in {source}: "))
            if amount < 0:
                raise ValueError("Amount cannot be negative.")
        except ValueError as e:
            print(f"Invalid amount: {e}")
            continue

        print("\nFetching latest exchange rates...🔄")
        rates = fetch_exchange_rate(source)

        if rates and target in rates:
            converted_amount = convert_currency(amount, rates[target])
            print(f"\n💰 {amount:.2f} {source} = {converted_amount:.2f} {target}\n")
        else:
            print("Conversion failed. Please try again later.")

        another = input("Do you want to convert another currency? (y/n): ").lower()
        if another != 'y':
            print("Thank you for using Currency Converter! 🌟")
            break

if __name__ == "__main__":
    main()

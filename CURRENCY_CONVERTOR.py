import requests

# Correct API Key (Only Key, Not the Full URL)
API_KEY = "3f9cf025178e75ad6a8c2e98"
BASE_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/"

def get_exchange_rate(base_currency, target_currency):
    """Fetch exchange rate from base_currency to target_currency."""
    url = BASE_URL + base_currency  # Correct URL formation
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data["conversion_rates"].get(target_currency, None)
    else:
        print("Error fetching data. Check your API key and connection.")
        return None

def convert_currency():
    """Get user input and convert currency."""
    try:
        amount = float(input("Enter amount: "))
        base = input("Enter base currency (e.g., USD): ").upper()
        target = input("Enter target currency (e.g., INR): ").upper()

        rate = get_exchange_rate(base, target)

        if rate:
            converted_amount = amount * rate
            print(f"{amount} {base} = {converted_amount:.2f} {target}")
        else:
            print("Conversion failed. Please check your input.")
    
    except ValueError:
        print("Invalid amount. Please enter a number.")

# Run the program
if __name__ == "__main__":
    convert_currency()

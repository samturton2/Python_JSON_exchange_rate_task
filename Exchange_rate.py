# Import json module
import json

# open the json file to read, and load it as a dictionary into a variable
with open("python_modules-main/exchange_rates.json", "r") as jsonfile:
        exchange_rates = json.load(jsonfile)

# Display data in exchange_rates
print(exchange_rates)

# Iterate through the exchange rates dictionary displaying the currencies and there exchange rates in a formatted table
print("| Currency | Exchange rate |")
print("|----------|---------------|")
print("| EUR      | 1.0000        |")
for currency, rate in exchange_rates['rates'].items():
    print(f"| {currency}      | {rate}" + (" " * (14 - len(str(rate)))) + "|")
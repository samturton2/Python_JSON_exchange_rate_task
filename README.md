# JSON exchange rate task

### Acceptance Criteria
- Create a new repo for this task
- .gitignore and readme in pycharm project
- Have the exchange rates json file available in the repo
- Display all the data from json file
- Iterate through the data and display the exchange rate by country

### Task
- create a new file in the same folder as the json exchange rates info
- In the folder import the json module, to convert the json data
```python
import json
```
- Open the json file to read, and load it as a dictionary into a variable using the .load function of the json module
```python
with open("exchange_rates.json", "r") as jsonfile:
        exchange_rates = json.load(jsonfile)
```
- Display data in exchange_rates, by printing it
- Iterate through the exchange rates dictionary displaying the currencies and there exchange rates in a formatted table
- You can format how you want but i have added in extra print files at the top to add collumn titles , and a base exchange rate of euros
```python
print("| Currency | Exchange rate |")
print("|----------|---------------|")
print("| EUR      | 1.0000        |")
for currency, rate in exchange_rates['rates'].items(): #for loop unpacking the dictionary
    print(f"| {currency}      | {rate}" + (" " * (14 - len(str(rate)))) + "|") # Optional spaces calculation, to make sure the columns are the same length despite the length of the rate float
```
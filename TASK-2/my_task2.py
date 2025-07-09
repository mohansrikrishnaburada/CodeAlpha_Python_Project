prices = {
    "AAPL": 180,
    "TSLA": 250,
    "NFLX": 400,
    "META": 290,
    "IBM": 160
}
portfolio = {}
total = 0

print("Welcome to your Stock Tracker!")
print("Stocks you can track:", ', '.join(prices.keys()))

while True:
    symbol = input("Enter a stock symbol (or 'exit' to finish): ").upper()
    if symbol == "EXIT":
        break
    if symbol not in prices:
        print("Stock not found, please try again.")
        continue

    quantity = input(f"How many shares of {symbol} do you have? ")
    if not quantity.isdigit():
        print("Please enter a valid number.")
        continue

    quantity = int(quantity)
    portfolio[symbol] = portfolio.get(symbol, 0) + quantity

print("\nYour Portfolio Summary:")
for stock, qty in portfolio.items():
    cost = prices[stock] * qty
    total += cost
    print(f"{stock}: {qty} shares × ${prices[stock]} = ${cost}")

print(f"Total value of your stocks: ${total}")

save = input("Save summary to file? (yes/no): ").lower()
if save == "yes":
    with open("portfolio.txt", "w") as file:
        file.write("Portfolio Summary\n")
        for stock, qty in portfolio.items():
            cost = prices[stock] * qty
            file.write(f"{stock}: {qty} shares × ${prices[stock]} = ${cost}\n")
        file.write(f"\nTotal Value: ${total}\n")
    print("Summary saved as portfolio.txt")
else:
    print("Summary not saved.")

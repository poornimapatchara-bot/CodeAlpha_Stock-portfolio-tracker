import csv

stock_prices = {
    "TCS": 3500,
    "INFY": 1500,
    "RELIANCE": 2800,
    "HDFCBANK": 1700,
    "WIPRO": 450
}

portfolio = {}
total_investment = 0

n = int(input("Enter the number of stocks: "))

for i in range(n):
    stock_name = input("\nEnter stock name: ").upper()
    if stock_name in stock_prices:
        quantity = int(input("Enter quantity: "))
        portfolio[stock_name] = quantity
    else:
        print("Stock not found in price list.")

print("\nPortfolio Summary")
print("-" * 30)

for stock, qty in portfolio.items():
    value = stock_prices[stock] * qty
    total_investment += value
    print(f"{stock}: {qty} shares × ₹{stock_prices[stock]} = ₹{value}")

print("-" * 30)
print(f"Total Investment Value = ₹{total_investment}")

choice = input("\nDo you want to save the result? (yes/no): ").lower()

if choice == "yes":
    file_type = input("Save as txt or csv? ").lower()

    if file_type == "txt":
        with open("portfolio.txt", "w") as file:
            file.write("Portfolio Summary\n")
            file.write("-" * 30 + "\n")
            for stock, qty in portfolio.items():
                value = stock_prices[stock] * qty
                file.write(f"{stock}: {qty} shares = ₹{value}\n")
            file.write(f"\nTotal Investment Value = ₹{total_investment}")
        print("Data saved in portfolio.txt")

    elif file_type == "csv":
        with open("portfolio.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Stock", "Quantity", "Price", "Value"])
            for stock, qty in portfolio.items():
                value = stock_prices[stock] * qty
                writer.writerow([stock, qty, stock_prices[stock], value])
            writer.writerow([])
            writer.writerow(["Total Investment", "", "", total_investment])
        print("Data saved in portfolio.csv")

    else:
        print("Invalid file type.")
else:
    pass

class StockMarketSystem:
    def __init__(self):
        self.portfolio = []

    def display_menu(self):
        print("--------------------------------------")
        print(" Welcome to Stock Market Trading System")
        print("---------------------------------------")
        print("1. Buy Stock")
        print("2. Sell Stock")
        print("3. View Portfolio")
        print("4. Search Stock")
        print("5. Quit")

    def buy_stock(self):
        print("-------------------------")
        print("Buy Stock")
        print("-------------------------")
        stock = {}
        stock['symbol'] = input("Enter Stock Symbol: ")
        stock['quantity'] = int(input("Enter Quantity: "))
        stock['price'] = float(input("Enter Price per Share: "))
        self.portfolio.append(stock)
        print("Stock bought successfully")

    def sell_stock(self):
        print("-------------------------")
        print("Sell Stock")
        print("-------------------------")
        symbol = input("Enter Stock Symbol to sell: ")
        quantity = int(input("Enter Quantity to sell: "))
        for stock in self.portfolio:
            if stock['symbol'] == symbol:
                if stock['quantity'] >= quantity:
                    stock['quantity'] -= quantity
                    print("Stock sold successfully")
                    return
                else:
                    print("Not enough shares to sell")
                    return
        print("Stock not found in portfolio")

    def view_portfolio(self):
        print("--- Portfolio ---")
        for stock in self.portfolio:
            print("Symbol:", stock['symbol'])
            print("Quantity:", stock['quantity'])
            print("Price per Share:", stock['price'])
            print("-----------------")

    def search_stock(self):
        symbol = input("Enter Stock Symbol to search: ")
        for stock in self.portfolio:
            if stock['symbol'] == symbol:
                print("Stock Found:")
                print("Symbol:", stock['symbol'])
                print("Quantity:", stock['quantity'])
                print("Price per Share:", stock['price'])
                return
        print("Stock not found in portfolio")

# Create an instance of the StockMarketSystem
stock_market_system = StockMarketSystem()

# Main loop for menu selection
while True:
    stock_market_system.display_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        stock_market_system.buy_stock()
    elif choice == '2':
        stock_market_system.sell_stock()
    elif choice == '3':
        stock_market_system.view_portfolio()
    elif choice == '4':
        stock_market_system.search_stock()
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")

print("-------------------------------")
print(" Thank you for using our system")
print("-------------------------------")

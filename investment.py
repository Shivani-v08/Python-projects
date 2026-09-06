print("===============================")
print("      INVESTMENT SIMULATOR     ")
print("===============================")

print("Hello! Start your investment journey with us.")
print("Please provide the following details to create your investment account.")
name = input("Enter your full name: ")
balance = float(input("Enter your initial balance: "))
account_type = input("Enter your account type (e.g., Savings, Checking): ")
sort_code = input("Enter your sort code: ")
account_number = input("Enter your account number: ")

# Create account function
def create_account(name, balance, account_type, sort_code, account_number):
    account = {
        "name": name,
        "balance": balance,
        "account_type": account_type,
        "sort_code": sort_code,
        "account_number": account_number,
        "assets": [],
        "transactions": []
    }
    return account

account = create_account(name, balance, account_type, sort_code, account_number)
print("Account created successfully! Here are your account details:")
print(f"Name: {account['name']}")
print(f"Balance: £{account['balance']:.2f}")
print(f"Account Type: {account['account_type']}")
print(f"Sort Code: {account['sort_code']}")
print(f"Account Number: {account['account_number']}")

#buy asset function
def buy_asset(account, asset_name, asset_type, quantity, price_per_unit):
    new_asset = {
        "asset_name": asset_name,
        "asset_type": asset_type,
        "quantity": quantity,
        "price_per_unit": price_per_unit
    }
    balance_needed = quantity * price_per_unit
    if account['balance'] >= balance_needed:
        account['balance'] -= balance_needed
        found = False
        for asset in account['assets']:
            if asset['asset_name'] == asset_name:
                asset['quantity'] += quantity
                found = True
                break
        if not found:
                account['assets'].append(new_asset)
        account['transactions'].append({
                "type": "buy",
                "asset_name": asset_name,
                "asset_type": asset_type,
                "quantity": quantity,
                "price_per_unit": price_per_unit,
                "total": balance_needed})
        
        print(f"Successfully purchased {quantity} units of {asset_name} at £{price_per_unit:.2f} each.")
    else:
        print("Insufficient balance to complete the purchase.")
    return account

#sell asset function
def sell_asset(account, asset_name, asset_type, quantity, price_per_unit):
    for asset in account['assets']:
         if asset['asset_name'] == asset_name and asset['asset_type'] == asset_type:
              if asset['quantity'] >= quantity:
                    asset['quantity'] -= quantity
                    account['balance'] += quantity * price_per_unit
                    account['transactions'].append({
                                    "type": "sell",
                                    "asset_name": asset_name,
                                    "asset_type": asset_type,
                                    "quantity": quantity,
                                    "price_per_unit": price_per_unit,
                                    "total": quantity * price_per_unit})
                    
                    print(f"Successfully sold {quantity} units of {asset_name} at £{price_per_unit:.2f} each.")
                    if asset['quantity'] == 0:
                        account['assets'].remove(asset)
              else:
                    print(f"Insufficient quantity of {asset_name} to sell. You have {asset['quantity']} units.")
              return account
    else:
        print(f"No asset named {asset_name} found in your portfolio.")
    return account

#To match user input to correct asset key
def find_asset_key(market, user_input):
    user_input = user_input.strip().lower()
    for asset in market.keys():
        if user_input.lower() in asset.lower():
            return asset
    return None

stock_market = {
    "Apple (AAPL)": 150.00,
    "Google (GOOGL)": 2800.00,
    "Amazon (AMZN)": 3400.00,
    "Tesla (TSLA)": 700.00,
    "NVIDIA (NVDA)": 220.00,
    "Microsoft (MSFT)": 300.00,
    "Meta (META)": 100.00,
    "Netflix (NFLX)": 500.00,
    "Nike (NKE)": 130.00,
    "Coca-Cola (KO)": 60.00,
    "Johnson & Johnson (JNJ)": 170.00,
    "Walmart (WMT)": 140.00,
    "Procter & Gamble (PG)": 150.00,
    "Visa (V)": 220.00,
    "KPMG (KPMG)": 50.00,
}

forex_market = {
    "EUR/USD": 1.10,
    "GBP/USD": 1.30,
    "USD/JPY": 110.00,
    "AUD/USD": 0.75,
    "USD/CAD": 1.25,
    "NZD/USD": 0.70,
    "USD/CHF": 0.90,
    "EUR/GBP": 0.85,
    "EUR/JPY": 130.00,
    "GBP/JPY": 150.00,
    "USD/SGD": 1.40,
    "CNY/USD": 6.50,
    "USD/INR": 75.00,
    "USD/BRL": 5.00,
    "USD/RUB": 90.00
}

cryptocurrency_market = {
    "Bitcoin (BTC)": 30000.00,
    "Ethereum (ETH)": 2000.00,
    "Ripple (XRP)": 0.50,
    "Litecoin (LTC)": 150.00,
    "Cardano (ADA)": 1.20,
    "Polkadot (DOT)": 25.00,
    "Chainlink (LINK)": 30.00,
    "Stellar (XLM)": 0.30,
    "Dogecoin (DOGE)": 0.10,
    "Solana (SOL)": 40.00,
    "Avalanche (AVAX)": 60.00,
    "Polygon (MATIC)": 1.50,
    "VeChain (VET)": 0.08,
    "Tezos (XTZ)": 3.00,
    "Algorand (ALGO)": 1.20
}

commodities_market = {
    "Gold": 1800.00,
    "Silver": 25.00,
    "Crude Oil": 70.00,
    "Natural Gas": 3.50,
    "Copper": 4.00,
    "Platinum": 1000.00,
    "Palladium": 2500.00,
    "Wheat": 6.00,
    "Corn": 5.50,
    "Soybeans": 13.00,
    "Coffee": 1.50,
    "Sugar": 0.15,
    "Cotton": 0.80,
    "Cocoa": 2.50,
    "Lumber": 400.00
}

print()
print("You're all set to start investing! Explore our investment options and grow your wealth.")
print()
while True:
    print("--------------------------------")
    print("              HOME              ")
    print("--------------------------------")
    print("1. View portfolio")
    print("2. Buy asset")
    print("3. Sell asset")
    print("4. View transaction history")
    print("5. Portfolio summary")
    print("6. Exit")
    choice = input("Please select an option (1-6): ")



    if choice == "1":
        while True:
         print("--------------------------------")
         print("          YOUR PORTFOLIO        ")
         print("--------------------------------")
         print(f"Name: {account['name']}")
         print(f"Balance: £{account['balance']:.2f}")
         print(f"Account Type: {account['account_type']}")
         print(f"Sort Code: {account['sort_code']}")
         print(f"Account Number: {account['account_number']}")
         print()
         print("Assets:")
         if len(account['assets']) == 0:
            print("You don't own any assets yet.")
         else:
            for asset in account['assets']:
                print(f"{asset['asset_name']:<15} ({asset['asset_type']}): {asset['price_per_unit']:.2f} ({asset['quantity']} units)")
         choice0 = input("Would you like to return to the home menu? (yes/no): ").lower()
         if choice0 != "no":
             break
                  

    if choice == "2":
     while True:
        asset_type = input("Enter the asset type (Stock, forex, Cryptocurrency, commodities): ").lower()
        markets = {
            "stock": stock_market,
            "forex": forex_market,
            "cryptocurrency": cryptocurrency_market,
            "commodities": commodities_market,
        }

        if asset_type not in markets:
            print("Invalid asset type.")
            continue

        market = markets[asset_type]
        print("================================")
        print(f"          {asset_type.upper()} MARKET          ")
        print("================================")
        for asset, price in market.items():
            print(f"{asset:<25}: £{price:.2f}")

        asset_name = input("Enter the name of the asset you want to buy: ")
        asset_name = find_asset_key(market, asset_name)
        price_per_unit = market.get(asset_name)
        if price_per_unit is None:
            print("Asset not found in the selected market.")
            continue

        quantity = int(input("Enter the quantity you want to buy: "))
        buy_asset(account, asset_name, asset_type, quantity, price_per_unit)
        choice1 = input("Would you like to buy another asset or return to the home menu? (buy/home): ").lower()
        if choice1 != "buy":
            break

    if choice == "3":
        while True:
            if len(account['assets']) == 0:
                print()
                print("You dont own any assets to sell.")
                break
            print("--------------------------------")
            print("          YOUR ASSETS          ")
            print("--------------------------------")
            for asset in account['assets']:
                print(f"{asset['asset_name']:<15} ({asset['asset_type']}): {asset['price_per_unit']:.2f} ({asset['quantity']} units)")
            asset_name = input("Enter the name of the asset you want to sell: ")
            asset_name = find_asset_key(market, asset_name)
            asset_type = input("Enter the type of the asset you want to sell: ").lower()
            quantity = int(input("Enter the quantity you want to sell: "))
            price_per_unit = None
            for asset in account['assets']:
                if asset['asset_name'] == asset_name and asset['asset_type'] == asset_type:
                    price_per_unit = asset['price_per_unit']
                    break
            sell_asset(account, asset_name, asset_type, quantity, price_per_unit)
            choice2 = input("Would you like to sell another asset or return to the home menu? (sell/home): ").lower()
            if choice2 != "sell":
                break

    if choice == "4":
        while True:
         print("--------------------------------")
         print("      TRANSACTION HISTORY      ")
         print("--------------------------------")
         if len(account['transactions']) == 0:
            print("No transactions found.")
            break
         else:
            for transaction in account['transactions']:
                print(f"{transaction['type'].capitalize()} - {transaction['asset_name']:<15} ({transaction['asset_type']}): {transaction['quantity']} units at £{transaction['price_per_unit']:.2f} each, Total: £{transaction['total']:.2f}")
         choice3 = input("Would you like to return to the home menu? (yes/no): ").lower()
         if choice3 != "no":
             break

    if choice == "5":
        while True:
         print("--------------------------------")
         print("        PORTFOLIO SUMMARY       ")
         print("--------------------------------")
         total_assets_value = sum(asset['quantity'] * asset['price_per_unit'] for asset in account['assets'])
         total_portfolio_value = account['balance'] + total_assets_value
         print(f"Total Assets Value: £{total_assets_value:.2f}")
         print(f"Total Portfolio Value (Balance + Assets): £{total_portfolio_value:.2f}")
         choice4 = input("Would you like to return to the home menu? (yes/no): ").lower()
         if choice4 != "no":
             break

    if choice == "6":
        print("Thank you for using the Investment Simulator!")
        break




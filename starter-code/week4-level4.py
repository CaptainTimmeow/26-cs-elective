"""
Week 4 Starter Code - Level 4: Advanced
Cryptocurrency Portfolio Tracker

BONUS CHALLENGES:
- Add price alerts (notify when coin crosses threshold)
- Show 7-day price history chart (use matplotlib)
- Add coin comparison feature
- Implement portfolio diversification analysis
- Add "watchlist" feature separate from portfolio
"""

import requests
import json

class CryptoPortfolio:
    def __init__(self):
        self.portfolio = {}  # {coin_id: amount}
        self.prices = {}    # {coin_id: price_data}
        self.load()
    
    def load(self):
        """Load portfolio from file"""
        try:
            with open('portfolio.json', 'r') as f:
                self.portfolio = json.load(f)
        except FileNotFoundError:
            self.portfolio = {}
    
    def save(self):
        """Save portfolio to file"""
        with open('portfolio.json', 'w') as f:
            json.dump(self.portfolio, f, indent=2)
    
    def get_top_coins(self):
        """Get top 10 cryptocurrencies by market cap"""
        
        url = "https://api.coingecko.com/api/v3/coins/markets"
        params = {
            'vs_currency': 'usd',
            'order': 'market_cap_desc',
            'per_page': 10,
            'page': 1,
            'sparkline': False
        }
        
        # ============================================
        # YOUR CODE HERE:
        # ============================================
        # Make API request and return list of coins
        
        return []
    
    def search_coin(self, query):
        """Search for a coin by name"""
        
        url = "https://api.coingecko.com/api/v3/search"
        params = {'query': query}
        
        # ============================================
        # YOUR CODE HERE:
        # ============================================
        # Make API request, return list of matches
        
        return []
    
    def add_holding(self, coin_id, amount):
        """Add coins to portfolio"""
        
        # ============================================
        # YOUR CODE HERE:
        # ============================================
        # Add amount to self.portfolio[coin_id]
        # Save to file
        pass
    
    def get_prices(self, coin_ids):
        """Get current prices for coins in portfolio"""
        
        if not coin_ids:
            return {}
        
        # ============================================
        # YOUR CODE HERE:
        # ============================================
        # Get market data for specific coins
        
        return {}
    
    def calculate_value(self):
        """Calculate total portfolio value"""
        
        # ============================================
        # YOUR CODE HERE:
        # ============================================
        # Get prices, calculate total value
        
        return 0.0
    
    def display_top(self):
        """Display top 10 cryptocurrencies"""
        
        coins = self.get_top_coins()
        
        print("\n" + "=" * 70)
        print(f"{'#':<3} {'Coin':<20} {'Price':<15} {'24h %':<10}")
        print("=" * 70)
        
        for i, coin in enumerate(coins, 1):
            name = f"{coin['name']} ({coin['symbol'].upper()})"
            price = f"${coin['current_price']:,.2f}"
            change = f"{coin['price_change_percentage_24h']:.2f}%"
            print(f"{i:<3} {name:<20} {price:<15} {change:<10}")
    
    def display_portfolio(self):
        """Display current portfolio with values"""
        
        if not self.portfolio:
            print("Portfolio is empty!")
            return
        
        # ============================================
        # YOUR CODE HERE:
        # ============================================
        # Get prices for portfolio coins
        # Calculate values
        # Display nicely with profit/loss
        
        pass

def main():
    portfolio = CryptoPortfolio()
    
    while True:
        print("\n" + "=" * 50)
        print("  CRYPTO PORTFOLIO TRACKER")
        print("=" * 50)
        print("1. View Top 10 Cryptocurrencies")
        print("2. Search for a Coin")
        print("3. Add to Portfolio")
        print("4. View Portfolio")
        print("5. Exit")
        print("=" * 50)
        
        choice = input("\nEnter your choice: ")
        
        if choice == '1':
            portfolio.display_top()
        elif choice == '2':
            query = input("Enter coin name to search: ")
            results = portfolio.search_coin(query)
            # Display search results
        elif choice == '3':
            coin_id = input("Enter coin ID (e.g., bitcoin): ")
            amount = float(input("Enter amount: "))
            portfolio.add_holding(coin_id, amount)
            print(f"Added {amount} {coin_id} to portfolio!")
        elif choice == '4':
            portfolio.display_portfolio()
        elif choice == '5':
            portfolio.save()
            print("Portfolio saved. Goodbye!")
            break

if __name__ == "__main__":
    main()

import ccxt
import time
from decimal import Decimal

class Trader:
    def __init__(self, config):
        self.config = config
        self.exchange = ccxt.binance({
            'apiKey': config['api_key'],
            'secret': config['api_secret'],
            'enableRateLimit': True
        })
    
    def get_balance(self, asset='USDT'):
        """
        Balance inquiry
        """
        try:
            balance = self.exchange.fetch_balance()
            return float(balance['free'][asset])
        except Exception as e:
            print(f"Balance inquiry error: {e}")
            return 0

    def create_market_buy_order(self, symbol, quantity):
        """
        Market price buy order
        """
        try:
            order = self.exchange.create_market_buy_order(
                symbol,
                quantity
            )
            print(f"Buy order executed: {order}")
            return order
        except Exception as e:
            print(f"Buy order error: {e}")
            return None

    def create_market_sell_order(self, symbol, quantity):
        """
        Market price sell order
        """
        try:
            order = self.exchange.create_market_sell_order(
                symbol,
                quantity
            )
            print(f"Sell order executed: {order}")
            return order
        except Exception as e:
            print(f"Sell order error: {e}")
            return None

    def set_stop_loss(self, symbol, quantity, entry_price):
        """
        Stop-loss order
        """
        try:
            stop_price = entry_price * (1 - self.config['stop_loss_percentage'] / 100)
            order = self.exchange.create_order(
                symbol,
                'stop_loss',
                'sell',
                quantity,
                None,
                {
                    'stopPrice': stop_price,
                    'type': 'STOP_LOSS'
                }
            )
            print(f"Stop-loss order placed: {order}")
            return order
        except Exception as e:
            print(f"Stop-loss order error: {e}")
            return None

    def set_take_profit(self, symbol, quantity, entry_price):
        """
        Take-profit order
        """
        try:
            take_profit_price = entry_price * (1 + self.config['take_profit_percentage'] / 100)
            order = self.exchange.create_order(
                symbol,
                'take_profit',
                'sell',
                quantity,
                None,
                {
                    'stopPrice': take_profit_price,
                    'type': 'TAKE_PROFIT'
                }
            )
            print(f"Take-profit order placed: {order}")
            return order
        except Exception as e:
            print(f"Take-profit order error: {e}")
            return None 
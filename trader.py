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
        Bakiye sorgulama
        """
        try:
            balance = self.exchange.fetch_balance()
            return float(balance['free'][asset])
        except Exception as e:
            print(f"Bakiye sorgulama hatasi: {e}")
            return 0

    def create_market_buy_order(self, symbol, quantity):
        """
        Market fiyatindan alim emri
        """
        try:
            order = self.exchange.create_market_buy_order(
                symbol,
                quantity
            )
            print(f"Alim emri gerçekleşti: {order}")
            return order
        except Exception as e:
            print(f"Alim emri hatasi: {e}")
            return None

    def create_market_sell_order(self, symbol, quantity):
        """
        Market fiyatindan satiş emri
        """
        try:
            order = self.exchange.create_market_sell_order(
                symbol,
                quantity
            )
            print(f"Satiş emri gerçekleşti: {order}")
            return order
        except Exception as e:
            print(f"Satiş emri hatasi: {e}")
            return None

    def set_stop_loss(self, symbol, quantity, entry_price):
        """
        Stop-loss emri
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
            print(f"Stop-loss emri yerleştirildi: {order}")
            return order
        except Exception as e:
            print(f"Stop-loss emri hatasi: {e}")
            return None

    def set_take_profit(self, symbol, quantity, entry_price):
        """
        Take-profit emri
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
            print(f"Take-profit emri yerleştirildi: {order}")
            return order
        except Exception as e:
            print(f"Take-profit emri hatasi: {e}")
            return None 
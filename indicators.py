import pandas as pd
import numpy as np

class Indicators:
    @staticmethod
    def calculate_ma(data, period):
        """
        Calculate moving average
        """
        return data['close'].rolling(window=period).mean()
    
    @staticmethod
    def calculate_rsi(data, period):
        """
        Calculate RSI
        """
        delta = data['close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
        
        rs = gain / loss
        rsi = 100 - (100 / (1 + rs))
        return rsi 
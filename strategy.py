import pandas as pd

class TradingStrategy:
    def __init__(self, config):
        self.config = config
    
    def generate_signals(self, df):
        """
        Alım-satım sinyalleri üretir
        """
        signals = pd.DataFrame(index=df.index)
        signals['position'] = 0
        
       
        price_above_ma = df['close'] > df['ma']
        rsi_oversold = df['rsi'] < self.config['rsi_oversold']
        rsi_overbought = df['rsi'] > self.config['rsi_overbought']
        
        
        signals.loc[price_above_ma & rsi_oversold, 'position'] = 1
        
       
        signals.loc[rsi_overbought, 'position'] = -1
        
        return signals 
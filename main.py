from config import CONFIG
from data_fetcher import DataFetcher
from indicators import Indicators
from strategy import TradingStrategy
from trader import Trader
import time

def main():
   
    fetcher = DataFetcher()
    indicators = Indicators()
    strategy = TradingStrategy(CONFIG)
    trader = Trader(CONFIG)
    

    in_position = False
    
    while True:
        try:
          
            df = fetcher.fetch_ohlcv(
                CONFIG['symbol'], 
                CONFIG['interval']
            )
            
            if df is not None:
              
                df['ma'] = indicators.calculate_ma(df, CONFIG['ma_period'])
                df['rsi'] = indicators.calculate_rsi(df, CONFIG['rsi_period'])
                
            
                signals = strategy.generate_signals(df)
                
           
                last_signal = signals['position'].iloc[-1]
                current_price = df['close'].iloc[-1]
                
                if last_signal == 1 and not in_position:
                    print(f"ALIM SİNYALİ - {CONFIG['symbol']} - Fiyat: {current_price}")
                    
                
                    order = trader.create_market_buy_order(
                        CONFIG['symbol'],
                        CONFIG['quantity']
                    )
                    
                    if order:
                        in_position = True 
                       
                        trader.set_stop_loss(
                            CONFIG['symbol'],
                            CONFIG['quantity'],
                            current_price
                        )
                        trader.set_take_profit(
                            CONFIG['symbol'],
                            CONFIG['quantity'],
                            current_price
                        )
                
                elif last_signal == -1 and in_position:
                    print(f"SATIŞ SİNYALİ - {CONFIG['symbol']} - Fiyat: {current_price}")
                    
                    # Satış emri ver
                    order = trader.create_market_sell_order(
                        CONFIG['symbol'],
                        CONFIG['quantity']
                    )
                    
                    if order:
                        in_position = False
                
            
            time.sleep(60)  
            
        except Exception as e:
            print(f"Hata oluştu: {e}")
            time.sleep(60)

if __name__ == "__main__":
    main()

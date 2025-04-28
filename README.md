# Hareketli Ortalama ve RSI Tabanlı Trading Botu / Moving Average and RSI Based Trading Bot

## Açıklama / Description
Bu proje, Binance borsasında otomatik alım-satım işlemleri gerçekleştirmek için Python ile geliştirilmiş bir trading botudur. Bot, hareketli ortalama (MA) ve Göreceli Güç Endeksi (RSI) göstergelerine dayanarak alım ve satım sinyalleri üretir ve ccxt kütüphanesi aracılığıyla emirleri yönetir.

This project is an automated trading bot written in Python for executing buy and sell orders on the Binance exchange. The bot uses Moving Average (MA) and Relative Strength Index (RSI) indicators to generate trading signals and manages orders via the ccxt library.

## Özellikler / Features
- Basit ve etkili hareketli ortalama (MA) göstergesi
- Göreceli Güç Endeksi (RSI) göstergesi
- Stop-loss ve Take-profit emirleri
- Gerçek zamanlı OHLCV verisi çekme ve emir yönetimi
- Esnek ve yapılandırılabilir parametreler

- Simple and effective Moving Average (MA) indicator
- Relative Strength Index (RSI) indicator
- Stop-loss and Take-profit orders
- Real-time OHLCV data fetching and order management
- Flexible and configurable parameters

## Gereksinimler / Requirements
- Python 3.7 veya üstü / Python 3.7+
- pandas >=1.0.0
- numpy >=1.18.0
- ccxt >=2.7.0

## Kurulum / Installation
1. Depoyu klonlayın:
   ```bash
   git clone <repo_url>
   cd ma_rsi_trading_bot
   ```
2. Sanal ortam oluşturun ve etkinleştirin:
   ```bash
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # macOS/Linux:
   source venv/bin/activate
   ```
3. Gerekli paketleri yükleyin:
   ```bash
   pip install -r requirements.txt
   ```

## Yapılandırma / Configuration
`config.py` dosyasını açarak aşağıdaki ayarları ihtiyacınıza göre düzenleyin:

| Parametre                | Açıklama (TR)                               | Description (EN)                               |
|--------------------------|---------------------------------------------|-----------------------------------------------|
| `symbol`                 | İşlem çifti (ör. BTCUSDT)                   | Trading pair (e.g. BTCUSDT)                   |
| `interval`               | Zaman dilimi (ör. 1h, 5m, vs.)             | Timeframe (e.g. 1h, 5m, etc.)                 |
| `ma_period`              | Hareketli Ortalama periyodu                 | MA period                                     |
| `rsi_period`             | RSI periyodu                                 | RSI period                                    |
| `rsi_oversold`           | Aşırı satım eşiği                           | RSI oversold threshold                        |
| `rsi_overbought`         | Aşırı alım eşiği                            | RSI overbought threshold                      |
| `quantity`               | İşlem miktarı (örn. 0.001)                  | Order quantity (e.g. 0.001)                   |
| `api_key`, `api_secret`  | Binance API anahtarlarınız                  | Your Binance API credentials                  |
| `stop_loss_percentage`   | Stop-loss yüzdesi (örn. 2.0)                | Stop-loss percentage (e.g. 2.0)               |
| `take_profit_percentage` | Take-profit yüzdesi (örn. 3.0)              | Take-profit percentage (e.g. 3.0)             |

## Kullanım / Usage
Botu çalıştırmak için terminalde aşağıdaki komutu kullanın:
```bash
python main.py
```
Bot, her döngüde son OHLCV verilerini çeker, MA ve RSI hesaplamalarını yapar, sinyaller üretir ve pozisyon açıp kapatır.

Run the bot with:
```bash
python main.py
```
The bot fetches the latest OHLCV data, calculates MA and RSI indicators, generates signals, and opens/closes positions accordingly.

## Önemli Uyarı / Disclaimer
Bu bot demo amaçlıdır ve gerçek para ile kullanmadan önce testnet veya küçük miktarlarla test edilmelidir. Kripto para piyasaları yüksek oynaklık içerir ve zarar riski vardır.

This bot is for demo purposes. Test on a testnet or with small amounts before using real funds. Cryptocurrency markets are highly volatile and carry risk of loss.

## Katkıda Bulunma / Contributing
Katkı önerileri, raporlanan hatalar veya geliştirme talepleri için lütfen bir issue açın veya pull request gönderin.

Feedback, bug reports, or feature requests? Please open an issue or submit a pull request.

## Lisans / License
MIT Lisansı altında lisanslanmıştır.

Licensed under the MIT License.


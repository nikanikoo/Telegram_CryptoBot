# Telegram CryptoBot (telebot)
Telegram bot preset with basic crypto bot based on the Telebot library: wallet, admin capabilities, getting notification about wallet refill, etc.


## 🖥 Installing

```sh
git clone https://github.com/nik0ri/Telegram_CryptoBot.git
cd Telegram_CryptoBot
pip install pyTelegramBotAPI
python main.py
```

Then change the value of the TOKEN variable in main.py to the token of your bot. (line 5)

## 📃 All commands bot

```
*User commands*
/start - Main menu
/wallet - Account balance

*Admin commands*
/add_amount [id] [currency] [amount] - Refill the user's balance.
/add_admin [id] - Issuance of admin rights
/rem_admin [id] - Revocation of admin rights
```

## 🪙 All currency (for /add_amount)

```
USDT - Tether
TON - Toncoin
GRAM - Gram
BTC - Bitcoin
LTC - Litecoin
ETH - Ethereum
BNB - Binance coin
TRX - TRON
USDC - USD Coin
```

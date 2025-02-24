import requests
from telegram import Bot
from telegram.ext import Application, CommandHandler

# Token de Telegram
TELEGRAM_TOKEN = ''
CHAT_ID = ''  

# Lista de criptomonedas a seguir
cryptos = ["bitcoin", "ethereum", "solana", "ripple"]

# Función para obtener los precios de las criptomonedas desde CoinGecko
def get_crypto_price(crypto):
    url = f'https://api.coingecko.com/api/v3/simple/price?ids={crypto}&vs_currencies=usd'
    response = requests.get(url)
    data = response.json()
    return data.get(crypto, {}).get('usd', 'No disponible')

# Función para manejar el comando /start
async def start(update, context):
    await update.message.reply_text("¡Hola! Soy tu bot de seguimiento de criptomonedas. Usa /precio para obtener el precio.")

# Función para manejar el comando /precio
async def precio(update, context):
    message = "Precios de criptomonedas:\n"
    for crypto in cryptos:
        price = get_crypto_price(crypto)
        message += f"• {crypto.capitalize()}: ${price} USD\n"
    await update.message.reply_text(message)

# Ejecutar el bot de Telegram
if __name__ == "__main__":
    application = Application.builder().token(TELEGRAM_TOKEN).build()
    
    # Agregar los handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("precio", precio))

    # Iniciar el bot
    application.run_polling()

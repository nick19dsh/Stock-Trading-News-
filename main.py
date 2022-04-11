import requests
import os
from dotenv import load_dotenv

STOCK_NAME = "BSE:HDFCBANK"
COMPANY_NAME = "HDFC BANK Limited"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

load_dotenv()

API_KEY = os.getenv("API_KEY")
NEWS_API_KEY = os.getenv("NEWS_APIKEY")

BOT_KEY = os.getenv("BOT_KEY")
BOT_ENDPOINT = f"https://api.telegram.org/bot{BOT_KEY}/sendMessage"
CHAT_ID = os.getenv("CHAT_ID")


# 1.Yesterday's closing stock price

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

# 2.The day before yesterday's closing stock price

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)

# 3.Difference between 1 and 2

difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"


# 4. Percentage difference in price between closing price yesterday and closing price the day before yesterday

diff_percent = round((difference / float(yesterday_closing_price)) * 100, 2)
print(diff_percent)

# 5. If percentage is greater than 0 then get articles related to the COMPANY_NAME

if abs(diff_percent) > 0:

    news_params = {"apiKey": NEWS_API_KEY, "qInTitle": COMPANY_NAME, "pageSize": 3}

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]

    # 6. A new list of the first 3 article's headline and description using list comprehension

    formatted_articles = [
        f"{STOCK_NAME}: {up_down}{abs(diff_percent)}%\nHeadline: {article['title']}. \nBrief: {article['description']}"
        for article in articles
    ]

    for article in formatted_articles:
        message = article

        # 7. Send these article briefs through Telegram

        parameters_bot = {"chat_id": CHAT_ID, "text": message}

        response = requests.post(BOT_ENDPOINT, params=parameters_bot)
        response.raise_for_status()

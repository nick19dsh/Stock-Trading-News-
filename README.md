# Overview
Stock Trading News Alert is a message alert system from data using different APIs and Telegram bot. This alert system gives the absolute
percentage of difference of particular stock closing price between two days and it also sends 3 news about the stock through Telegram messaging application.

# Features
1. Gives closing price of yesterday and the day before yesteday of a particular stock using stock API
2. Gives the difference of stock price between two days
3. Sends message of absolute difference of stock price if the difference is more than 0 percentage using news API
4. Sends 3 latest news about the stock using Telegram bot

# Python libraries
-   os
-   requests
-   dotenv

# API
1. Stock API (https://www.alphavantage.co/)
2. News API (https://newsapi.org/)
3. Telegram Bot

# stock-prices-tracker
Simple NASDAQ stock companies tracker. Created using Finnhub.io API, python and SQLite.


# How to use?
1) Create your own account on https://finnhub.io/
2) Get your API Key
3) Create SECRETS.py in /app 
4) FINNHUB_TOKEN = 'YOUR_OWN_API_KEY'
5) Setup your database by running sqlite_database_setup.py
6) Insert stock tickers that interests you following this scheme

![Bez tytułu](https://user-images.githubusercontent.com/16820475/113864224-ed83bb80-97aa-11eb-8ad2-9ba835d02576.png)


7) Run everyday (use scripts!) using python -m app.stock_tracker_app and track prices!

# Future?
I am planning new version with Flask/FastAPI, probably using https://www.pythonanywhere.com/ free hosting. Stay tune for updates. 

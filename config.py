# looking for at least 100k members
REDDIT_CONFIG = dict(crypto_subreddits=['CryptoCurrency', 'CryptocurrencyICO', 'CryptoMarkets', 'investing'],
                     bitcoin_subreddits=['Bitcoin', 'BitcoinMarkets'],
                     ethereum_subreddits=['ethtrader', 'ethereum'],
                     investing_subreddits=['investing', 'wallstreetbets', 'stocks'],
                     test_subreddits=['investing'])

FILES = dict(sentiment_dict='files/sentiwords.txt')

MONGO_URL = 'mongodb://admin:password3@ds235197.mlab.com:35197/heroku_gk05lzsb'
DB_NAME = 'heroku_gk05lzsb'

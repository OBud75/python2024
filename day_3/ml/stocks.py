from matplotlib import pyplot
import seaborn
import yfinance
import nltk

nltk.download('punkt_tab')


def plot_amazon():
    amazon_data = yfinance.download(
        tickers="AMZN", start="2020-06-1", end="2024-06-1"
    )
    amazon_data.reset_index(inplace=True)

    pyplot.figure(figsize=(14, 5))
    seaborn.set_style(style="ticks")
    seaborn.lineplot(data=amazon_data, x="Date", y="Price", color="firebrick")
    seaborn.despine()

    pyplot.title(label="Amazon stock prices", size="x-large", color="blue")
    pyplot.show()

from classes.scrapper import Scrapper

scrapper = Scrapper()


news_df = scrapper.get_all_news()
news_df.to_csv("news.csv", index=False)
import newspaper
from bs4 import BeautifulSoup as bs
import requests

def get_data_from_article(url):
    article = newspaper.Article(url)
    article.download()
    article.parse()
    if article.text != '':
        return {'content': article.text, 'authors': article.authors, 'title': article.title, 'date': article.publish_date}
    else:
        print('newspaper failed. Trying with beautiful soup')
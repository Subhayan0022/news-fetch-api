from fastapi import FastAPI,HTTPException
import requests
from cachetools import TTLCache, cached
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)                     # creating a logger instance

top_news_id_url = "https://hacker-news.firebaseio.com/v0/topstories.json"   #fetching the ids of topstories.
top_news_url = "https://hacker-news.firebaseio.com/v0/item/{}.json"         #fetching the details of topstories from ids

cache = TTLCache(maxsize=10, ttl=600)                    # cache for 10 times for 10 minutes

app = FastAPI()

@cached(cache)                                           # decorator for caching.
def get_top_news_ids():                                  # function that returns ids for the top-news.
    try:
        logger.info("Top news ids fetched successfully.")
        response = requests.get(top_news_id_url)
        return response.json()
        
    except Exception:
        logger.error("Cannot establish connection with API.")
        raise HTTPException(status_code=503, detail="Something went wrong, API not avaiable.")


def get_top_news(id):                                    # function that returns the top-news taking id of article as param.
    try:
        logger.info("Top news fetched successfully.")
        response = requests.get(top_news_url.format(id))
        return response.json()
        
    except Exception:
        logger.error("Cannot establish connection with API.")
        raise HTTPException(status_code=503, detail="Something went wrong, API not avaiable.")


@app.get("/top-news")                                    # endpoint of the top-news articles.
def get_articles(count: int = 10):                       # count: int = 10 is a type hint.
    news_ids = get_top_news_ids()
    news_ids = news_ids[:count]                          # slicing the ids to display only top 10.
    
    top_news = []

    if len(news_ids) == 0:
        logger.error("Empty list.")
        raise HTTPException(status_code=404, detail="No articles found.")
        
    else:
        logger.info("Top news articles fetched successfully.")
        for id in news_ids:                              #traversing through the news_ids adding the details to empty list.
            news = get_top_news(id)
            top_news.append(news)

        return top_news
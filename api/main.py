import requests

#x = requests.get('https://newsapi.org/v2/everything?q=tesla&from=2024-03-11&sortBy=publishedAt&apiKey=71c704f080b24c9b82fafb7662e41813')
#print(x)
#content = x.json()
#articles = (content['articles'])

#for article in articles:
    #print('Title\n',article['title'], '\nDescription\n', article['description'])


def get_news(title_news,from_date,api_key='71c704f080b24c9b82fafb7662e41813' ):
    url = 'https://newsapi.org/v2/everything?q={title_news}&from={from_date}&sortBy=publishedAt&apiKey={api_key}'
    x = requests.get(url)
    content = x.json()
    articles = content['article']
    result = []
    for article in articles:
        result.append(f"Titles\n'{article['title']}, '\nDescription\n'{article['description']}")
        return result
    
news = get_news('apple', 2024/4/10)
print(news)
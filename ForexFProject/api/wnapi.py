import worldnewsapi

# Initial SDK configuration
newsapi_configuration = worldnewsapi.Configuration(api_key={'apiKey': '31a8634c11be47b78dfb7298121a6935'})

try:
    newsapi_instance = worldnewsapi.NewsApi(worldnewsapi.ApiClient(newsapi_configuration))

    max_results = 250   # replace with your maximum
    offset = 0
    all_results = []

    while len(all_results) < max_results:
        request_count = min(100, max_results - len(all_results)) # request 100 or the remaining number of articles

        response = newsapi_instance.search_news(
            text='football',
            language='en',
            earliest_publish_date='2024-07-01',
            latest_publish_date='2024-07-17',
            categories='sports',
            sort="publish-time",
            sort_direction="desc",
            min_sentiment=-0.8,
            max_sentiment=0.8,
            offset=offset,
            number=request_count)

        print("Retrieved " + str(len(response.news)) + " articles. Offset: " + str(offset) + "/" + str(max_results) +
              ". Total available: " + str(response.available) + ".")

        if len(response.news) == 0:
            break

        all_results.extend(response.news)
        offset += 100

except worldnewsapi.ApiException as e:
    print("Exception when calling NewsApi->search_news: %s\n" % e)

for article in all_results:
    print("\nTitle: " + str(article.title))
    print("Author: " + str(article.author))
    print("URL: " + str(article.url))
    print("Sentiment: " + str(article.sentiment))
    print("Text: " + str(article.text[:80]) + "...") # print first 80 characters of the text
import yweather

def get_woeid(country):
    client = yweather.Client()
    return client.fetch_woeid(country)
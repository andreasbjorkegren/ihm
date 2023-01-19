import requests

api_url = "https://dummyjson.com/products/10"

response = requests.get(api_url)
print(response.json())


# Vad är priset för produkt med id 10?

# Svaret är: 
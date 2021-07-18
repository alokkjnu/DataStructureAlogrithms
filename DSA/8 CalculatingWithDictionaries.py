#Calculating with Dictionaries

price = {
    'ACME' : 45.23,
    'AAPL' : 612.78,
    'IBM' : 205.55,
    'HPQ' : 37.20,
    'FB' : 10.75
}
min_price = min(zip(price.values(),price.keys()))
print(min_price)
max_price = max(zip(price.values(),price.keys()))
print(max_price)

price_sorted = sorted(zip(price.values(),price.keys()))
print(price_sorted)

price_and_names = zip(price.values(),price.keys())
print(min(price_and_names))
print(max(price_and_names))
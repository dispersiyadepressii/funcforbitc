import requests

def PriceOfBitc():
    response = requests.get("https://coinlib.io/api/v1/coin?key=3d149733fe68ae0c&pref=EUR&symbol=BTC")
    print("connection code:", response.status_code)
    a = response.json()
    print("price:", a["price"])
    return a["price"]
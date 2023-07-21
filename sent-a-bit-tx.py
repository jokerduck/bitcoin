from requests_html import HTMLSession

session = HTMLSession()

url = 'https://api.coingecko.com/api/v3/coins/bitcoin'

response = session.get(url)

if response.status_code == 200:
    with open("parse_result.txt", "w", encoding="utf-8") as f:
        f.write(response.text)
    print("Data saved successfully to 'parse_result.txt'")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")

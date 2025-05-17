import requests

def fetch_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        raise Exception(f"Failed to retrieve data from {url}, status code: {response.status_code}")

# Example usage
data = fetch_data('https://api.example.com/data')
if isinstance(data, dict):
    print(data)
else:
    print("No data fetched successfully.")

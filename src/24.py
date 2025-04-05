import os
import requests

def download_file(url):
    response = requests.get(url)
    if response.status_code == 200:
        with open(os.path.basename(url), 'wb') as file:
            file.write(response.content)
        print(f"File downloaded: {url}")
    else:
        print(f"Failed to download file. Status code: {response.status_code}")

def main():
    url = "https://github.com/schoolproject/PythonProject.git"
    download_file(url)

if __name__ == "__main__":
    main()

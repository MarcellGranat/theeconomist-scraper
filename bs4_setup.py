import requests
from bs4 import BeautifulSoup
from datetime import date
import requests
import pickle

with open("cookies.pkl", "rb") as file:
    cookies = pickle.load(file)

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36", 
    "Accept-Encoding":"gzip, deflate", 
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", 
    "DNT":"1",
    "Connection":"close", 
    "Upgrade-Insecure-Requests":"1"
}

def req(url):
    return requests.get(url, headers=headers, cookies=cookies, timeout=10)

def read_html(url):
    return BeautifulSoup(requests.get(url, headers=headers, cookies=cookies, timeout=10).content, 'html.parser')

if __name__ == "__main__":
    page = read_html("https://www.economist.com/leaders/2024/06/20/war-and-ai")
    print(page)
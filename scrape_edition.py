from bs4_setup import read_html, req
import re
from scrape_article import download_article
from datetime import datetime, timedelta
import os
from tqdm import tqdm
from json import dump

def last_edition():    
    today = datetime.now()
    edition = datetime(2024, 5, 25)
    while edition < today:
        edition += timedelta(days=7)
    edition -= timedelta(days=7)
    return edition

def download_edition(edition = None):
    if edition is None:
        edition = last_edition()
        
    folder = edition.strftime("%Y-%m-%d")
    # create folder
    os.makedirs(folder, exist_ok=True)
    page = read_html("https://www.economist.com/weeklyedition/" + folder)
    
    cover_source = page.find("div").find("section").find("figure").find("img").get("src")
    cover = req(cover_source).content
    
    with open(folder + "/cover.jpg", "wb") as f:
        f.write(cover)
        
    divs = page.find_all("a")
    links = [_.get("href") for _ in divs]
    # only link containing date
    links = [link for link in links if link and re.match(r".*202", link)]
    links = [link for link in links if not link.startswith("/interactive")]

    start = [i for i, link in enumerate(links) if link.startswith("/the-world-this-week")][0]
    links = links[start:]
    # only unique but same order
    links = list(dict.fromkeys(links))

    titles = []
    for link in links:
        for div in divs:
            if div.get("href") == link:
                title = div.get_text()
                if title == '':
                    print(link)
                    titles.append(re.sub(r".*/", "", link))
                else:
                    titles.append(title)
                break
        
    articles = []    
    for link, title in tqdm(zip(links, titles)):
        body = ""
        try:
            body = download_article("https://www.economist.com" + link)
        except Exception as e:
            print(e)
        
        articles.append((link, title, body))
        
    dump(articles, open(folder + "/articles.json", "w"))
        

if __name__ == "__main__":
    download_edition()


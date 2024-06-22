from scrape_edition import last_edition
from json import load
import re

def print_edition(edition = None):
    if edition is None:
        edition = last_edition()
    
    folder = edition.strftime("%Y-%m-%d")
    with open(folder + "/articles.json", "r") as f:
        articles = load(f)
    
    # copy cover.jpg
    with open(folder + "/cover.jpg", "rb") as f:
        cover = f.read()
        
    with open("cover.jpg", "wb") as f:
        f.write(cover)
    
    txt = ""
    prev_topic = ""
    for article in articles:
        link = article[0]
        title = article[1]
        body = article[2]
        
        topic = re.sub(r"/", "", link, count = 1)
        topic = re.sub(r"/.*", "", topic)
        topic = re.sub(r"-", " ", topic)
        topic = topic.upper()
        
        if len(body) > 0:
            if topic != prev_topic:
                txt += "\n\n# " + topic
            prev_topic = topic
            
            txt += "\n\n## " + title
            
            for b in body:
                if b[0] == "text":
                    txt += "\n\n" + b[1]
                if b[0] == "img":
                    txt += "\n\n![](" + b[1] + ")"
                    
    return txt
        
if __name__ == "__main__":
    print(print_edition())
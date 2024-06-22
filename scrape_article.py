from bs4_setup import read_html

def extract_content(div):
    img_div = div.find("img")
    
    if img_div:
        return "img", img_div["src"]
    else:
        return "text", div.get_text()

def download_article(url):
    page = read_html(url)
    new_article_template = page.find(id = "new-article-template")
    site_divs = new_article_template.find_all("div")[0].find_all("div")
    article_divs = [_ for _ in site_divs if _.get_text().startswith("Listen to this story. Enjoy more audio and podcasts")][0]
    
    content = [extract_content(_) for _ in article_divs]
    content = [_ for _ in content if not _[1].startswith("Listen to this story.")]
    content = [_ for _ in content if not _[1].startswith(".css-")]
    return content
    
if __name__ == "__main__":
    download_article("https://www.economist.com/leaders/2024/06/20/emmanuel-macrons-project-of-reform-is-at-risk")

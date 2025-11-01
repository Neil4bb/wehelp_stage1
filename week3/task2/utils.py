import urllib.request
from bs4 import BeautifulSoup

#url = "https://www.ptt.cc/bbs/Steam/M.1761656883.A.C3F.html"
def fetch_html(url):
    req = urllib.request.Request(url, headers= {"User-Agent":"Mozilla/5.0"})
    with urllib.request.urlopen(req) as response:
        return response.read().decode("utf-8")

    
def get_article_time(url):
    html = fetch_html(url)
    soup = BeautifulSoup(html ,"html.parser")

    for tag in soup.select(".article-metaline"):
        key = tag.select_one(".article-meta-tag")
        value = tag.select_one(".article-meta-value")

        if key.text == "時間":
            return value.text.strip()
    
    return ""

#aaa ="https://www.ptt.cc/bbs/Steam/index.html"
#theindex = fetch_html(aaa)
#soup = BeautifulSoup(theindex ,"html.parser")
#print(soup)
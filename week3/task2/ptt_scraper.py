#import urllib.request
from bs4 import BeautifulSoup
from utils import fetch_html, get_article_time
import csv

###scrape網頁

start_url = "https://www.ptt.cc/bbs/Steam/index.html"
#request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
# 用.Request來假冒使用者身分進入 填入瀏覽器及版本供識別
#with urllib.request.urlopen(request) as response:
#    html = response.read().decode("utf-8")

###parse

base_url = "https://www.ptt.cc"

def parse_list_page(url):
    html = fetch_html(url)
    soup = BeautifulSoup(html, "html.parser")
    articles = []

    for entry in soup.select(".r-ent"):
        title_tag = entry.select_one(".title a")
        push_tag = entry.select_one(".nrec span")

        if not title_tag:
            continue

        title = title_tag.text.strip()
        push = push_tag.text.strip() if push_tag else 0
        link = base_url + title_tag["href"]

        full_time = get_article_time(link)

        articles.append({
            "ArticleTitle": title,
            "LikeCount": push,
            "PublishTime": full_time
            
        })
    return articles


def turn_page_f(url):
    html = fetch_html(url)
    soup = BeautifulSoup(html, "html.parser")

    for a in soup.select("a.btn.wide"):
        if "上頁" in a.text:
            prev_page = base_url+a["href"]
            return prev_page
    
    return None


prev_page1 = turn_page_f(start_url)
prev_page2 = turn_page_f(prev_page1)

articlesinthree = parse_list_page(start_url) + parse_list_page(prev_page1) + parse_list_page(prev_page2)

#for art in articlesinthree:
#    print(art)

with open("articles.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(
        f,
        fieldnames=["ArticleTitle", "LikeCount", "PublishTime"],
        extrasaction="ignore",  # 忽略 dict 中多餘的鍵，避免報錯
        restval=""
    )
    writer.writeheader()
    writer.writerows(articlesinthree)

#soup = BeautifulSoup(html, "html.parser")
#print(soup)
#titles =[a.text.strip() for a in soup.select(".title a")]
#push = [b.text.strip() for b in soup.select("span .h1 f2")]
#print(titles)

#with open("articles.csv", "w", encoding="utf-8", newline="") as f:
#    writer = csv.writer(f)
#    writer.writerow(["title"])
#    for t in titles:
#        writer.writerow([t])
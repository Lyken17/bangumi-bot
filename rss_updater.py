import sqlite3


import requests
from bs4 import BeautifulSoup



def err():
    raise Exception('rss filter is not set properly')

class rss_feeder():
    links = " "
    def __init__(self, links="", filter=err):
        self.links = links
        self.filter = filter

def trans2urlencode(s,sep="http"):
    temp = str(s)
    sep += "://"
    temp = temp.split(sep)
    from urllib.parse import quote
    return sep + quote(temp[-1])

def bangumi_filter(links):
    web_content = requests.get(links, stream=True)
    web_as_string = web_content.content
    soup = BeautifulSoup(web_as_string, "xml")
    # print(soup.prettify())
    for item in soup.item.next_siblings:
        # print(item.prettify())

        # print(item.title.string)
        title = item.title.string

        # print(item.pubDate.string)
        pubData = item.pubDate.string

        # print(item.link.string)
        link = item.link.string

        torrent_url = item.enclosure["url"]
        torrent_url = trans2urlencode(torrent_url, sep="https")
        # print(torrent_url)

        yield [title, pubData, link, torrent_url]
        # break
    pass


if __name__ == "__main__":
    url = "https://bangumi.moe/rss/latest"
    import config as cfg

    conn = sqlite3.connect(cfg.sqlite_file)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS BANGUMI
                   (ID TEXT PRIMARY KEY,
                    title           TEXT,
                    pubDate         TEXT,
                    link            TEXT,
                    torrent_url     TEXT);''')

    for record in bangumi_filter(url):
        import hashlib
        from urllib.parse import quote

        s = record[0] + record[1]
        ID = str(hashlib.sha224(s.encode('utf-8')).hexdigest())
        title = record[0]
        # pubData = quote(record[1])
        post_date = str(record[1])

        link = record[2]
        torrent_url = record[3]

        # print(record)
        # print(ID)
        # print(title)
        # print(post_date)
        # print(link)
        # print(torrent_url)

        c.execute("INSERT OR IGNORE INTO BANGUMI (ID,title,pubDate,link,torrent_url) VALUES (?, ?, ?, ?, ?)",(ID, title, post_date, link, torrent_url))
        conn.commit()
    conn.close()


import urllib.request
import re

urls = [
    "https://jasweb.or.jp/video/video_05.html",
    "https://jasweb.or.jp/video/video_02.html",
    "https://jasweb.or.jp/video/video_06A.html",
    "https://jasweb.or.jp/video/video_06B.html",
    "https://jasweb.or.jp/video/video_10.html",
    "https://jasweb.or.jp/video/video_04.html",
    "https://jasweb.or.jp/video/video_07.html",
    "https://jasweb.or.jp/video/video_01A.html"
]

for url in urls:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8')
            # Look for poster="..." inside video tag or img tags
            posters = re.findall(r'poster=["\'](.*?\.(?:jpg|png))["\']', html)
            imgs = re.findall(r'<img.*?src=["\'](.*?\.(?:jpg|png))["\']', html)
            print(f"{url}: POSTER: {posters}, IMGS: {imgs}")
    except Exception as e:
        print(f"Error {url}: {e}")

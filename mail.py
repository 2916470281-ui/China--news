import requests
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone

def update_news():
    tz = timezone(timedelta(hours=8))
    yesterday = datetime.now(tz) - timedelta(days=1)
    display_date = yesterday.strftime("%Y年%m月%d日")
    
    url = 'http://www.people.com.cn/rss/politics.xml'
    try:
        r = requests.get(url, timeout=10)
        root = ET.fromstring(r.content)
        items = ""
        for item in list(root.iter('item'))[:8]:
            items += f'<div style="margin-bottom:15px;padding:15px;background:#fff;border-radius:8px;">' \
                     f'<a href="{item.find("link").text}" style="text-decoration:none;color:#333;font-weight:bold;">' \
                     f'{item.find("title").text}</a></div>'
        
        html = f"<html><body style='background:#f4f4f4;font-family:sans-serif;padding:20px;'>" \
               f"<h2 style='color:#c8102e;'>中国重大事件汇总 ({display_date})</h2>{items}</body></html>"
        
        with open("index.html", "w", encoding="utf-8") as f:
            f.write(html)
    except Exception as e:
        print(e)

update_news()

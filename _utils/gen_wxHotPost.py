# from requests import get
from pyquery import PyQuery as pq
import yaml

data = {  
    "title": "集智俱乐部公众号",  
    "id": "gallery-wx",  
    "style": "style1 big lightbox onscroll-fade-in",  
    "content": "集智俱乐部公众号致力于报道复杂科学与人工智能领域的最新进展，特别关注跨学科研究与交流。集智俱乐部公众号目前已成为复杂科学领域最有影响力的科学媒体，受到国内交叉学科领域学者的广泛关注，并多次入围学术媒体Top榜单。",  
    "pictures": [  
        
    ]  
}

d = pq(url='https://swarma.org/')
for a in d('.widget_suxingme_post>li>a'):
    thumb = pq(a)('img')[0].attrib['data-original']
    if thumb.startswith('/'):
        thumb = 'https://swarma.org' + thumb
    post = {  
            "title": a.attrib['title'],  
            "content": "",  
            "image": a.attrib['href'],  
            "thumb": thumb,  
            "button": "阅读"  
        } 
    data["pictures"].append(post)

with open("gallery_wx.yaml", "w", encoding='utf8') as f:  
    yaml.dump(data, f, allow_unicode=True)  

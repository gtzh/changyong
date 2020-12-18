import requests
from lxml import etree
import time
from tzhutils import *
import json

def download_pdfs(pdf_title, pdf_url): 
    filename = 'pdf_files/' + pdf_title + '.pdf'
    content = requests.get(pdf_url).content
    with open(filename, 'wb') as f:
        f.write(content)
    print(f"save '{filename}' file successfully!")


def _post():
    pdf_items = {}
    headers = {
        'Host': 'www.cninfo.com.cn',
        'Origin': 'http://www.cninfo.com.cn',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
        'Cookie': 'JSESSIONID=1325FC27DEB9246D1437B08EBD4DEDC7; routeId=.uc1; cninfo_user_browse=002732,9900022959,%E7%87%95%E5%A1%98%E4%B9%B3%E4%B8%9A; insert_cookie=37836164; SID=f4eff7bd-5e17-4596-a135-6c4c6f8f5454; _sp_ses.2141=*; _sp_id.2141=9059b6dc-aa55-44e6-a68c-eecb22501c53.1608263889.2.1608270125.1608264975.4df0e2e3-5340-443a-a10a-4ede2cc580a0',
        'Connection': 'keep-alive',
        'Referer': 'http://www.cninfo.com.cn/new/disclosure/stock?stockCode=002732&orgId=9900022959',
        'X-Requested-With': 'XMLHttpRequest',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    }
    
    for page in range(1, total_page+1):
        data = {
        'stock': '002732,9900022959',
        'pageSize': '30',
        'pageNum': page,
        'column': 'szse',
        'plate': 'sz',
        }
        res = requests.post('http://www.cninfo.com.cn/new/hisAnnouncement/query',headers=headers, data= data).text
        json_block = json.loads(res)
        items = json_block['announcements']
        for item in items:
            if item:
                pdf_title = item['announcementTitle']
                pdf_url = head_url + item['adjunctUrl']
                pdf_items[pdf_title] = pdf_url
                download_pdfs(pdf_title, pdf_url)
    print(pdf_items)
    return pdf_items




if __name__ == "__main__":
    total_page = 24
    head_url = 'http://static.cninfo.com.cn/'
    _post()

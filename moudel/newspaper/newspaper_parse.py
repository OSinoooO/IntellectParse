import json
import re
import retrying
from newspaper import Article
from html.parser import unescape


@retrying.retry(stop_max_attempt_number=3)
def parse_from_url(url: str) -> dict:
    """调用 newspaper 处理 url"""
    ret = Article(url,
                  browser_user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.16 Safari/537.36 Edg/79.0.309.15',
                  request_timeout=30,
                  keep_article_html=True)
    ret.download()  # 下载网页
    if ret.download_state == 2:
        ret.parse()  # 解析网页
        item = {
            'url': url,
            'title': ret.title,
            'keywords': ret.meta_keywords,
            'description': ret.meta_description,
            'author': ret.authors,
            'publishdate': str(ret.publish_date) if ret.publish_date else '',
            'content': ret.text,
            'content_html': re.sub(r'\r|\n|\t', '', unescape(ret.article_html)),
        }
        return item
    else:
        raise Exception(f'Page download error, download_state: {ret.download_state}')


if __name__ == '__main__':
    import json
    test_url = 'https://www.bbc.com/zhongwen/simp/world-51869081'
    print(json.dumps(parse_from_url(test_url)))

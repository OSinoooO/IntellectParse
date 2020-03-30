import requests
import retrying
from gne import GeneralNewsExtractor


@retrying.retry(stop_max_attempt_number=3)
def parse_from_html(html: str, url: str) -> dict:
    """根据 html 提取新闻内容, 该 url 仅用于返回（不做处理）"""
    extractor = GeneralNewsExtractor()
    try:
        result = extractor.extract(html, with_body_html=True)
    except Exception as e:
        raise Exception(f'Html parsing error, reason: {e}')
    result['url'] = url
    return result


if __name__ == '__main__':
    from pprint import pprint
    test_url = 'https://www.bbc.com/zhongwen/simp/world-51869081'
    response = requests.get(test_url)
    pprint(parse_from_html(response.text, test_url))
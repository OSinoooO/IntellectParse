import uvicorn
from fastapi import FastAPI, Response
from moudel.newspaper import newspaper_parse
from moudel.gne import gne_parse
from pydantic import BaseModel
from items import *

app = FastAPI()

data_temp = {
    'status': 'ok',
    'result': ''
}


@app.get('/')
async def index():
    content = 'Welcome to Intellect Parse API'
    return Response(f'''<html><script src="https://code.jquery.com/jquery-3.1.1.min.js"></script><p id="welcome" style="user-select:none;display:none;font-weight:400;font-size:50px;position:absolute;left:50%;top:40%;transform:translate(-50%,-50%);">{content}</p><script language="javascript" type="text/javascript">$("#welcome").show("slow");</script></html>''')


@app.get('/newspaper')
async def newspaper_api(target_url: str):
    """使用 newspaper 解析网页"""
    data = data_temp.copy()
    try:
        data['result'] = newspaper_parse.parse_from_url(target_url)
    except Exception as e:
        data['status'] = 'error'
        data['result'] = str(e)
    return item


@app.post('/gne')
async def gne_api(item: GneItem):
    item = item.dict()
    data = data_temp.copy()
    try:
        data['result'] = gne_parse.parse_from_html(item.get('html'), item.get('url'))
    except Exception as e:
        data['status'] = 'error'
        data['result'] = str(e)
    return data


@app.get('/diffbot')
async def diffbot_api():
    pass


if __name__ == '__main__':
    uvicorn.run(app)
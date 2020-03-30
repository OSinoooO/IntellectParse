# IntellectParse

新闻网页智能解析接口，集成现有的开源解析器。



- ### newspaper

接口：（GET）http://127.0.0.1:8000/newspaper?target_url=[替换为目标网址]



- ### gne

接口：（POST）http://127.0.0.1:8000/gne

body：（JSON）{"html": 网页源码, "url": 网址}
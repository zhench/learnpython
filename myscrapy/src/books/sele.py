from scrapy.selector import Selector
from scrapy.http import HtmlResponse

text = '''<html>
        <body>
                <h1>Hello World</h1>
                <h1>Hello Scrapy</h1>
                <b>Hello python</b>
                <ul>
                        <li>C++</li>
                        <li>Java</li>
                        <li>Python</li>
                </ul>
        <body>
</html>'''


selector = Selector(text=text)
print(selector)

body = text
response = HtmlResponse(url='http://www.example.com',
                        body=body, encoding='utf8')
selector = Selector(response=response)
print(selector)

selector_list = selector.xpath('//h1')
print(selector_list)
for sel in selector_list:
    print(sel.xpath('./text()'))
print(selector_list.xpath('text()'))

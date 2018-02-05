# -*- coding:utf-8 -*-
import xlrd
import xlwt
import json
from urllib import request,parse


xlspath='./address/jixianaddresses.xlsx'
filepath='./address/test.xls'

def searchpoi(strpoi):
    print('正在查询%s' % strpoi)
    key='03498a1766c02d2e3cd5b1566f445fb5'
    keywords=parse.quote(strpoi)
    city=parse.quote('蓟县')
    url='http://restapi.amap.com/v3/place/text?key='+key+'&keywords='+keywords+'&types=&city='+city+'&children=1&offset=20&page=1&extensions=all'
    with request.urlopen(url) as f:
        data=f.read().decode('utf-8')
        jsondata=json.loads(data)
        count=int(jsondata['count'])
        if count==0:
            return
        nameaddr=''
        for i in range(len(jsondata['pois'])):
            poi=jsondata['pois'][i]
            address=poi['address']
            if isinstance(poi['address'],list):
                address='无'
            nameaddr+='  '+str(i+1)+':'+poi['name']+' 的地址是：'+address
        return nameaddr


def readexcel(filepath):
    data=xlrd.open_workbook(filepath)
    table=data.sheets()[0]
    nrows=table.nrows
    print(nrows)
    dict_address={}
    for i in range(nrows):
        if i==0:
            continue
        cell_value=table.cell(i,2).value
        #print(cell_value)
        address=searchpoi(strpoi=cell_value)
        dict_address[cell_value]=address
        print(len(dict_address))
       
    return dict_address

def writexls(filepath,addresses=None):
    f=xlwt.Workbook()
    sheet1=f.add_sheet(u'sheet1',cell_overwrite_ok=True)
    i=0
    for key in addresses:
        sheet1.write(i,0,i+1)
        sheet1.write(i,1,key)
        sheet1.write(i,2,addresses[key])
        i+=1
    f.save(filepath)

jixian_address=readexcel(xlspath)
writexls(filepath,addresses=jixian_address)
print('done')

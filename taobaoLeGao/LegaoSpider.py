# -*- coding: utf-8 -*-
"""
Created on 2021-09-22 19:37:56
---------
@summary:
---------
@author: Tuling
"""
import codecs
import csv
import json
import re
import feapder
f = codecs.open('淘宝乐高.csv','a','gbk')
writer = csv.writer(f)
writer.writerow(["标题","商家","地址","付款人数","价格"])

class Xx(feapder.AirSpider):
    def start_requests(self):
        headers= {
        'cookie': 'miid=120076508994945398; cna=s5XgGHTA/QACAa8N+wOHxkKB; thw=cn; t=09ef0b533d5f5014504435330c5b23a7; _m_h5_tk=9afb8815f59ecdd6d90f960fa950b608_1632318660385; _m_h5_tk_enc=32d88fe37367c7d8191e0d6ccaa6aeb8; xlly_s=1; _samesite_flag_=true; cookie2=11352226bbcc90e131fb8e2d9a3a78a2; _tb_token_=ed63bd661b9e0; sgcookie=E1002hzxj0%2BkNyK8SW%2BdTaNG6Ou62zkRwlh9oIg6TSxlgEVkBKN0WwQH%2Fw9SRRgzrUuiBsCz5ZwM5v0Z0kwmK1MF3NBMh3Yh3q5FfwrTVvf7M0s%3D; unb=3071675414; uc3=nk2=AQc0Nbnx9S4H8pkl%2BA%3D%3D&vt3=F8dCujdzW2tWEWdg7bI%3D&id2=UNDTw7IM5DYpuA%3D%3D&lg2=WqG3DMC9VAQiUQ%3D%3D; csg=bc1d7fa4; lgc=bcptbtptp%5Cu5F20%5Cu5F20; cancelledSubSites=empty; cookie17=UNDTw7IM5DYpuA%3D%3D; dnk=bcptbtptp%5Cu5F20%5Cu5F20; skt=d666d4e9a1995a28; existShop=MTYzMjMwOTgxNQ%3D%3D; uc4=id4=0%40UgcjZF9065lxnqGgFvjXZ5vSp20%2B&nk4=0%40A6qJ%2FkooLkypmChVx5EvcDW8EO%2BkDz4V; tracknick=bcptbtptp%5Cu5F20%5Cu5F20; _cc_=VT5L2FSpdA%3D%3D; _l_g_=Ug%3D%3D; sg=%E5%BC%A043; _nk_=bcptbtptp%5Cu5F20%5Cu5F20; cookie1=BxZoM4%2FT%2BmdjW5MEqR9Mt5craH93rw995UJ3Ud496K4%3D; enc=zdYu03KQWYVyBA9LCueMaJsN0HdEWldS4oFNif9IGQEQaT%2B3o%2Bpb4Mv8qOADxIw325G1hjBZ8c6veP2pQaHigw%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; mt=ci=109_1; uc1=cookie16=VFC%2FuZ9az08KUQ56dCrZDlbNdA%3D%3D&cookie21=U%2BGCWk%2F7p4mBoUyS4E9C&cookie14=Uoe3dYITfaJ8EQ%3D%3D&existShop=false&cookie15=UtASsssmOIJ0bQ%3D%3D&pas=0; JSESSIONID=A10BE1A97F1454FFCFEE08EC1DA77AD4; tfstk=cmMcB3i71jPXWIPoOKwjV8YaxfORZiBa-AkSUvVE8Z3Q65kPiGfPThuHqr0mB11..; l=eBNHRWw4gR5fSGh9BOfwourza77OSIRA_uPzaNbMiOCPOzfp5yfRW6FgCAT9C3GVh6k6R35NsM4TBeYBqS24n5U62j-la_kmn; isg=BNDQjj_8hRiU-VkcaLeqLGneoR4imbTjIXyEsMqhnCv-BXCvcqmEcya33c3l0my7',
            'referer': 'https://s.taobao.com/search?q=%E4%B9%90%E9%AB%98%E6%95%B0%E6%8D%AE&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20210922&ie=utf8',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
        }
        for i in range(0,2200,44):
            yield feapder.Request(f"https://s.taobao.com/search?q=%E7%A7%AF%E6%9C%A8&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.21814703.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&p4ppushleft=2%2C48&s={i}",headers=headers)

    def parse(self, request, response):
        # print(response.text)
        '''
        商品的名称 店铺的名称，付款人数，位置
        :param request:
        :param response:
        :return:
        '''
        try:
            data = re.findall('{"pageName".*?};', response.text)
            re_script = re.compile(';', re.I)
            res = re_script.sub('', str(data))
            formats = eval(res)
            s = json.loads(formats[0])
            res1 = s.get('mods')
            res2 = res1.get('itemlist')
            res3 = res2.get('data')
            res4 = res3.get('auctions')
            for i in res4:
                title = i.get('title')
                dr = re.compile(r'<[^>]+>', re.S)
                dd = dr.sub('', title)
                nick = i.get('nick')
                item_loc = i.get('item_loc')
                view_sales = i.get('view_sales')
                view_price = i.get('view_price')
                writer.writerow([dd,nick,item_loc,view_price,view_sales])
        except Exception as e:
            print('被监测了，需要切换IP地址')

if __name__ == "__main__":
    Xx().start()


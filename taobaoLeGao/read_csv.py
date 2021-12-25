import pandas as pd
import numpy as np
import jieba
import time
from pyecharts.charts import Bar,Line,Map,Page,Pie
from pyecharts import options as opts
# from pyecharts.globals import SymbolType
df_tb = pd.read_csv(r'./淘宝乐高.csv',encoding='gbk')
# print(df_tb.head(100))
# shop_top10 = df_tb.groupby('标题')['商家'].sum().sort_values(ascending=False).head(10)
# print(shop_top10)
shop_top10 = df_tb.groupby('商家')['付款人数'].sum().sort_values(ascending=False).head(10)


#条形图
#bar1 = Bar(init_opts=opts.InitOpts(width='1350px', height='750px'))
bar1 = Bar()
# bar1.theme('vintage')
bar1.add_xaxis(shop_top10.index.tolist())
bar1.add_yaxis('', shop_top10.values.tolist())
bar1.set_global_opts(title_opts=opts.TitleOpts(title='乐高销量排名Top10淘宝店铺'),
                     xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-15)),
                     visualmap_opts=opts.VisualMapOpts(max_=28669)
                    )

bar1.render()
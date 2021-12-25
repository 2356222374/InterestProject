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

province_num = df_tb.groupby('商家')['付款人数'].sum().sort_values(ascending=False)

# province_num[:10]
map1 = Map()
map1.add("",[list(z) for z in zip(province_num.index.tolist(),province_num.values.tolist())],
       maptype='china')
map1.set_global_opts(
    title_opts = opts.TitleOpts(title='国内各产地乐高销量分布图'),
    visualmap_opts = opts.VisualMapOpts(max_=172277)
)
map1.render()
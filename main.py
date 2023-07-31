import plotly.express as px
import pandas as pd
import numpy as np
import plotly

gapminder=px.data.gapminder()

Switzerland  = gapminder[gapminder["country"] == "Switzerland"]

fig=px.bar(Switzerland,  # 上面指定的数据
       x="year",  # 横坐标
       y="pop",  # 纵坐标
       color="pop")  # 颜色取值

# pip install -U kaleido
# fig.write_image("yourfile.png") 

# plotly.offline.plot(fig, filename='lifeExp.html')
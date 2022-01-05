import plotly.express as px
import plotly.figure_factory as ff
import pandas as pd

df = pd.read_csv("amazon mobile brand sales data.csv")
fig = ff.create_distplot([df["Avg Rating"].tolist()],["Rating"],show_hist = False )
fig.show()

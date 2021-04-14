import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px
from plotly.offline import plot


sorted10 = pd.read_json(r'/home/kaka/Downloads/sort/src/tej')
sorted50 = pd.read_json(r'/home/kaka/Downloads/sort/src/tej50')
sorted100 = pd.read_json(r'/home/kaka/Downloads/sort/src/tej100')
sorted1000 = pd.read_json(r'/home/kaka/Downloads/sort/src/tej1000')
sorted10000 = pd.read_json(r'/home/kaka/Downloads/sort/src/tej10000')
df = pd.read_json(r'/home/kaka/Downloads/sort/src/k100')

df['cn'] = df.apply(lambda row: (row['compare'] / row.amount), axis=1)
df['chn'] = df.apply(lambda row: (row['changes'] / row.amount), axis=1)
df_1000mq = df.loc[(df['name'] != 'insert')]
df_1000mq["const"] = df_1000mq.apply(lambda row: (row['compare'] / (
                                    row.amount * np.log(row.amount))), axis=1)

tmp = 1.9
maksik = 10100
step = 100
cos = pd.DataFrame(data=None)
cos["name"] = ["log" for x in range(100, maksik, 100)]
cos["amount"] = [x for x in range(100, maksik, 100)]
cos["compare"] = [tmp * x * np.log(x) for x in range(100, maksik, 100)]
cos["changes"] = [tmp * x * np.log(x) for x in range(100, maksik, 100)]
cos["time"] = [tmp * x * np.log(x) for x in range(100, maksik, 100)]
cos["cn"] = [tmp * x * np.log(x) for x in range(100, maksik, 100)]
cos["chn"] = [tmp * x * np.log(x) for x in range(100, maksik, 100)]
cos["const"] = [tmp for x in range(100, maksik, 100)]

df_dual = df.loc[df['name'] == "dual"]
df_dual = df_dual.groupby(['name', "amount"]).mean().reset_index()
df_dual["const"] = df_dual.apply(lambda row: (row['compare'] / (
                                    row.amount * np.log(row.amount))), axis=1)

df_quick = df.loc[df['name'] == "quick"]
df_quick = df_quick.groupby(['name', "amount"]).mean().reset_index()
df_quick["const"] = df_quick.apply(lambda row: (row['compare'] / (
                                    row.amount * np.log(row.amount))), axis=1)


frames = [df_1000mq, cos]

elo = pd.concat(frames)
df_1000mq['name_id'] = df_1000mq.groupby('name').grouper.group_info[0]

 
sns.lineplot(data = df_1000mq, x = 'amount', y = 'chn', hue = 'name')

sns.lineplot(data = elo, x = 'amount', y = 'const', hue = 'name')


fig = px.scatter_matrix(data_frame = df_1000mq, 
                        dimensions = ['amount', 'compare', 'changes', 
                                      'time', 'cn', 'chn', 'const'], 
                        title = "Anzaliza Algorytmow", color = "name")
plot(fig)


fig = px.parallel_coordinates(data_frame = df_1000mq, 
                        dimensions = ['amount', 'compare', 'changes', 'time',
                                      'cn', 'chn', 'const'],
                        title = "Anzaliza Algorytmow", color="name_id")
plot(fig)

fig = px.scatter(data_frame=df_1000mq, x='time', y='const', size='changes',
                 color='name', size_max=10, animation_frame='amount', 
                 range_y=[0, 2.5], range_x=[0.0001, 0.08])
plot(fig)

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.offline import plot

from sklearn.metrics import confusion_matrix, classification_report

def label(row):
    if row['name_id'] == 0:
        return 'amazing'
    elif row['name_id'] == 1:
        return 'dual'
    elif row['name_id'] == 2:
        return 'merge'
    else:
        return 'quick'

df = pd.read_json(r'/home/kaka/Downloads/sort/src/k100')
df['cn'] = df.apply(lambda row: (row['compare'] / row.amount), axis=1)
df['chn'] = df.apply(lambda row: (row['changes'] / row.amount), axis=1)
df = df.loc[(df['name'] != 'insert')]
df["const"] = df.apply(lambda row: (
    row['compare'] / (row.amount * np.log(row.amount))), axis=1)
df['name_id'] = df.groupby('name').grouper.group_info[0]

data = df.iloc[:, 1:5].to_numpy()
target = df.iloc[:, 8].to_numpy()

data_train, data_test, target_train, target_test = train_test_split(
    data, target, test_size=0.3)

model = LogisticRegression(max_iter=10000)
model.fit(X=data_train, y=target_train)


y_pred = model.predict(data_test)
y_true = target_test
diff = y_pred == y_true
diff = diff.astype(int)


predicted = pd.DataFrame(data=data_test[:,0], columns=['amount'])
predicted['compare'] = pd.DataFrame(data=data_test[:,1], columns=['compare'])
predicted['changes'] = pd.DataFrame(data=data_test[:,2], columns=['changes'])
predicted['time'] = pd.DataFrame(data=data_test[:,3], columns=['time'])

predicted['pred'] = pd.DataFrame(diff)
predicted['name_id'] = pd.DataFrame(data=target_test)

tmp = predicted.apply(lambda row: (label(row)), axis = 1)
predicted['name'] = tmp
predicted["const"] = predicted.apply(lambda row: (row['compare'] / (
    row.amount * np.log(row.amount))), axis=1)
predicted = predicted.sort_values(['amount'])

fig = px.scatter(data_frame=predicted, x='time', y='const', size='changes', 
                 text = 'pred', color='name', size_max=10, 
                 animation_frame='amount', range_y=[0, 2.5], 
                 range_x=[0.0001, 0.08], title="Predykcja Algorytmu")



ans= confusion_matrix(target_test, y_pred)
ans = pd.DataFrame(ans, columns=['amazing', 'dual', 'merge', 'quick'], 
                    index = ['amazing', 'dual', 'merge', 'quick'])
info= classification_report(target_test, y_pred)
score = model.score(data_test, target_test)
# %%
plot(fig)
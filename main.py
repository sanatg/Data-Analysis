import csv
import pandas as pd
import plotly.graph_objects as plotly

csv_read = pd.read_csv('https://raw.githubusercontent.com/whitehatjr/Data-Analysis-by-visualisation/master/data.csv')

csv_read_student = csv_read.loc[csv_read['student_id']=="TRL_987"]

print(csv_read_student.groupby("level")["attempt"].mean())
figure = plotly.Figure(plotly.Scatter(
    x=csv_read_student.groupby("level")["attempt"].mean(),
    y=['Level 1','Level 2','Level 3','Level 4'],
    orientation='h'))

figure.show()

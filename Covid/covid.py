import pandas as Py
import plotly_express as Px

Data_Frame = Py.read_csv('Covid\Copy+of+data+-+data.csv')
#Graph = Px.line(Data_Frame,x = 'date',y='cases',color='country',title='Covid Cases')
Graph = Px.scatter(Data_Frame,x = 'date',y='cases',color='country',title='Covid Cases',size = 'cases')
Graph.show()
import pandas as pd 
import plotly_express as px

line1 = pd.read_csv("data.csv")

graph = px.scatter(line1, x="Population", y="InternetUsers", color ="Country", size="Percentage", title="Population VS Internet Users")
print("Adios!")
graph.show()
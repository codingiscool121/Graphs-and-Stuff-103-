import plotly.express as px
import pandas as pd

line1 = pd.read_csv("line_chart.csv")
# print(line1.tail())
graph = px.line(line1,x="Year", y = "Per capita income", color="Country", title="Yearly Per Capita Income(Country)")
print("Bouncing you there...")
graph.show()
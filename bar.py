import pandas as pd
import plotly.express as px

line1 = pd.read_csv("data.csv")
graph = px.bar(line1, x="Country", y="InternetUsers", color="Per capita")
print("Bouncing you there...")
graph.show()

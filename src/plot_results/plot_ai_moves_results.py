#!/usr/bin/env python
import pandas as pd
import plotly.express as px

import pathlib


data_dir = pathlib.Path('../data/results/ai_moves/')
data_files = data_dir.iterdir()

data = pd.read_csv(max(data_files))
fig = px.scatter(x=range(len(data)), y=data.iloc[:, 0].tolist())
fig.show()

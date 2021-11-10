#!/usr/bin/env python
import pandas as pd
import plotly.graph_objects as go
from pathlib import Path


data_files = Path('../data/results/random_moves/').glob('202111*.csv')
data = [pd.read_csv(path) for path in data_files]

for c in ['score', 'max_tile']:
    fig = go.Figure()
    for d in data:
        fig.add_trace(go.Histogram(x=d[c]))

    fig.show()

import pandas as pd
import networkx as nx
import json

def graph_reader(input_path):
    edges = pd.read_csv(input_path)
    graph = nx.from_edgelist(edges.values.tolist())
    return graph

def json_dumper(data, path):
    with open(path, 'w') as outfile:
        json.dump(data, outfile)

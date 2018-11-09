import pandas as pd
import networkx as nx
import json
from texttable import Texttable

def argument_printer(args):
    """
    Function to print the arguments in a nice tabular format.
    :param args: Parameters used for the model.
    """
    args = vars(args)
    keys = sorted(args.keys())
    t = Texttable() 
    t.add_rows([["Parameter", "Value"]] +  [[k.replace("_"," ").capitalize(),args[k]] for k in keys])
    print(t.draw())

def graph_reader(input_path):
    edges = pd.read_csv(input_path)
    graph = nx.from_edgelist(edges.values.tolist())
    return graph

def json_dumper(data, path):
    with open(path, 'w') as outfile:
        json.dump(data, outfile)

from parser import parameter_parser
from model import LabelPropagator
from print_and_read import graph_reader

def create_and_run_model(args):
    
    graph = graph_reader(args.input)
    model = LabelPropagator(graph, args)
    model.do_a_series_of_propagations()

if __name__ == "__main__":
    args = parameter_parser()
    create_and_run_model(args)




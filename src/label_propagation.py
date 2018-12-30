from parser import parameter_parser
from model import LabelPropagator
from print_and_read import graph_reader, argument_printer

def create_and_run_model(args):
    """
    Method to run the model.
    :param args: Arguments object.
    """
    graph = graph_reader(args.input)
    model = LabelPropagator(graph, args)
    model.do_a_series_of_propagations()

if __name__ == "__main__":
    args = parameter_parser()
    argument_printer(args)
    create_and_run_model(args)

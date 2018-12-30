import argparse

def parameter_parser():

    """
    A method to parse up command line parameters. By default it does community detection on the Facebook politicians network.
    The default hyperparameters give a good quality clustering. Default weighting happens by neighborhood overlap.
    """

    parser = argparse.ArgumentParser(description = "Run Label Propagation.")

    parser.add_argument("--input",
                        nargs = "?",
                        default = "./data/politician_edges.csv",
	                help = "Input graph path.")

    parser.add_argument("--assignment-output",
                        nargs = "?",
                        default = "./output/politician.json",
	                help = "Assignment path.")

    parser.add_argument("--weighting",
                        nargs = "?",
                        default = "overlap",
	                help = "Overlap weighting.")

    parser.add_argument("--rounds",
                        type = int,
                        default = 30,
	                help = "Number of iterations. Default is 30.")

    parser.add_argument("--seed",
                        type = int,
                        default = 42,
	                help = "Random seed. Default is 42.")

    return parser.parse_args()


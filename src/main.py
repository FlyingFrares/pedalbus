import data_parser
import os
import graph

test_file = "pedibus_10"  # edit this if you do not want to pass a command line arg.

file_path = ".." + os.path.sep + "instances" + os.path.sep + test_file + ".dat"

data = data_parser.get_data(file_path)

gr = graph.Graph(data)

t2 = tuple(map(lambda x: isinstance(x, float) and round(x, 2) or x, gr.get_root_vector())) # round to 2 decimal places the tuple

print(t2)
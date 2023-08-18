import data_parser
import os
import graph

test_file = "pedibus_10"  # edit this if you do not want to pass a command line arg.

file_path = "instances" + os.path.sep + test_file + ".dat"

data = data_parser.get_data(file_path)

gr = graph.Graph(data)

print(gr.get_ordered_vector([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
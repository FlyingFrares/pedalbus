import data_parser
import os

test_file = "pedibus_10"  # edit this if you do not want to pass a command line arg.

file_path = "instances" + os.path.sep + test_file + ".dat"

data = data_parser.get_data(file_path)

print(data)
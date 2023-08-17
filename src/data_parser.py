from amply import Amply

def get_data(file_path):
    """
    Get the data contained in the Ampl input file
    :param file_path: the file_path of the input file
    :return: An object that contains the data contained in the input file
    """

    # I put in file_content the content of the file
    with open(file_path, 'r') as ampl_file:
        file_content = ampl_file.read()

    # Now I use the variable temp to transform the file content in order to be compatible with amply
    first_row = file_content.split('\n', 1)[0]
    
    temp = file_content

    aux_str1 = """param coordX{random_text};
    param coordX"""

    aux_str2 = """param coordY{random_text};
    param coordY"""

    # Now I use the three auxiliary strings that I declared above to modify temp

    temp = temp.split('param coordX', 1)
    temp = temp[0] + aux_str1 + temp[1]

    temp = temp.split('param coordY', 1)
    temp = temp[0] + aux_str2 + temp[1]

    # Now temp is compatible with Amply
    return Amply(temp)
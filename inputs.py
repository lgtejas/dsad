from os.path import  isfile

def read_inputs(path="./inputPS3.txt"):
    inputs =[]
    if not isfile(path):
        print(f'Input file {path} not found')
        return
    with open(path, 'r') as f:
        lines = f.readlines()
        for line_number, line in enumerate(lines):
            split_numbers = line.split(',')
            try:
                split_numbers = [int(n) for n in split_numbers]
                inputs.append((split_numbers))
            except :
                print(f'Error reading line number {line_number + 1} with value  - {split_numbers}, may contain invalid/non integer values')
    return inputs



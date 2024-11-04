import sys
import json
from functools import reduce

def cell_to_code(cell):
    # Code
    if cell['cell_type'] == 'code':
        return '#%%\n' + ''.join(cell['source']) + '\n'
    
    # Markdown 
    return ''.join(list(map(lambda s: "# " + s, cell['source']))) + '\n'

def is_exercise(cell):
    return cell['cell_type'] == 'markdown' and '# Ćwiczenie' in cell['source'][0]

if __name__ == '__main__':
    infile_name = sys.argv[1]

    with open(infile_name, 'r') as f:
        data = json.load(f)
    
    code = list(map(cell_to_code, data['cells']))

    outfile_name = infile_name.replace('.ipynb', '.py')
    with open(outfile_name, 'w') as f:
        f.write(''.join(code))
    
    num_exercises = reduce(lambda acc, cell: acc + 1 if is_exercise(cell) else acc, data['cells'], 0)
    print(f'Number of exercises: {num_exercises}')
    
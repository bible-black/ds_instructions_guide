import json

notebook_path = 'notebook/data_quality_assessment.ipynb'
output_path = 'notebook_cells_list.txt'

with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

with open(output_path, 'w', encoding='utf-8') as f_out:
    f_out.write(f"Total cells: {len(nb['cells'])}\n")
    code_cell_index = 0
    for i, cell in enumerate(nb['cells']):
        cell_type = cell.get('cell_type')
        exec_count = cell.get('execution_count')
        source = cell.get('source', [])
        first_line = source[0].strip() if source else ""
        
        if cell_type == 'code':
            code_cell_index += 1
            f_out.write(f"Cell Index: {i}, Code Cell Index: {code_cell_index}, Exec Count: {exec_count}\n")
            f_out.write(f"Source: {first_line[:100]}...\n")
            f_out.write("-" * 20 + "\n")

import json

notebook_path = 'notebook/data_quality_assessment.ipynb'

with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

print(f"Total cells: {len(nb['cells'])}")
for i, cell in enumerate(nb['cells']):
    cell_type = cell.get('cell_type')
    exec_count = cell.get('execution_count')
    source = cell.get('source', [])
    first_line = source[0].strip() if source else ""
    
    if cell_type == 'code':
        print(f"Index {i}: Code, Exec Count: {exec_count}, Source: {first_line[:50]}...")

import json

notebook_path = 'notebook/data_quality_assessment.ipynb'

with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

for i, cell in enumerate(nb['cells']):
    if cell.get('execution_count') == 14:
        print(f"--- Cell found with execution_count 14 (Index {i}) ---")
        print("Source:")
        print(''.join(cell['source']))
        print("\nOutputs:")
        for output in cell.get('outputs', []):
            if output.get('output_type') == 'error':
                 print(f"Error ({output.get('ename')}): {output.get('evalue')}")
                 for trace in output.get('traceback', []):
                     print(trace)
            elif 'text' in output:
                 print(''.join(output['text']))
            elif 'data' in output and 'text/plain' in output['data']:
                 print(''.join(output['data']['text/plain']))
        break
else:
    print("Cell with execution_count 14 not found.")

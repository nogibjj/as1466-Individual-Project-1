import nbformat
from nbconvert import HTMLExporter
from nbconvert.preprocessors import ExecutePreprocessor

def create_hidden_html_notebook(notebook_path, output_path):
    with open('main.ipynb', 'r', encoding='utf-8') as nb_file:
        notebook = nbformat.read(nb_file, as_version=4)

    # Create an ExecutePreprocessor to execute the code cells
    executor = ExecutePreprocessor(timeout=None)
    executor.preprocess(notebook, {'metadata': {'path': ''}})

    # Remove code cells
    notebook.cells = [cell for cell in notebook.cells if cell.cell_type != 'code']

    # Create an HTMLExporter instance
    html_exporter = HTMLExporter()
    (body, resources) = html_exporter.from_notebook_node(notebook)

    # Save the HTML output to a file
    with open(output_path, 'w', encoding='utf-8') as html_file:
        html_file.write(body)

if __name__ == '__main__':
    create_hidden_html_notebook('main.ipynb', 'main_output.html')


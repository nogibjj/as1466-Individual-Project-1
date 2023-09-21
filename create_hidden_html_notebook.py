import nbformat
from nbconvert import HTMLExporter

def create_hidden_html_notebook(notebook_path, output_path):
    with open(notebook_path, 'r', encoding='utf-8') as nb_file:
        notebook = nbformat.read(nb_file, as_version=4)

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

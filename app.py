import streamlit as st
import nbformat
import pandas as pd
from nbconvert import PythonExporter
from io import StringIO

def load_notebook(file_path):
    """Carrega e converte um notebook Jupyter para código Python."""
    with open(file_path, "r", encoding="utf-8") as f:
        nb = nbformat.read(f, as_version=4)
    exporter = PythonExporter()
    source_code, _ = exporter.from_notebook_node(nb)
    return source_code

def extract_dataframes(source_code):
    """Executa o código extraído e retorna os DataFrames encontrados."""
    globals_dict = {}
    try:
        exec(source_code, globals_dict)
    except Exception as e:
        st.error(f"Erro ao executar o código do notebook: {e}")
        return {}
    return {key: value for key, value in globals_dict.items() if isinstance(value, pd.DataFrame)}

def main():
    st.title("Visualização de Tabelas do Notebook")
    notebook_path = "report.ipynb"
    
    source_code = load_notebook(notebook_path)
    dataframes = extract_dataframes(source_code)
    
    if dataframes:
        selected_df = st.selectbox("Selecione um DataFrame:", list(dataframes.keys()))
        st.dataframe(dataframes[selected_df])
    else:
        st.warning("Nenhum DataFrame foi encontrado no notebook.")

if __name__ == "__main__":
    main()

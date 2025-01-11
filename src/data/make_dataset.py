import os
import pandas as pd
from tkinter import filedialog, Tk

def select_file():
    root = Tk()
    root.withdraw()
    return filedialog.askopenfilename(title="Select file", filetypes=[("Excel files", "*.xlsx *.xls")])

def ensure_data_files():
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    root_dir = os.path.dirname(root_dir)
    data_dir = os.path.join(root_dir, "data")
    raw_dir = os.path.join(data_dir, "raw")
    external_dir = os.path.join(data_dir, "external")

    materials_path = os.path.join(raw_dir, "Materials.xlsx")
    bom_path = os.path.join(raw_dir, "BOM.xlsx")
    input_path = os.path.join(external_dir, "input.xlsx")

    if not os.path.exists(materials_path):
        print("Select the Materials file:")
        materials_path = select_file()
    if not os.path.exists(bom_path):
        print("Select the BOM file:")
        bom_path = select_file()
    if not os.path.exists(input_path):
        print("Select the Input file:")
        input_path = select_file()

    return materials_path, bom_path, input_path

def clean_materials(file_path):
    mat_df = pd.read_excel(file_path)
    mat_df = mat_df.sort_values(by=['Material', 'Created'], ascending=[True, False])
    mat_df = mat_df.drop_duplicates(subset='Material', keep='first')
    return mat_df

def clean_bom(file_path):
    return pd.read_excel(file_path)

def clean_input(file_path):
    return pd.read_excel(file_path)
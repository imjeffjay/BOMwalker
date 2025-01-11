import pandas as pd

from src.data.make_dataset import ensure_data_files, clean_materials, clean_bom, clean_input
from src.features.build_features import get_all_components_for_material, find_root_materials
from src.models.process_chunks import process_materials_in_chunks
import os

def main():
    materials_path, bom_path, input_path = ensure_data_files()

    mat_df = clean_materials(materials_path)
    bom_df = clean_bom(bom_path)
    input_df = clean_input(input_path)

    materials_to_process = input_df["Material"].tolist()

    timestamp = pd.Timestamp.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"data/processed/results_{timestamp}.csv"

    process_materials_in_chunks(
        materials_to_process, mat_df, bom_df, find_root_materials, chunk_size=100, output_file=output_file
    )

if __name__ == "__main__":
    main()
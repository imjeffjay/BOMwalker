import pandas as pd

def process_materials_in_chunks(materials, mat_df, bom_df, process_func, chunk_size=100, output_file='results.csv'):
    results = []
    for start in range(0, len(materials), chunk_size):
        end = start + chunk_size
        chunk = materials[start:end]
        chunk_results = []
        for material in chunk:
            result = process_func(material, mat_df, bom_df)
            chunk_results.append({
                'Material': material,
                'Results': result
            })
        results.extend(chunk_results)
        chunk_df = pd.DataFrame(chunk_results)
        chunk_df.to_csv(output_file, mode='a', header=not bool(start), index=False)
        print(f"Processed chunk {start // chunk_size + 1} / {len(materials) // chunk_size + 1}")
    return results
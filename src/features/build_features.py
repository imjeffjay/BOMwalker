def get_all_components_for_material(material, mat_df, bom_df):
    stack = [material]
    all_components = set()
    while stack:
        current_material = stack.pop()
        bom_id = mat_df[mat_df['Material'] == current_material]['BOM'].values
        if len(bom_id) > 0:
            components = bom_df[bom_df['BOM'] == bom_id[0]]['Component'].values
            for component in components:
                if component not in all_components:
                    all_components.add(component)
                    stack.append(component)
    return list(all_components)

def find_root_materials(component, mat_df, bom_df):
    def find_parents_recursive(component, visited):
        if component in visited:
            return visited
        visited.append(component)
        if not mat_df[mat_df['Material'] == component].empty and \
           mat_df.loc[mat_df['Material'] == component, 'MTyp'].iloc[0] == 'FERT':
            return visited
        parents = mat_df[mat_df['BOM'].isin(bom_df[bom_df['Component'] == component]['BOM'])]['Material'].tolist()
        for parent in parents:
            find_parents_recursive(parent, visited)
        return visited
    all_parents = find_parents_recursive(component, [])
    return [material for material in all_parents if material not in bom_df['Component'].unique()]
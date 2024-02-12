def build_category_tree(categories):
    category_tree = []

    # Create a dictionary to quickly look up categories by ID
    category_dict = {category.category_id: category for category in categories}

    # Build the category tree
    for category in categories:
        if category.parrent_id is None:
            # If the category has no parent, it is a top-level category
            category_tree.append({
                'id': category.category_id,
                'name': category.category_name,
                'children': build_subtree(category, category_dict),
            })

    return category_tree

def build_subtree(parent_category, category_dict):
    children = []

    # Find all categories with the current category as a parent
    subcategories = [category for category in category_dict.values() if category.parrent_id == parent_category.category_id]

    for subcategory in subcategories:
        # Recursively build the subtree for each subcategory
        children.append({
            'id': subcategory.category_id,
            'name': subcategory.category_name,
            'children': build_subtree(subcategory, category_dict),
        })

    return children
import os, json


def build_folder_hierarchy(root_path, excluded) -> dict:
    def traverse_folder(current_path):
        current_folder = {"files": [], "folders": {}}

        for item in os.listdir(current_path):
            item_path = os.path.join(current_path, item)

            if os.path.isdir(item_path) and item not in excluded:
                current_folder["folders"][item] = traverse_folder(item_path)

            elif os.path.isfile(item_path):
                current_folder["files"].append(item)

        return current_folder

    return traverse_folder(root_path)

def print_folder_hierarchy(path: str, excluded: list) -> None:
    hiearchy = build_folder_hierarchy(path, excluded)
    
    # helper function
    # def print_h(folder_hierarchy, indentation=0):
    #     if isinstance(folder_hierarchy, dict):
    #         for folder, content in folder_hierarchy.items():
    #             print("  " * indentation + f"{folder}/")
    #             print_folder_hierarchy(content, indentation + 1)
    #             files = content.get("files", [])
    #             if files:
    #                 print("  " * (indentation + 1) + "Files:")
    #                 for file in files:
    #                     print("  " * (indentation + 2) + file)

    # print_h(hiearchy)

    print(json.dump(hiearchy, indent=2))
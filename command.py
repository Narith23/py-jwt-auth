import os
import argparse


def create_structing_folder(folder_name, files):
    api_folder = os.path.join(os.getcwd(), "src")
    folder_path = os.path.join(api_folder, folder_name)

    if os.path.exists(folder_path):
        raise FileExistsError(
            f"The folder '{folder_name}' already exists in the '{api_folder}' directory."
        )

    # Create the main folder
    os.makedirs(folder_path)

    # Create multiple files inside the folder
    for file_name in files:
        with open(os.path.join(folder_path, file_name), "w") as file:
            file.write("# This is a sample {} file".format(file_name))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=f"Create a Project folder and files inside the '/src' directory."
    )
    parser.add_argument(
        "folder_name", type=str, help="Name of the folder to create inside '/src'"
    )

    args = parser.parse_args()

    folder_name = args.folder_name

    try:
        create_structing_folder(
            folder_name,
            ["__init__.py", "model.py", "router.py", "schemas.py", "services.py"],
        )
        print(
            f"{folder_name}' and files created successfully inside the '/src' directory!"
        )
    except FileExistsError as e:
        print(e)

from functions.get_files_info import validate_path
from os import makedirs, path

def write_file(working_directory, file_path, content) -> str:
    try:
        file_path, isvalid = validate_path(working_directory, file_path)
        if not isvalid:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        if path.isdir(file_path):
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        makedirs(path.dirname(file_path), exist_ok=True)

        with open(file_path, "w") as f:
            c = f.write(content)
        f.close()

        return f'Successfully wrote to "{file_path}" ({c} characters written)'
    except:
        return f'Error: An error occurred while writing to "{file_path}"'
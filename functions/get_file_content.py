from os import path
from config import MAX_CHARS
from functions.get_files_info import validate_path

def get_file_content(working_directory, file_path) -> str:

    try:

        file, is_valid = validate_path(working_directory, file_path)
        if not is_valid:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not path.isfile(file):
            f'Error: File not found or is not a regular file: "{file_path}"'

        f = open(file) 
        content = f.read(MAX_CHARS)

        if f.read(1):
            content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'

        return content
    except:
        return f'Error: error while reading file'